# App_python

![python-app workflow badge](https://github.com/yesliesnayder/devops-course-labs/actions/workflows/python_ci.yml/badge.svg)

This is application to show current time in specified region (timezone).
Initially, it shows Moscow time.

Also, it shows how many times it was accessed. You can check it on `/visits` endpoint.

## How to run

### Virtual environment

1. Install `Python` at least version 3.11:

    ```shell
    apt install python:3.11
   ```

1. Create virtual environment. It will generate new folder with your virtual environment:

    ```shell
    python3 -m venv /path/to/your/environment
   source /path/to/your/environment/bin/activate
   ```

1. Install dependencies:

    ```shell
   pip install -r ./requirements/dev.txt
   ```

1. Run the application. To run it you must be in project folder (in *devops-course-labs*):

    ```shell
   cd ..
   python -m uvicorn app_python.src.main:app --reload
   ```

### Docker

1. To run the application you should have docker image. You can obtain it by 2 ways:
   - From DockerHub:
   ```shell
   docker pull yesliesnayder/app_python:1.0.0
   ```
   
   - Build from Dockerfile:
   ```shell
   docker build -t app_python --no-cache  .
   ```

1. Run the docker image:

   ```shell
   docker run -p 8000:8000 app_python
   ```

1. Access the application at `localhost:8000`. If you have problems with connection
(reset by peer), then try launch docker image with the following
command: `docker run --network host -p 8000:8000 app_python`

## Unit Tests

1. To run tests make sure you installed dependencies:

    ```shell
    pip install -r ./requirements/dev.txt
    ```

1. Run tests. You can run the following command either in *app_python* or in *app_python/tests* folder:

    ```shell
    pytest
    ```

## CI
CI workflow is on *python_ci.yml* contains:

- Linter step that uses `pylint`
- Unit Tests that uses `pytest` to check correctness of the application
- Snyk vulnerability check
- Deploy that logins to DockerHub, build the project and push it to DockerHub