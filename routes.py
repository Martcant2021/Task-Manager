from crypt import methods
from app import app
from flask import render_template, jsonify
from app import crud



@app.route("/")
def home():

    return render_template('index.html')


@app.route("/create", methods = ['POST'])

def create():
    crud.create_task()
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

