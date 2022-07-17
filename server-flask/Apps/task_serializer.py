from flask import jsonify


def task_serializer(task):
    task_view ={
    "id" :task.id,
    "title" : task.title,
    "description" :task.description,
    "status" : task.status,

    }
    return task_view

