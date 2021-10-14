from flask import Flask, render_template, flash, request
from app.db import DB

app = Flask(__name__)
app.secret_key = 'development key'
db_users = DB('app/database/users.json')
users = db_users.get_users()
data = DB('app/database/users_data.json')

from app import views
