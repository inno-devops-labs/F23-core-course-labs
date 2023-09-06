# python_time

Simple Python web application that displays the current time in Moscow.

- **Framework**: FastAPI
- **Testing**: pytest
- **Code style**: autoflake, isort and black

## Running

1. Make sure you have at least python3.8 installed.
   You can create new virtual environment if you want

   ```shell
   python -m venv /path/to/new/virtual/environment
   source /path/to/new/virtual/environment/bin/activate
   ```

1. Install python packages

   ```shell
   cd app_python
   pip install -r ./requirements/base.txt
   # Optional
   pip install -r ./requirements/dev.txt
   ```

1. Run

   ```shell
   uvicorn src.main:app
   ```

## Docker

You can use Docker to run the application.

1. `make build` to build Docker image
1. `make run` to run Docker image locally on port 8000
1. `make push` to push Docker image to Docker Hub
