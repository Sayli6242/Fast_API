import fastapi

app = fastapi.FastAPI()


@app.get("/hello/{name}")
async def root():
    return {"message": "Hello World"}
