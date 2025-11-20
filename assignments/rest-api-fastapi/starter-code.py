# FastAPI Book Management API - Starter Code
# Install required packages: pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Create FastAPI app instance
app = FastAPI()

# TODO: Define your Book model here using Pydantic BaseModel
# Include fields: id (int), title (str), author (str), year (int), genre (str)


# In-memory storage for books
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
]

# TODO: Implement your endpoints below

# Task 1: Basic endpoints
@app.get("/")
def root():
    # TODO: Return a welcome message
    pass

@app.get("/about")
def about():
    # TODO: Return API information
    pass


# Task 2: CRUD endpoints
# TODO: GET /books - Get all books


# TODO: GET /books/{book_id} - Get a specific book


# TODO: POST /books - Create a new book


# TODO: PUT /books/{book_id} - Update a book


# TODO: DELETE /books/{book_id} - Delete a book


# Task 3: Filtering and pagination
# TODO: Add query parameters to GET /books for filtering by author, genre, year
# TODO: Add pagination with skip and limit parameters


# Run the application:
# uvicorn starter-code:app --reload --port 8000
# Then visit: http://localhost:8000/docs
