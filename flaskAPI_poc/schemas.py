# Schemas file (schemas.py):
"""This file defines the Pydantic schemas for data validation and serialization/deserialization. Here,
we define BookCreateRequest and BookUpdateRequest schemas to specify the expected fields and their types for creating
and updating books. """

from pydantic import BaseModel

class BookCreateRequest(BaseModel):
    title: str
    author: str

class BookUpdateRequest(BaseModel):
    title: str
    author: str
