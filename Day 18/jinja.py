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

# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/")
# def welcome():
#     return "<html><h1>WELCOME</h1></html>" 

    

# @app.route("/success/<int:score>")
# def success(score):
#     res = ""
#     if score >= 50:
#         res = "PASS"
#     else:
#         res = "FAIL"
#     return render_template('result.html', results=res) ## I created results variable and passed data in it. This results variable can be accessed in results.html using {{}} which is jinja2 template engine


# if __name__ == "__main__": 
#     app.run(debug=True)

## So in Jinja2 Template Engine
'''
1. {{}} expressions to print output in html (expressions)
2. {%...%} conditions, loops (statements)
3. {#...#} this is for comments

'''

## Using {%...%} conditions (index1.html)

# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/")
# def welcome():
#     return "<html><h1>WELCOME</h1></html>" 

    

# @app.route("/successres/<int:score>")
# def successres(score):
#     res = ""
#     if score >= 50:
#         res = "PASS"
#     else:
#         res = "FAIL"

#     exp = {'score': score, "res": res}
#     return render_template('index1.html', results=exp) ## exp is passed as key value pairs and can be accessed by for loop in index1.html

# if __name__ == "__main__": 
#     app.run(debug=True)

## Using redirect(url_for('routename', data=))
# in the backed we can use this for redirecting to another route and also pass data

## Using an example
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/marksform", methods=["GET","POST"])
def marksform():
    return render_template("exampleform.html")

@app.route("/calculate", methods=["GET","POST"])
def calculate():
    total_score=0
    if request.method=='POST':
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        english=float(request.form['english'])
        histroy=float(request.form['history'])
        geography=float(request.form['geography'])

        total_score=(maths+science+english+histroy+geography)/5
    
    return redirect(url_for("successmarks", score= total_score))

@app.route("/successmarks/<int:score>")
def successmarks(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score': score, "res": res}
    return render_template('index1.html', results=exp)

if __name__ == "__main__": 
    app.run(debug=True)