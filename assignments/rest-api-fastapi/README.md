# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn how to build a RESTful API using FastAPI, a modern, fast web framework for building APIs with Python. You'll create endpoints for managing a collection of books, implement CRUD operations, and learn about request/response models.

## 📝 Tasks

### 🛠️	Task 1: Create a Basic FastAPI Application

#### Description
Set up a basic FastAPI application with a root endpoint and a simple GET endpoint that returns information about your API.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Create a root endpoint (`/`) that returns a welcome message
- Create an `/about` endpoint that returns information about your API (name, version, description)
- Run the application using Uvicorn server on port 8000


### 🛠️	Task 2: Implement Book Management Endpoints

#### Description
Create a RESTful API for managing a book collection. Implement endpoints to create, read, update, and delete books from an in-memory data store.

#### Requirements
Completed program should:

- Define a `Book` model using Pydantic with fields: id, title, author, year, and genre
- Implement a GET endpoint `/books` to retrieve all books
- Implement a GET endpoint `/books/{book_id}` to retrieve a specific book by ID
- Implement a POST endpoint `/books` to add a new book to the collection
- Implement a PUT endpoint `/books/{book_id}` to update an existing book
- Implement a DELETE endpoint `/books/{book_id}` to remove a book from the collection
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include proper error handling for cases like "book not found"


### 🛠️	Task 3: Add Query Parameters and Filtering

#### Description
Enhance your API by adding query parameters to filter books by different criteria and implement data validation.

#### Requirements
Completed program should:

- Add query parameters to the `/books` endpoint to filter by author, genre, or year
- Implement validation for the year field (must be between 1000 and current year)
- Add pagination support with `skip` and `limit` query parameters
- Return meaningful error messages for invalid requests
- Test all endpoints using FastAPI's automatic interactive documentation at `/docs`
