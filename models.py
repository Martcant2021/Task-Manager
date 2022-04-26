from sqlalchemy import Column, String, Integer, Boolean
from app.config import db
from flask_sqlalchemy import SQLAlchemy


class Task(db):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(Boolean)


    def __init__(self, id ,title, description, status ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status



