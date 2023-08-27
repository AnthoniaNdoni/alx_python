# Import necessary SQLAIchemy components
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create an engine to connect to the MySQL server
# Replace "mysql+mysqldb://root:root@localhost/food_db" with your connection URL
# The URL format is "mysql+mysqldb://username:password@host/database_name"
# Connecting to MySQL server at 23.92.23.113 using mysql-python DBAPI 
engine = create_engine("mysql+mysqldb://root:root@localhost/food_db")

# create a session factory
Session = sessionmaker(bind = engine)
session = Session()

# Connect to the database using the engine
connection = engine.connect()

# check if the connction was successful
if connection:
    print("Database is connected") 
else:
    print("database is not connected")
