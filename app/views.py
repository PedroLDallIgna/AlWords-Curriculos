from flask.templating import render_template
from app import app
from app.forms import SignIn, SignUp

@app.route('/')
def index():
    return render_template("public/index.html", title="Hello, World!")

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = SignIn()
    return render_template("public/signin.html", form=form)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignUp()
    return render_template("public/signup.html", form=form)
