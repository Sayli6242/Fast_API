from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/order/")
async def place_order(preferred_cuisine: str = Cookie(None)):
    if preferred_cuisine:
        return {"message": f"Order placed for {preferred_cuisine} cuisine"}
    else:
        return {"message": "Order placed"}
