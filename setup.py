# UTF-8
# Author : Margaux Faurie
# Date : 19 Nov. 2020

from sqlalchemy.orm import sessionmaker, query
from connection import connect, createdb, checkdb
from datetime import datetime
from createtables import createtables
from populate import populate


startTime = datetime.now()
print("Setup in progress. Please wait.")
dbname = 'MF_BOOK_LIST'
rawdata = 'data.json'

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
