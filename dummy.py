from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id, "name": "John"}


# @app.put("/users/{user_id}")
# def update_user(user_id: int, updated_user_data: dict):
#     return {"message": f"User with ID {user_id} updated successfully"}


# @app.post("/users/")
# def create_user(user_data: dict):
#     return {"message": "User created successfully"}


# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     # Code to delete user based on user_id
#     return {"message": f"User with ID {user_id} deleted successfully"}


# Sample book data for demonstration purposes
books = [
    {"id": 1, "title": "Book 1", "genre": "Fiction"},
    {"id": 2, "title": "Book 2", "genre": "Fantasy"},
    {"id": 3, "title": "Book 3", "genre": "Fiction"},
]


# get request with query params
@app.get("/books/")
async def get_books_by_genre(genre: str = Query(None)) -> List[dict]:
    filtered_books = []
    if genre:
        for book in books:
            if book["genre"] == genre:
                filtered_books.append(book)
    else:
        filtered_books = books
    return filtered_books


# get request with path params
@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}
