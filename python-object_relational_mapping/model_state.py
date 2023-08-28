"""
Write a python file that contains the class definition of 
a State and an instance Base = declarative_base()
"""
# Import necessary SQLAIchemy components
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define Base class for table class inheritance
Base = declarative_base()

# creat s table for class state
class state(Base):
    """
    class definition for sql table states
    PARAMETER
        Base declarative
    Return:
    base meta data for the creation of state tables
    """
   # define table name
    __tablename__ = 'states'
    # define column for states table
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

