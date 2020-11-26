# UTF-8
# Author : Margaux Faurie
# Date : 26 Nov. 2020


import json
from sqlalchemy.orm import sessionmaker, query
from connection import connect, createdb, checkdb
from datetime import datetime
from createtables import createtables
from populate import populate
import sqlalchemy as db
from models import books
import pandas as pd


startTime = datetime.now()
print("Setup in progress. Please wait.")
dbname = 'booklist'
rawdata = 'data.json'


with open("config.json") as f:
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]


if checkdb(dbname) is True:
    createdb(dbname)
    session = connect(dbname)

    createtables(dbname)
    populate(dbname, rawdata)

    finishTime = datetime.now()
    timeDetla = finishTime - startTime

    print("Setup is finished. Your database is now available.")
    print("The process was completed in : " + str(
        timeDetla.total_seconds()) + "s.")

else:
    print("Your database already exists.")

# ---------------------------
#How to read a database ? 
# ---------------------------

engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
connection = engine.connect()

def printtable(connection):
    result = connection.execute("SELECT * FROM books")
    return pd.DataFrame(result)

print(printtable(connection))


# ---------------------------
#Update book
# ---------------------------

    
query = db.update(books).values(Author=4).where(
        books.Title=="The World as I See It")
results = connection.execute(query)


print("\nDatabase with upadte:\n")
print(printtable(connection))


# ---------------------------
#Suppresion du livre lu "The World as I See It"
# ---------------------------

query = db.delete(books).where(books.Title=="The World as I See It")
results = connection.execute(query)

print("\nDatabase with deleted element:\n")
print(printtable(connection))



