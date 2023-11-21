![Python CI](https://github.com/MaximInnopolis/devops-labs/workflows/Python%20CI/badge.svg)

# Python Web Application: Display Moscow Time

## Overview

This Python web application is a simple utility that displays the current time in Moscow. It utilizes the Flask framework for web development and Jinja2 templating for rendering the Moscow time on an HTML page.

## Features

- Display the current time in Moscow in the format: YYYY-MM-DD HH:MM:SS.
- Minimalist and user-friendly web interface.
- Automatic time update upon page refresh.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Python (3.x recommended)
- Flask framework (install via `pip install Flask`)

## Containerized Application

The application is containerized using Docker, allowing for easy deployment and isolation.

### How to Build the Docker Image

To build the Docker image for application, follow these steps:

```bash
docker build -t my-flask-app .
```

### How to Pull the Docker Image (Optional)

If you prefer not to build the image locally, you can pull it from Docker Hub:

```bash
docker pull madfisher/my-flask-app
```

### How to Run the Docker Container

This command fetches the pre-built Docker image from the Docker Hub repository:

```bash
docker run -p 80:80 madfisher/my-flask-app
```
or if you want to fetch locally built Docker image:
```bash
docker run -p 80:80 my-flask-app
```

This command starts a container based on the my-flask-app image, mapping port 80 on your host system to port 80 inside the container.

Access the application in your web browser at http://localhost:80.

## Unit Tests

The Python web application includes a suite of unit tests to ensure its functionality and correctness. These unit tests are implemented using Python's `unittest` framework and cover various aspects of the application's behavior.

### Running Unit Tests

To run the unit tests locally, follow these steps:

1. Ensure you have Python (3.x recommended) and the Flask framework installed.

2. Navigate to the project directory.

3. Run the following command to execute the unit tests:

   ```bash
   python -m unittest test_app
   
## Continuous Integration (CI) Workflow

This project uses GitHub Actions for continuous integration (CI). The CI workflow performs the following tasks:

- Installs project dependencies.
- Lints the code using Pylint.
- Runs unit tests.
- Builds and pushes a Docker image to Docker Hub.

To trigger the CI workflow manually, follow these steps:

1. Make sure you have pushed your changes to a branch (e.g., `main`).
2. Check the "Actions" tab in the repository on GitHub for the CI workflow runs.

## Endpoints description

### Endpoint: /
* Description: This endpoint increments a counter each time it is called and returns the current time in Moscow. It also writes the current counter value to a file named 'visits'.
* HTTP Method: GET
* Response: A string containing the current time in Moscow and the number of times the endpoint has been called.


### Endpoint: /visits
* Description: This endpoint returns the current counter value. The counter is incremented each time the root endpoint (/) is called.
* HTTP Method: GET
* Response: A string containing the current counter value.