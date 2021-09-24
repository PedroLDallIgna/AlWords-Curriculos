from flask.templating import render_template
from app import app
from app import forms

@app.route('/')
def index():
    return render_template("public/index.html", title="Hello, World!")

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = forms.SignIn()
    return render_template("public/signin.html", form=form)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = forms.SignUp()
    return render_template("public/signup.html", form=form)
