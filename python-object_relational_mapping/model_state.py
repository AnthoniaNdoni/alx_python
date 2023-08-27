from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connecting to MySQL server at 23.92.23.113 using mysql-python DBAPI 
engine = create_engine("mysql+mysqldb://root:root@localhost/food_db")

Session = sessionmaker(bind = engine)
session = Session()

connection = engine.connect()
if connection:
    print("Database is connected") 
else:
    print("database is not connected")
