## FAST API
- Is a WEB Framework


## Uvicorn
Like for react there is NOde, for php there is XAMPP and here uvicorn will be used.

##
When a user enters the website you want it to return something So in python for this we make a function.
so inside main.py:

def greet():
    return "Welcome to my website"

and now we can use our webserver Uvicorn to run this.
using "uvicorn main --reload" command.

 ERROR:    Error loading ASGI app. Import string "main" must be in format "<module>:<attribute>".

the error mentions that the module is ther but where is the attribute. We are using FAST APi bunot mentioning anywhere. SO, We import FASTApi and make its object and then run our serever with the attribute.

main.py:

from fastapi import FastAPI

app = FastAPI()

def greet():
    return "Welcome to my website"

command: uvicorn main:app --reload

For now it will provide us with {"detail":"Not Found"} because we have not specified endpoints.

# REST API

So the web client sends request to the backend, the backend examines and executes the request with the database and then sends the response back to the client. Now cant be just any command—it needs to follow a standardized structure so both sides perfectly understand each other.

REST (Representational State Transfer) provides this predictable rulebook. Instead of inventing custom instructions for every single action, REST treats everything as a **resource** (like a user, a blog post, or a product) and relies on standard HTTP methods to interact with them:

* **GET:** Read or fetch a resource.
* **POST:** Create a new resource.
* **PUT / PATCH:** Update an existing resource.
* **DELETE:** Remove a resource.

Because these rules are universal, any client—whether it's a web browser, a mobile app, or a smart TV—can communicate seamlessly with the backend without needing a custom translation manual.

So now in my main.py: I can use get method to read

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to my website"

Now our website will show "Welcome to my website"

##  Pydantic
is for Data Validation and if you want to convert data from the server side to JSON format to send it to client. we will use this. 
for example user enter negative value age or price or maybe 2 characters name so this is not possible alyhough they will still satisfy the data type. So for such data validation we use Pydantic.

So inside our models.py;

from pydantic import BaseModel #Import base model

class Product(BaseModel): #Inherit base model
    id: int
    name: str
    description: str
    price: float
    quantity: int

# Now we dont need this constructor after pydantic(Commented out)

    # def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

In FAST API we ha SWAGGER UI by default to test out out Backend Just add /docs at the end of the URL

# Dynamic data fetching use {}
@app.get("/product/{id}")
def getProductById(id: int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found"

# Data adding using POST
@app.post("/product")
def addProduct(product: Product):
    products.append(product)
    return product

# Update Method
@app.put("/product")
def updateProduct(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully"
    return "No product Found"

# Delete Method
@app.delete("/product")
def deleteProduct(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "Product Not found"

## SQL Alchemy
SQLAlchemy is an open-source library used to interact with relational databases using Python code instead of raw SQL. It functions as both a database toolkit and an Object-Relational Mapper (ORM), allowing developers to map database tables directly to Python classes

# DB configuration
# Creating object of SessionLocal and then we can use it in our app for database connection
# Everytime you connect to something that is a session
# to create a session we have sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# sessionmaker has parameters
# Whenever we do database transactions noramlly we have to do commits for it but by default it will be autocommit=false and we can set to false or true
#autoflush is a configuration setting that forces the Session to automatically write pending in-memory data changes to the database transaction immediately before any new query is executed.
# passing bind=engine into sessionmaker links your database driver configurations directly to your session factory. This setting ensures that every individual Session instance generated by that factory automatically knows which database to communicate with and where to request connection resources.
#When Session = sessionmaker(bind=engine) is called, you are establishing a default database target. Whenever a newly generated session needs to execute a query or flush data, it silently goes to that specific engine, checks out a physical connection, runs the SQL, and returns the connection to the pool when done.

db_url = "postgresql://postgres:12345678@localhost:5432/FASTAPI_Practice"

engine = create_engine(db_url)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

## Go to where you want to use your db (main.py in this case)
 import database session from the dbconfig using "from dbconfig import session"
 make db session "db = Session()" in any function inside endpoints
 Execute query by using "db.query(<query>)"

 We don't need to write actual SQL query because of SQLAlchemy. 

 Now for mapping the database and the class. The classes in models.py are pydantic. so we have to create another kind of class based on SQL Alchemy for database. So the database schema will be created based on that particular class.

 We can mention column types, name and some filters or special access like Foreign keys, Primary keys etc. We cant do that inside pydantic base model classes.

 So we need a class for data validation (Pydantic) and a seperate class for SQL Alchemy. 

 My pydanyic models are in models.py and SQL Alchemy models in dbModels.py for now.

 Now in main.py we can create tables according to our models in dbmodels.py and import engine from dbconfig
 
 import dbmodels

Then I will say in main that hey use the metadata in dbmodels to create tables and bind to engine (main.py)

dbmodels.Base.metadata.create_all(bind=engine)

Now I want to insert data into my POSRGRESQL using SQL Alchemy.
SO i want to make a condition that whenever i open my application it should check if the table is empty, populate with dummy data, if there is any data then don't do it.

to acheive that we will create a function (main.py for now)

def db_init():
    db = Session()  # first we need connection object

    for product in products:  # Adding products
    db.add(product)  # add products in it
init_db()

    # Now here we will have a problem, the DB is working with database model class of product which is connected to SQL Alchemy, but in the code the product we are using is not SQL Alchemy product it is actually Pydantic model, so this will not work. We need to somehow convert this to SQL Alchemy product. We cannot pass object of product (model pydantic) but a product of SQL Alchemy. How we are going to do it?

lets rewrite:

We need to convert the product in for loop to SQL Alchemy product. So we can pass it to dbmodels.Product(product). Now the model in dbmodels.py the Product(Base) accepts key value pairs for converting it and will create an object for it. Now how to pass a key value pair?
We can use .model_dump() on our pydantic model to convert it into dictionary and use Pythons syntax (**) for unpacking it for getting raw key value pairs. So it becomes db.add(dbmodels.Product(**product.model_dump())) 

In our dbconfig.py autocommit = False so that is why it wont execute so we need to db.commit().

def db_init():
    db = Session()  # first we need connection object

    for product in products:  
        db.add(dbmodels.Product(**product.model_dump())) 
    db.commit()

init_db()

Now added data.
Note: We have to make sure that we are adding database entries of SQL Alchemy(dbmodels.py in this case) not pydantic models(models.py in this case). we have to convert the pydantic object using model_dump which gives dictionary and use ** to unpack it for raw key value pairs and feed it to database.

Now we everytime we reload the server it will try to again put same values into database but it will provide error because there is primary key. So how to fix that. Lets add:

I dont want it to call this every time i load this. It should do its job only if table is empty. so baically we can check this before we do that. Added count and if condition to track.

to get something we use db.query() and for adding we use db.get() So for getting the count of queries to track count. we will use db.query(dbmodels.Product).count on count variable.


def db_init():
    db = Session() 

    count = db.query(dbmodels.Product).count
    if count == 0:
        for product in products:  
            db.add(dbmodels.Product(**product.model_dump())) 
        db.commit()

db_init()

Note:In normal project we dont need to do it normally because data might already be there or we might add data manually.

Now we have another problem:
Everytime we need to use database we have to repeatedly use:
db = Session()

# Dependency Injection

we are repeatedly creating a session and not closing it. Not a good idea.
We should have one place where when we need it we will use it then the connection will be closed

Note: The yield keyword in Python is used to turn a standard function into a generator function. Instead of computing all values at once and returning them as a finished list, yield produces data lazily—one item at a time—on demand.

So we can make a function of getting database:

def get_db():
    db = Session()
    yield db
    db.close()

imagine if something goes wrong inside "yield db". I still want to close the connection, not just when the "yield db" works fine so for thay we will add try and finally blocks.(error handling)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Dependency injection (DI) in Python is used to pass external resources—such as database connections, configuration settings, or API clients—directly into a class or function rather than having the code create them internally.

Now how we are going to get the use of get_db() using dependency injection.

for example I will use it in getAllProducts():
getAllPrducts() needs to ask for the dependency. it will not be given by default.

first import Session of sqlalchemy.orm(not the local session we created) and also import Depends from fastapi

Note: if Session of sqlalchemy.orm conflicts we can use "as" keyword and rename it to anything then use for example (from sqlalchemy.orm import Session as DBSession)

from fastapi import Depends
from sqlalchemy.orm import Session

How to inject:

I want db of type session and this depends "def getAllProducts(db: Session = Depends(get_db)):". This is how database is injected to the function and now we can use our database in this function.

How to use(example: getting all products)

@app.get("/products")
def getAllProducts(db: Session = Depends(get_db)):
    db_products = db.query(dbmodels.Product).all()

    return db_products

So in this line "db_products = db.query(dbmodels.Product).all()" we created an object "db_products" and used query and specified which model I need in bracket arguments "db.query(dbmodels.Product)" which is SQL Alchemy model. and I need all of them so .all().

# CRUD Operations (Read already done)
# with database Dependency Injection and SQL Alchemy

# Specific Read
@app.get("/product/{id}")
def getProductById(id: int, db: DBSession = Depends(get_db)):
    db_product = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_product:
        return db_product

    return "Product not found"

# Create
@app.post("/product")
def addProduct(product: Product, db: DBSession = Depends(get_db)):
    db.add(dbmodels.Product(**product.model_dump()))
    db.commit()
    return product

# Update
@app.put("/product")
def updateProduct(id: int, product: Product, db: DBSession = Depends(get_db)):
    db_product = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        return "Product updated Successfully"
    else:
        return "Product Not Found" 

# Delete 
@app.delete("/product")
def deleteProduct(id: int, db: DBSession = Depends(get_db)):
    db_product = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    else:
        return "Product Not found"