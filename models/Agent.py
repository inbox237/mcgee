from main import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Agent(db.Model):
    __tablename__ = "agents"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    office_id = db.Column(db.Integer, db.ForeignKey("offices.id"), nullable=True)
    office_name = db.relationship("Office", back_populates="office_agents")