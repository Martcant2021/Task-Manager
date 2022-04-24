from sqlalchemy.orm import Session
from models import Task
from flask_sqlalchemy import SQLAlchemy



def get_task_by_id(db:Session, Task_id:int):
    return db.query(Task).filter(Task.id == Task_id).first()

def get_task(db:Session, skip:int=0,limit=100):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db:Session):
    _task = Task(title=Task.title, description=Task.description)
    db.add(_task)
    db.commit()
    db.refresh(_task)
    return _task


def remove_task(db:Session, Task_id:int):
    _task = get_task_by_id(db=db, Task_id=Task_id)
    db.delete(_task)
    db.commit()


def update_task(db:Session, Task_id:int, title:str, description:str):
    _task = get_task_by_id(db=db, Task_id=Task_id)
    _task.title = title
    _task.description = description
    db.commit()
    db.refresh(_task)
    return _task