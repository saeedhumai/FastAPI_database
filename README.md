

Here's the complete README.md file:

```markdown:README.md
# FastAPI Todo App

A simple Todo API built with FastAPI and SQLAlchemy.

## Project Structure

```
├── main.py          # API routes and FastAPI app
├── database.py      # Database configuration
├── models.py        # Todo database model
├── requirements.txt # Project dependencies
├── .gitignore      # Git ignore file
└── todo.db         # SQLite database
```

## Setup & Run

1. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run server**
```bash
uvicorn main:app --reload
```

## Code Breakdown

### database.py
- Sets up SQLAlchemy connection
- Creates database session
- Configures SQLite database

### models.py
- Defines Todo database model
- Sets up table structure
- Handles database schema

### main.py
- Contains FastAPI application
- Defines API routes
- Handles database sessions
- Implements dependency injection

## API Documentation

Server runs at: http://127.0.0.1:8000

Available endpoints:
- `GET /` - List all todos

Interactive API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Dependencies

Main packages:
- FastAPI (v0.115.6)
- SQLAlchemy (v2.0.36)
- Uvicorn (v0.34.0)
- Pydantic (v2.10.4)

Full dependencies list in `requirements.txt`
```
