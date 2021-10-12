from flask import Flask, render_template, flash, request
from app.db import DB

app = Flask(__name__)
app.secret_key = 'development key'
db = DB('app/database/users.json')
users = db.get_users()

from app import views
