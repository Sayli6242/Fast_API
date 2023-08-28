"""
grampachayt website

requirements
1) add user data
    a. name, adress, cast, DOB etc.
2) update user data
    a. name, adress, casr DOB etc.
3) retrieve user data
    a. by name, DOB,cast .


"""
"""
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.

"""
from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    name: str
    address: str | None = None
    DOB: str | None = None


class Goods(BaseModel):
    cost: int
    quantity: int
    # tax: int


p_info = []


# add user data


@app.post("/person/")
def add_person_info(person: Person, goods: Goods):
    p_info.append(person)
    return {"message": "person data added successfully"}


@app.get("/person/")
def all_person_info():
    return p_info


# update user data
@app.put("/person/{person_Id}")
def update_person_info(person_ID: int, update_person: Person, goods: Goods):
    if person_ID < len(p_info):
        p_info[person_ID] == update_person
        return {"message": "update person info successfylly"}
    else:
        return {"error": "person_id not found"}


@app.put("/person/{person_Id}/goods")
def update_goods_info(person_Id: int, goods: Goods):
    if person_Id < len(p_info):
        p_info[person_Id].goods = goods
        return {"message": "goods information succesfully update"}
    else:
        return {"error": "person_Id not found"}


# retrieve user data
