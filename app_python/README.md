# Lab 1 – Web application

Simple FastAPI web app that displays current time in Moscow

## Structure

Following the guidelines recommended by FastAPI documentation:

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── schemas
│   │   ├── __init__.py
│   │   └── items.py
│   └── static
```

## Installation

```bash
pip3 install -r requirements.txt
```

## Running

```bash
# in parent directory
uvicorn --reload app_python.main:app
```

## Linters

```bash
# in app_python directory
pylint *.py
```
