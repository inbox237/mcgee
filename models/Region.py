from main import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from models.Salesperson import Salesperson

Base = declarative_base()

class Region(db.Model):
    # bind key allows connection to other non-default database
    __bind_key__ = "mcgee_mayblack"
    __tablename__ = "regions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    region_salespersons = db.relationship("Salesperson", back_populates="region_name")
    def __str__(self):
        return self.name
        