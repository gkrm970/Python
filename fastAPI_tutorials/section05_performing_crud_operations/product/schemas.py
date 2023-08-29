# from product.model import Product
from pydantic import BaseModel, validator
from typing import Optional


class Seller(BaseModel):
    username: str
    email: str
    password: str


class DisplaySeller(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    name: str
    description: str
    price: int


# this class will be used when the requirements like selected field should be present in response, then you should use this class.
class DisplayProduct(BaseModel):
    name: str
    description: str
    seller = DisplaySeller

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token :str
    token_type :str

class TokenData(BaseModel):
    username :Optional[str] = None