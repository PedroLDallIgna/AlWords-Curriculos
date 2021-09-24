from flask.templating import render_template
from app import app

@app.route('/')
def index():
    return render_template("public/index.html", title="Hello, World!")
