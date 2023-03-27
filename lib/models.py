from sqlalchemy import create_engine, func
from sqlalchemy import PrimaryKeyConstraint, ForeignKey, Table, Column, Integer, Float, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///pet_stores.db')

Base = declarative_base()