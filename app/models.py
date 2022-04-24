from turtle import title
from xmlrpc.client import Boolean
from sqlalchemy import Column, String, Integer, Boolean
from config import db
from app import app

class Task(db):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(Boolean)


