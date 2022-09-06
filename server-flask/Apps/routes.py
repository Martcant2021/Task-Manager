from Apps import app
from flask import Flask, jsonify, render_template, request, redirect, url_for
from Apps.config import db
from Apps.models import Task
from Apps.task_serializer import task_serializer, task_response



@app.route("/task", methods=["GET"])
def home():
    # Task_id = db.query(Task).filter(Task.id == Task_id).first()
    Tasks = Task.query.all()
    return jsonify([*map(task_serializer, Tasks)])
    # return render_template('index.html', Tasks=Tasks)



@app.route("/task/create", methods=['POST'])
def create_task():
    # title = request.form['title']
    # description = request.form['description']
    # _task = Task(title, description)
    # task= task_data('title')
    task_data = request.get_json()
    title = task_data.get('title')
    _task = Task(title=title)
    db.session.add(_task)
    db.session.commit()

    return task_response(201,'Successfully added task',task_serializer(_task))



@app.route('/task/delete/<int:id>', methods=["POST"])
def remove_task(id):
    _task = Task.query.get(id)
    if not _task:
        return task_response(404,'task not found')

    db.session.delete(_task)
    db.session.commit()
    return task_response(200, 'Success delete')



@app.route('/task/<int:id>', methods=["GET"])
def resolve_task(id):
    _task = Task.query.filter_by(id=id).first()

    if not _task:
        return task_response(404,'task not found')

    return jsonify(task_serializer(_task))

