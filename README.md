# FastAPI Application

A modern, fast (high-performance) web API built with FastAPI, SQLAlchemy, and SQLite.

## Features

- Async SQLite database with SQLAlchemy 2.0
- Pydantic v2 for data validation
- Modern Python with type hints
- CORS middleware configured
- Structured project layout
- RESTful API endpoints
- Database migrations with Alembic
- Comprehensive error handling
- Input validation with Pydantic

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
alembic upgrade head
```

## Running the Application

Start the server with:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## Database Migrations

To create a new migration:
```bash
alembic revision --autogenerate -m "description of changes"
```

To apply migrations:
```bash
alembic upgrade head
```

To rollback migrations:
```bash
alembic downgrade -1  # Rollback one migration
alembic downgrade base  # Rollback all migrations
```

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /`: Welcome message
- `GET /items/`: List all items
- `POST /items/`: Create a new item
- `GET /items/{item_id}`: Get a specific item
- `PUT /items/{item_id}`: Update an item
- `DELETE /items/{item_id}`: Delete an item

## Project Structure

```
.
├── alembic/             # Database migrations
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── main.py              # FastAPI application instance and configuration
├── database.py          # Database configuration and session management
├── requirements.txt     # Project dependencies
├── models/             # SQLAlchemy models
│   └── item.py
├── schemas/            # Pydantic models for request/response
│   └── item.py
└── routers/            # API routes
    └── item.py
```

## Error Handling

The API includes comprehensive error handling:
- 404: Resource not found
- 422: Validation error (invalid input)
- 500: Internal server error

All errors return a consistent JSON response with error details.
