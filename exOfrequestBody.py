from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# contact app
"""
note: array index is uniqueID for contact.
1) user can add contact
    a. name and phone is mandatory , fullname and email is optional.
2) user can update contact
    a. update user by their uniqueID 
    b. user can update name, phone, fullname and email
    c. user can perform partial update or full update.

3) user can retrieve contact
    a. retrieve contact detail by uniqueID for single contact
    b. retrive list of all contacts.
    c. retrieve list of contact by pagination(10 contacts at a time).

4) user can delete contact
    a. delete contact by uniqueID.
"""


class Contact(BaseModel):
    name: str
    full_name: str = None
    phone: int
    email: str = None


app = FastAPI()

contacts_db = []


# create contact with post request
@app.post("/contacts/")
async def create_contact(contact: Contact):
    contacts_db.append(contact)
    return {"message": "Contact created successfully"}


# to view all contacts lsit
@app.get("/contacts/")
async def get_contacts():
    return contacts_db


# to retrieve contact by perticular id
# @app.get("/contacts/{id}")
# async def get_contacts(id: int):
#     if 0 <= id <= len(contacts_db):
#         contacts_db[id]
#     return contacts_db[id]


@app.get("/contacts/")
async def get_contacts(start_point: int = 0, contacts_per_page: int = 3):
    end_point = start_point + contacts_per_page
    contact_on_page = contacts_db[start_point:end_point]
    return {"message": contact_on_page}


# # to perform full update
# @app.put("/contacts/{id}")
# async def update_contacts(id: int, contact: Contact):
#     if 0 <= id <= len(contacts_db):
#         contacts_db[id] = {
#             "name": contact.name,
#             "email": contact.email,
#             "phone": contact.phone,
#             "full_name": contact.full_name,
#         }
#         return {"message": "Contact updated successfully"}
#     else:
#         return {"message": "Contact not found"}


# to perform partial update
@app.put("/contacts/{id}")
async def update_contacts(id: int, contact: Contact):
    if 0 <= id <= len(contacts_db):
        contact_in_list = contacts_db[id]
        if contact.full_name is not None:
            contact_in_list["full_name"] = contact.full_name

        if contact.email is not None:
            contact_in_list["email"] = contact.email

        return {"message": "Contact partially updated successfully"}
    else:
        return {"message": "Contact not found"}


# delete contact
@app.delete("/contacts/{id}")
async def delete_contacts(id: int):
    if 0 <= id <= len(contacts_db):
        deleted_contact = contacts_db[id]
        contacts_db.remove(delete_contacts)
        return {"message": "contact delete successfully"}
    else:
        return {"message": "contact not found"}
