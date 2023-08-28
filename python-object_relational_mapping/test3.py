from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State




# Connecting to MySQL server at 23.92.23.113 using mysql-python DBAPI 
engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

Session = sessionmaker(bind = engine)
session = Session()

result = session.query(State).all()

