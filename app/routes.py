from app import app
from app import config as db
from flask import render_template



@app.route("/")
def home():
    return render_template('index.html')

