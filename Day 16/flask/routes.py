## Adding Routes to Basic Skeleton

from flask import Flask


app = Flask(__name__)

## Lets say Google.com is the home page of this application

@app.route("/")  ## This "/" will be my home page
def welcome():
    return "Welcome to this Flask App"

@app.route("/index")
def index():
    return("Welcome to the index page")

if __name__ == "__main__": 
    # app.run()
    app.run(debug=True) ## By adding "debug=True" the server will automatically restart on updates to codes otherwise it will not and we will have to restart the server

## app.run() parameters:
# (host: str | None = None, port: int | None = None,
# debug: bool | None = None, load_dotenv: bool = True,
# **options: Any) -> None

# host: the hostname to listen on. Set this to `"0.0.0.0"` to

# Runs the application on a local development server.

# Do not use `run()` in a production setting. It is not intended to
# meet security and performance requirements for a production
# server.

# Instead, see `/deploying/index` for WSGI server
# recommendations.

# If the `debug` flag is set the server will automatically reload for code

## I can run this using "python ./routes.py" in terminal

## Code without comments (Basic Skeleton + adding routes)

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def welcome():
#     return "Welcome to this Flask App"

# @app.route("/index")
# def index():
#     return("Welcome to the index page")

# if __name__ == "__main__": 
#     app.run(debug=True)