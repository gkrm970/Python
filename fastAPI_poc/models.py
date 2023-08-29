# let's create a models.py file to define the structure of the User table in the database:

# models.py
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)


"""Here, we define a User class that inherits from Base, which comes from the database module. The User class 
represents the structure of the users table in the database and includes columns for id, name, and age. """
