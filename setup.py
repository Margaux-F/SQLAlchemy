# UTF8
# Date: 26 Nov. 15h39
# Author: Margaux Faurie

import json
from sqlalchemy.orm import sessionmaker, query
from connection import connect, createdb, checkdb
from datetime import datetime
from createtables import createtables
from populate import populate
import sqlalchemy as db
from models import books
import pandas as pd

#-----------------------------
# Create the database --> C
# ----------------------------

startTime = datetime.now() #Take the time to know how long the set up lasted
print('\n\n----------------------------------------------------')
print("Setup in progress. Please wait.")
print('----------------------------------------------------\n')

dbname = 'booklist' #Name the database
rawdata = 'data.json' #Where does the raw data comes from


with open("config.json") as f: #Load data for the configuration
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

def Checkdb(dbname):
    prgrm = 1
    if checkdb(dbname) is True: #Check the existance of the database (if exists or not)
        createdb(dbname) #Create the database
        session = connect(dbname) #Connect to the database

        createtables(dbname) #Create the tables
        populate(dbname, rawdata) #Populate the database

        finishTime = datetime.now() #End of the set up
        timeDetla = finishTime - startTime

        print('\n----------------------------------------------------')
        print("Setup is finished. Your database is now available.")
        print("The process was completed in : " + str(
            timeDetla.total_seconds()) + "s.") #Total time
        print('----------------------------------------------------\n')
        return prgrm
    else:
        print("Your database already exists.")
        print('Do you want to delete the tables to run the program anyway ?')
        print('1 = Delete the tables and recreate others.\n')

        try:
            Choice = int(input('Your choice : '))
        except ValueError:
            print("The input is not right...\n")
            prgrm = 0
            return prgrm

        if Choice == 1:
            engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
            connection = engine.connect() #Connect

            session = connect(dbname) #Connect to the database

            query = db.delete(books)
            results = connection.execute(query)


            populate(dbname, rawdata) #Populate the database
            return prgrm
        else : 
            prgrm = 0
            print('The program will not run')
            return prgrm

        print('----------------------------------------------------\n')

prgrm = 1 
prgrm = Checkdb(dbname)
if prgrm == 1:
    # ---------------------------------
    # How to read a database ?  --> R
    # ---------------------------------

    engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
    connection = engine.connect() #Reconnect to the database

    def printtable(connection): # Def a function that print a database using pandas
        return pd.DataFrame(connection.execute("SELECT * FROM books"))

    print("Original database:\n")
    print(printtable(connection))
    print('\n----------------------------------------------------\n')


    # ---------------------------
    # Update book  --> U
    # ---------------------------

    query = db.update(books).values(Author=4).where(books.Title=="The World as I See It")
    results = connection.execute(query)

    print("Database with update:\n")
    print(printtable(connection))
    print('\n----------------------------------------------------\n')


    # ------------------------------------------------------
    # Suppresion du livre lu "The World as I See It" --> D
    # ------------------------------------------------------

    query = db.delete(books).where(books.Title == "The World as I See It")
    results = connection.execute(query)

    print("Database with deleted element:\n")
    print(printtable(connection))
    print('\n----------------------------------------------------\n')
else:
    print('You asked not to run the program')
