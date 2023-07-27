from fastapi import FastAPI

app = FastAPI()


# @app.get("/items/")
# async def read_item(item_id: int, category: str = None):
#     response = {"item_id": item_id}
#     if category:
#         response["category"] = category
#     return response


@app.get("/search_employees")
def search_employee(name, age):
    return {"name": name, "age": age}
