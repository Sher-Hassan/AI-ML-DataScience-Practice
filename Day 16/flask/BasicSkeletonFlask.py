## Understanding Simple Flask App Skeleton

from flask import flask

## WSGI Application

app = flask(__name__) ## It creates an instance of the Flask class, which will be your WSGI (Web Server Gateway Interface) application. The "__name__" parameter will be the first to be check for execution(entry point)

if __name__ == "__main__": ## First of all this will be checked and from here the execution will start
    app.run()

## This was the basic skeleton of flask app Web framework