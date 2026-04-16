# Working With HTTP Verbs Get And Post

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>WELCOME</h1></html>" 


## So the the second argurment in the @app.route is "methods=[]" which by default is set to "methods=["GET"]"

## GET is used to just recieve the files without user's input

## POST is used to retrieve/provide user's input or any action based on those input info.

## We use requests to access HTTP Verbs Get And Post (request.method, request.form)  (from flask import request)

@app.route("/index", methods=["GET"])   
def index():
    return render_template('index.html') 

@app.route("/form", methods=["GET", "POST"])
def myfrom():
    if request.method == "POST":
        name = request.form['name'] # because the input field that We want to retrieve has id="name"
        return f"HELLO  {name}! WELCOMEEEE"
    else:
        return render_template('form.html')
if __name__ == "__main__": 
    app.run(debug=True)