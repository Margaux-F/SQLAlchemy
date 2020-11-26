# UTF8
# Date: 26 Nov. 2020
# Author: Margaux Faurie

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from connection import connect

session = connect('aam_test_301')

Base = declarative_base()



class books(Base):
    """docstring for """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, nullable = False)
    Title = Column(String(20), nullable = True)
    Author = Column(String(20), ForeignKey("authors.id"), nullable = True)

class authors(Base):
    """docstring for """
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    First_Name = Column(String(20), nullable = True)
    Last_Name = Column(String(20), nullable = True)
    Date_Birth = Column(String(20), nullable = True)
    Date_Death = Column(String(10), nullable = True)
    Nationality = Column(String(5), ForeignKey("nation.Name"), nullable = True)

class nation(Base):
    """docstring for"""
    __tablename__ = "nation"
    id = Column(Integer, primary_key = True)
    Name = Column(String(5), nullable = True)
