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


# # """
import random
import string
from fastapi import FastAPI

from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import sqlite3

app = FastAPI()


# url_mapping = {}
# Connect to the SQLite database
conn = sqlite3.connect("url_mapping.db")
cursor = conn.cursor()


# Create a table to store the URL mapping
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS url_mapping (
        short_url TEXT PRIMARY KEY,
        long_url TEXT
    )
"""
)

conn.commit()


class url(BaseModel):
    url: str


def generate_random_string(length=5):
    string = ""
    # characters to make random string
    # characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # use random.choice to select random characters and join them to create string
    for i in range(length):
        random_string = random.choice(characters)
        string = string + random_string
    # print(string)
    return string

    #  Check if it already exists in the database
    def check_randomID():
        cursor.execute(
            "SELECT COUNT(*) FROM url_mapping WHERE short_url = ?", (string,)
        )
        count = cursor.fetchone()[0]
        if count == 0:
            return short_url


@app.post("/bit.ly")
async def get_redirect(url: url):
    # generate short url
    short_url = generate_random_string(length=5)
    # store in database
    cursor.execute(
        "INSERT INTO url_mapping (short_url, long_url) VALUES (?, ?)",
        (short_url, url.url),
    )
    conn.commit()
    return {"short_url": short_url}


@app.get("/{urlID}")
async def redirect_short_url(urlID: str):
    # Query database for the long URL
    cursor.execute("SELECT long_url FROM url_mapping WHERE short_url = ?", (urlID,))
    result = cursor.fetchone()
    if result:
        long_url = result[0]
        return RedirectResponse(long_url)
    else:
        return {"error": "Short URL not found"}
