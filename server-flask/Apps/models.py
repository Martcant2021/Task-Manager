
from flask_sqlalchemy import SQLAlchemy
from Apps.config import db




class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String)
    status = db.Column(db.Boolean(), default=False, nullable = False)


    def __init__(self,title ):
        self.id
        self.title = title
        self.status = False

    def __repr__(self) -> str:
        return '<title %s>' % self.title


