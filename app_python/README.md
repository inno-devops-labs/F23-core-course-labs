# Clock web application.

This web application displays current time in moscow timezone (UTC+3) and uses FastApi, known for its simplicity and performance.

/visits
shows the number of times this website has been visited.

## Docker

This application can be run as a Docker container for easy deployment. 

To build the Docker image, follow these steps:

1. Make sure you have Docker installed on your machine.

2. Clone this repository to your local machine:

3. Build the Docker image:
    ```
        docker build -t clock:latest ./app_python
    ```

* To pull the pre-built Docker image from a container registry:

    ```
        docker pull xyz/clock:latest
    ```

* To run the Docker container:

    ```
        docker run -p 8000:8000 clock:latest
    ```

Unit tests

* To run unit tests
    ```
        pytest unit_tests.py
    ```
Github workflow
    
[![CI](https://github.com/PATH242/core-course-labs/actions/workflows/main.yml/badge.svg)](https://github.com/PATH242/core-course-labs/actions/workflows/main.yml)

## Docker compose
For storage volume.