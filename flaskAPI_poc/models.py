# Database models file (models.py):

from database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

"""This file defines the database models using SQLAlchemy syntax. In this example, we define a Book model with three 
columns (id, title, author). """

"""This line creates the necessary database tables based on the defined models. You typically call this line once at 
the beginning of your application to create the tables if they don't already exist. """