from flask import jsonify


def task_serializer(task):
    task_view ={
    "id": task.id,
    "title": task.title,
    "status": task.status,

    }
    return task_view

def task_response(code, message, task=None):
    if task:
        return jsonify({'code':code, 'message':message, 'task':task}), code
    return jsonify({'code':code, 'message':message}), code