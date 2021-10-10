from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = 'development key'

from app import views
