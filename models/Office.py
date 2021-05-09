from main import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from models.Agent import Agent

Base = declarative_base()

class Office(db.Model):
    __tablename__ = "offices"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    office_agents = db.relationship("Agent", back_populates="office_name")
    def __str__(self):
        return self.name
        #return f"{{\n\tid: {self.id}\n\tname: {self.name}\n}}"