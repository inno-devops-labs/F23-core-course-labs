# Python web application

## Overview

This is a simple python web application that shows the current time in Moscow timezone.

## Docker

You can run this application in docker container.

Build image inside app_python directory:

```bash
docker build -t rakavaqaflow/app-python:v1 .
```

Or

Pull image from DockerHub:
```bash
docker pull rakavaqaflow/app-python:v1
```

And run docker image:

```bash
docker run -p 5000:5000 rakavaqaflow/app-python:v1
```


## Requirements

To run the application, you need a python version of at least 3.12. [How to install Python](https://www.tutorialspoint.com/how-to-install-python-in-windows)

You can install all the necessary dependencies for correct operation by running the command:

```bash
pip install -r requirements.txt
```

## Run

To run app you need run the command inside app_python folder:
```bash
python main.py
```

To check app with linter run the command inside app_python folder:

```bash
flake8 *.py
```

## Usage

To see the result of the work, open a browser and go to http://localhost:5000/ - you will see current time in Moscow timezone

Routes:

```
/        -- get current time
/visits  -- number of time root path accessed

```

## Unit Tests

You can check application by testing, to do this, run in terminal command:

```bash
python -m pytest
```

## CI

    Workflow:

- Security check
- Lint, Build and Run tests
- Release: Dockerhub image push

## Contact

email: v.khalilov@innopolis.university
tg: @vaqaaa 