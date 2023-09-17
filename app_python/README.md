# Innopolis University DevOps [F23] | Lab1

## Overview
The service provides information about current time in Europe/Moscow timezone.

## Build
### Building application on host machine
To build the project you should have Python3 executable.
Install dependencies go to `./app_python` directory and run the following commands:
```shell
python3 -m venv env
source env/bin/activate
pip3 install --no-cache-dir -r requirements-dev.txt
pre-commit install
```
### Building application Docker image
To build the application Docker image go to the `./app_python` directory and run the following command:
```shell
docker build --tag iskanred/app_python:1.0.0 .
```

## How to test?
In latest version of the project there are 3 properly documented tests.
To run tests go to the `./app_python` directory and run the following command:
```shell
pytest
```

## How to run?
### GitHub repository.
1. Clone this repo.
2. Go to the `./app_python` directory of the cloned repo.
3. Run the following command:
    ```shell
    python3 src/app.py
    ```
4. Now the service can be used
### Docker
1. Pull the image from Docker Hub (you can skip this step if you already have the image):
    ```shell
    docker pull iskanred/app_python:1.0.0
    ```
2. Run a container based on this image:
    ```shell
    docker run -p 8080:8080 --name app_python iskanred/app_python:1.0.0
    ```
3. Now the service can be used


## Usage
The server's URL is `http://127.0.0.1:8080/`.
Obtain the page from the browser or make a GET request from any HTTP client.
The resulting response is a text string with current Moscow time.

## Contact
* Author: Iskander Nafikov
* E-mail: i.nafikov@innopolis.university
