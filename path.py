# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

from fastapi import FastAPI

app = FastAPI()

# Sample product data (for demonstration purposes)
products_data = {
    1: {"name": "Widget", "price": 9.99},
    2: {"name": "Gadget", "price": 19.99},
    3: {"name": "things", "price": 20.00},
    4: {"name": "gadget", "price": 82.00},
}


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    if product_id in products_data:
        return products_data[product_id]
    else:
        return {"message": "Product not found"}
