from fastapi import FastAPI

app = FastAPI()


# @app.get("/items/")
# async def read_item(item_id: int, category: str = None):
#     response = {"item_id": item_id}
#     if category:
#         response["category"] = category
#     return response


# @app.get("/search_employees")
# def search_employee(name, age):
#     return {"name": name, "age": age}


weather_info = {
    "LA": {"temprature": 36, "condition": "Sunny"},
    "CALINFORNIA": {"temprature": 29, "condition": "mostly cloudy"},
    "VEGAS": {"tempreature": 40, "condition": "partly cloudy"},
    "SanFrancisco": {"temprature": 13, "condition": "snowy"},
}


@app.get("/weather/")
def weather_app(city: str):
    city = "LA"
    for i in weather_info:
        if city in weather_info:
            return weather_info[city]
        else:
            return {"city not found"}
