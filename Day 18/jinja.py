# Building Dynamic Url ,Variables Rule And Jinja 2 Template Engine

# from flask import Flask, render_template, request

# app = Flask(__name__)

# ## I can hit these routes by action="/routeName" in the from element too is another way

# @app.route("/")
# def welcome():
#     return "<html><h1>WELCOME</h1></html>" 


# @app.route("/index", methods=["GET"])   
# def index():
#     return render_template('index.html') 

# @app.route("/form", methods=["GET", "POST"])
# def myfrom():
#     if request.method == "POST":
#         name = request.form['name'] 
#         return f"HELLO  {name}! WELCOMEEEE"
#     else:
#         return render_template('form.html')
# if __name__ == "__main__": 
#     app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/")
# def welcome():
#     return "<html><h1>WELCOME</h1></html>" 



# @app.route("/submit", methods=["GET", "POST"])
# def myfrom():
#     if request.method == "POST":
#         name = request.form['name'] 
#         return f"HELLO  {name}! WELCOMEEEE"
#     else:
#         return render_template('form.html')
    
# ### 1. Variable Rule
# # @app.route("/success/<score>")
# # def success(score):
# #     return f"The marks you got is {score}"

# ## Adding type
# @app.route("/success/<int:score>")
# def success(score):
#     return f"The marks you got is {score} and in string it is "+ str(score) ## we can type cast too

# if __name__ == "__main__": 
#     app.run(debug=True)



### 2. Building URL Dynamically

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>WELCOME</h1></html>" 

    

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results=res) ## I created results variable and passed data in it. This results variable can be accessed in results.html using {{}} which is jinja2 template engine


if __name__ == "__main__": 
    app.run(debug=True)

## So in Jinja2 Template Engine
'''
1. {{}} expressions to print output in html
2. {%...%} conditions, loops
3. {#...#} this is for comments

'''

## Start from 13:48