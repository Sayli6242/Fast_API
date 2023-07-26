# from fastapi import FastAPI
from typing import Annotated

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI()


# app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# from typing import Annotated

# from fastapi import FastAPI, Path
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# # from typing import Annotated

# # from fastapi import Body, FastAPI
# # from pydantic import BaseModel

# # app = FastAPI()


# # class Item(BaseModel):
# #     name: str
# #     description: str | None = None
# #     price: float
# #     tax: float | None = None


# # class User(BaseModel):
# #     username: str
# #     full_name: str | None = None


# # @app.put("/items/{item_id}")
# # async def update_item(
# #     item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
# # ):
# #     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
# #     return results


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class User(BaseModel):
#     username: str
#     full_name: str | None = None


# @app.get("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)],
#     q: str | None = None,
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results
