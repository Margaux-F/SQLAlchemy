# UTF-8
# Author : Margaux Faurie
# Date : 19 Nov. 2020

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy import Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from connection import engine


def createtables(name):
    """Create tables in OC Pizza DB"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind = engin)

    authors = Table(
        'authors', metadata,
        Column('id', Integer, primary_key = True),
        Column('First_name', String(20), nullable = True),
        Column('Last_Name', String(20), nullable = True),
        Column('Date_Birth', String(20), nullable = True),
        Column('Date_Death', String(20), nullable = True),
        Column('Nationality',Integer , ForeignKey('Nation.id'))
    )

    Nation = Table(
        'Nation', metadata,
        Column('id', Integer, primary_key = True),
        Column('Name', Integer, nullable = True)
        
    )

    books = Table(
        'books', metadata,
        Column('id', Integer, primary_key = True), 
        Column('Title', String(40), nullable = True),
        Column('Author',Integer , ForeignKey('authors.id')),
    )


    # Create all tables
    metadata.create_all(engin)
