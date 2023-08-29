"""This file defines the db object, which is an instance of SQLAlchemy. It acts as the interface between Flask and
the database.
Database file (database.py):
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
