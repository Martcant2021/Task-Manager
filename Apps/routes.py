from Apps import app
from flask import Flask, render_template, request, redirect, url_for
from Apps.config import db
from Apps.models import Task



@app.route("/")
def home():
    # Task_id = db.query(Task).filter(Task.id == Task_id).first()
    Tasks = Task.query.all()
    return render_template('index.html', Tasks=Tasks)



@app.route("/create", methods=['POST'])
def create_task():
    title = request.form['title']
    description = request.form['description']
    _task = Task(title, description)
    db.session.add(_task)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def remove_task(id):
    Tasks = Task.query.get(id)

    db.session.delete(Tasks)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:id>')
def resolve_task(id):
    Tasks = Task.query.get(id)

    if not Tasks:
        return redirect('/')
    if Tasks.status:
        Tasks.status = False
    else:
        Tasks.status = True

    db.session.commit()
    return redirect('/')

