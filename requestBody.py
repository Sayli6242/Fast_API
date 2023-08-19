# from fastapi import FastAPI
# from pydantic import BaseModel
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# app = FastAPI()

# # items_dict = []


# # @app.get("/items/")
# # async def get_items():
# #     return items_db


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


from fastapi import FastAPI
from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    full_name: str = None
    phone: int
    email: str = None


app = FastAPI()

contacts_db = []


@app.post("/contacts/")
async def create_contact(contact: Contact):
    contacts_db.append(contact)
    return {"message": "Contact created successfully"}


@app.get("/contacts/")
async def get_contacts():
    return contacts_db
