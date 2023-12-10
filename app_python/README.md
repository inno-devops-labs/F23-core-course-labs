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

## Docker

### Use prebuild image:

```bash
docker run -v ./persistence:/persistence amoriodi/app_python:latest
```

### Build manually:

```bash
# building
docker build . -t <username>/app_python:latest

# pushing
docker push <username>/app_python:latest
```

## Unit tests

Units uses `pytest` and `unittest.mock` for ensuring critical routes of our app

```bash
pytest -v
```
