# from fastapi import FastAPI, Response
# from fastapi.responses import JSONResponse, RedirectResponse

# app = FastAPI()


# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

"""
# task : short url -> long url 
register url steps
1) get user long url from request body of postAPI
2) generate short url uniqueID
    - (random character)
3) store long url and short url into database.
4) return short url

fetch url and redirect steps
1) fetch long url using short url
2) redirect the user to long url


"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


url_mapping = {}


class url(BaseModel):
    url: str


@app.post("/bit.ly")
async def get_redirect(url: url):
    # generate short url
    short_url = "abs"
    # store in database
    return short_url


@app.get("/bit.ly/{urlID}")
async def redirect_short_url(url: url):
    # fetch long url using short url
    long_url = url_mapping.get(short_url)
    # redirect to long url
    return {"redirect_url": long_url}
