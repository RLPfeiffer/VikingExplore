import pandas as pd
import pyodbc 
import sqlalchemy as sal
from sqlalchemy import create_engine

#Connect to Data Structure for sqlalchemy is: "mssql+pyodbc://OpR-Marc-DB2:1433/RPC1?driver=ODBC+Driver+17+for+SQL+Server" --change RPC1 for other volumes

engine = sal.create_engine("mssql+pyodbc://OpR-Marc-DB2:1433/RPC1?driver=ODBC+Driver+17+for+SQL+Server")
conn = engine.connect()

#This is just a test of the connection
print(engine.table_names())

#Test query using alchemy interface
q1 = engine.execute("SELECT ID, Label FROM Structure WHERE ID=933")
for row in q1:
    print(row)