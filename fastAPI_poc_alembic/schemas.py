# Now, let's create a schemas.py file to define Pydantic models for request and response validation:

# schemas.py
from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    name: str
    age: int


class UserResponse(BaseModel):
    id: int
    name: str
    age: int

class UserUpdateRequest(BaseModel):
    name: str
    age: int

"""In this file, we define a UserCreateRequest model that represents the expected structure and types for the request 
body when creating a user. We also define a UserResponse model for the response structure when retrieving a user. """
