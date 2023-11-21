# Python Web Application

This is a simple web application developed using Python and the Flask framework. The application displays the current time in Moscow and serves as an example of web development using best practices.

Also `/visits` shows the number of visits

## Features

- Displays the current time in Moscow.
- Built using Flask, a lightweight Python web framework.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the `app_python` folder.

### Prerequisites

- Python 3.9 installed.

## Running the Application

To run the application locally without Docker, you can use the following command:

`python app.py`

### Dockerized Version

#### Build

To build the Docker container for this application, use the following command:

`docker build -t dshamik_msk_time .`

#### Pull

Alternatively, you can pull the container from Docker Hub using the following command:

`docker pull dshamik/moscow-time-flask-app:0.0.1`

#### Run

To run the Docker container, use the following command:

`docker run -p 8090:8090 dshamik/moscow-time-flask-app:0.0.1`


The application will be accessible at [http://localhost:8090/](http://localhost:8090/).

## Unit Tests

Unit tests locaten in `tests` folder.

To run test:

`python -m unittest discover -s tests -p 'tests.py'`

## CI Workflow

**Build**

- Python Setup

- Cache dependencies

- Dependencies install

- Vulnerability check

- Vulnerability report

- Linter

- Tests

**Docker**

- Login

- Build and Push

