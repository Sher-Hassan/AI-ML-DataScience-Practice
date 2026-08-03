## Alembic
Alembic is a lightweight database migration tool for Python written by the creator of SQLAlchemy. It handles tracking, creating, and applying schema changes safely across different environments.

Install alembic and psycopg2 in the virtual environment

# Migration Environment
Usage of Alembic starts with creation of the Migration Environment. This is a directory of scripts that is specific to a particular application. The migration environment is created just once, and is then maintained along with the application’s source code itself. The environment is created using the init command of Alembic, and is then customizable to suit the specific needs of the application.

The structure of this environment, including some generated migration scripts, looks like:
yourproject/
    alembic.ini
    pyproject.toml
    alembic/
        env.py
        README
        script.py.mako
        versions/
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
            3adcc9a56557_rename_username_field.py


Run "alembic init <Environment_name>" command to create a migration environment

It creates "alembic.ini" file and this is where the alembic scripts look for when we invoke the alembic commands.

We also get the <environent_name> folder with versions folder(initially empty) and env.py
env.py is a python script that is run anytime the alembic migrations are invoked. This file will always be running when we perform our migrations.
It is going to use SQL Alchemy and its provided engine to connect to database.

# Now we are going to tell Alembic how to connect to our database in docker container

- Go to alembic.ini file and find sqlalchemy.url 
- "sqlalchemy.url = driver://user:pass@localhost/dbname". We need a driver(postgres/mySql etc). We need user and password, localhost and the name of the database.
- So for this practice i replaced it with "postgresql://postgres:secret@localhost/alembic_db" whic I previously created.

# Lets create Migrations
- run "alembic revision -m "<message>"
- It is going to create migration inside <environment_name>/versions/<hashid>.py

- Inside that migration version we can find "down_revision" set to "None". It is set to None in only first migration. The purpose of this variable is to point to the ID of the previous migration in alembic configeration.

- There will be two functions named "upgrade()" and "downgrade()"

- In alembic we can add code to both these functions to tell it what happens on upgrade and on downgrade.

- Later we can auto-generate the code that is added to these functions from SQL Alchemy models.

- We have imported "from alembic import op" and "import sqlalchemy as sa". So we can use them for database operations inside our upgrade and downgrade functions in our migrations.

-upgrade() example:

def upgrade() -> None:
    op.create_table(
        "employee",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("current", sa.Boolean, default=True)
    )

-downgrade() example:

def downgrade() -> None:
    op.drop_table("employee")

# Running Migration against the database
- alembic upgrade <revision_id>/head  # Revision id is found in migration file if we want to upgrade to specific migration, head can be used for most recent migration. Now upgrade function will execute.

- we can see the database using docker exec command "docker exec -ti <containerName> <connectUsing(ex.psql)> <user> -d <databaeName>". and then command "\dt" to show all tables and also enter any kind of query like "select * from employees;" and "\q" to quit.

- We can add another revision/migration using "alembic revision -m <message>" command.

-Now in this version we have "down_revision: '6909a6a9797e'" which points to previous revision. This was None in first migration. This is used to keep track of the historical data of revisions. We can again define the upgrade and downgrade functions to use them and we can also make other migrations after this.

- Now when we tun the command "alemic upgrade head" it is going to apply what was coded in upgrade function.

- we can also use "alembic history" command to be provided with upgrade history in terminal "Running upgrade 6909a6a9797e -> 9da62ec54f38, add job_title column"

- We can track all these changes in our pgadmin 4 by connecting our postgres container database to a server in pgadmin 4.

# Downgrading in Alembic
To downgrade we can apply relative migration
# Relative Migration
Relative Migration operate in place from the current migration.
To get the current migreation "alembic current" command.

- To relatively downgrade we can use command "alembic downgrade <n>" where n can be any negative number and it is going to downgrade realtively from current migration.

- We can use "alembic upgrade <n>" where n can be any positive number to upgrade relatively.

- To completely downgrade we can use "alembic downgrade base" command. That is going to completely reverse everything and go back to its original state.

- To completely upgrade we can use "alembic upgrade head" command. That is going to completely upgrade everything and go back to its upgraded state.

# Auto-Generate Migrations from SQL Alchemy Models
Writing migrations by hand is tedious and easy to get wrong, a forgotten index or a mistyped column type only surfaces once it hits production. Alembic solves this with autogeneration: it inspects your SQLAlchemy models, compares them to the live database schema, and produces a migration script containing exactly the differences. You review the result, adjust anything it couldn't infer, and commit it alongside your model changes.

This works because Alembic reads the same MetaData object your models are registered on. Once target_metadata is wired up in env.py, a single alembic revision --autogenerate is enough to keep schema and code in sync.This places so-called candidate migrations into our new migrations file. We review and modify these by hand as needed, then proceed normally.

Note:
One thing worth flagging in the section itself: autogenerate detects table and column additions/removals and most type changes, but it won't catch things like column renames (it sees a drop plus an add), server-side default changes, or constraint tweaks on some backends. The generated script is a draft, not a final answer.

To use autogenerate, we first need to modify our env.py so that it gets access to a table metadata object that contains the target. Suppose our application has a declarative base in myapp.mymodel. This base contains a MetaData object which contains Table objects defining our database. We make sure this is loaded in env.py and then passed to EnvironmentContext.configure() via the target_metadata argument. The env.py sample script used in the generic template already has a variable declaration near the top for our convenience, where we replace None with our MetaData. Starting with:

Replace in .env:
From:
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

To:
from myapp.mymodel import Base
target_metadata = Base.metadata

- Then we can use the "alembic revision --autogenerate -m <message>" command for autogeneration of migrations/revisions.