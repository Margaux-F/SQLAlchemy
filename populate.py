# UTF-8
# Author : Margaux Faurie
# Date : 19 Nov. 2020

import json
import datetime
from connection import connect
from random import shuffle
from models import authors, nation, books


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
                           Last_Name = i["Last_Name"],
                           )
        session.add(Authors)

    for i in data['Nation']:
        Nation = nation(country = i["Name"])

    session.commit()
