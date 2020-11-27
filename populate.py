# UTF8
# Date: 26 Nov. 2020
# Author: Margaux Faurie


import json
import datetime
from connection import connect
from random import shuffle
from models import books, authors, nation


def populate(dbname, jsondata):
    """docstring for populate"""
    session = connect(dbname)

    with open(jsondata) as f:
        data = json.load(f)

    for i in data['books']:
        book_name = books(Title = i["Title"])
        session.add(book_name)

    for i in data['authors']:
        Authors = authors(First_Name = i["First_Name"],
                           Last_Name = i["Last_Name"]
                           )
        session.add(Authors)

    for i in data['Nation']:
        Nation = nation(Name = i["Name"])

    session.commit()
