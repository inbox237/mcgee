from main import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Salesperson(db.Model):
    # bind key allows connection to other non-default database
    __bind_key__ = "mcgee_mayblack"
    __tablename__ = "salespersons"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=True)
    region_name = db.relationship("Region", back_populates="region_salespersons")