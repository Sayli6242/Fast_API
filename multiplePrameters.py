from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = none


class User(BaseModel):
    username: str
    full_name: str = None
    # full_name is optional for user, program run continuously even if user cannot provide their full_name
