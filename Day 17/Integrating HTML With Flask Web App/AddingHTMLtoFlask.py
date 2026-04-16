# Integrating HTML With Flask Web App

from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>WELCOME</h1></html>" ## Adding directly but it is not a good practice, So we can redirect it to HTML files using render_template

@app.route("/index")   ## Using render_template here(good practice), This uses jinja2 Template Engine
def index():
    return render_template('index.html') ## This will look for index.html file inside the "templates" folder which should be located inside the same directory

@app.route("/about")  ## Another example
def about():
    return render_template('about.html')


if __name__ == "__main__": 
    app.run(debug=True)