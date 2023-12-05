![Go CI](https://github.com/MaximInnopolis/devops-labs/workflows/Go%20CI/badge.svg)
# Go Web Application: Display Moscow Time

## Overview

This Go web application is a simple utility that displays the current time in Moscow. It serves a web page that shows the time in the format: YYYY-MM-DD HH:MM:SS.

## Features

- Display the current time in Moscow in the format: YYYY-MM-DD HH:MM:SS.
- Minimalist and user-friendly web interface.
- Automatic time update upon page refresh.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Go (1.17 recommended)

## Containerized Application

The application is containerized using Docker, allowing for easy deployment and isolation.

### How to Build the Docker Image

To build the Docker image for the application, follow these steps:

```bash
docker build -t my-go-app .
```

### How to Pull the Docker Image (Optional)

If you prefer not to build the image locally, you can pull it from Docker Hub:

```bash
docker pull madfisher/my-go-app
```

### How to Run the Docker Container

This command fetches the pre-built Docker image from the Docker Hub repository:

```bash
docker run -p 8080:8080 madfisher/my-go-app
```
or if you want to fetch locally built Docker image:
```bash
docker run -p 8080:8080 my-go-app
```

This command starts a container based on the my-flask-app image, mapping port 80 on your host system to port 80 inside the container.

Access the application in your web browser at http://localhost:8080.

## Unit Tests

This project includes comprehensive unit tests to ensure the correctness of the code. The unit tests cover different aspects of the application, including HTTP request handling and response validation. Here's how to run the unit tests:

```bash
go test
```

## Continuous Integration (CI)

This project is configured with GitHub Actions for Continuous Integration (CI). The CI workflow includes the following steps:

1. **Dependencies:** Go dependencies are downloaded using `go mod download`.
2. **Linter:** Code is checked for common mistakes and style issues using `go vet`.
3. **Unit Tests:** Unit tests are run to ensure the correctness of the code.
4. **Docker Build & Push:** A Docker image of the application is built and pushed to Docker Hub.

The CI workflow is automatically triggered on pushes to the `app_go` directory or changes to the workflow file (`app_go.yml`). It helps maintain code quality and ensures that the application runs smoothly.

## Endpoints description

### Endpoint: /
* Description: This endpoint increments a counter each time it is called and returns the current time in Moscow. It also writes the current counter value to a file named 'visits'.
* HTTP Method: GET
* Response: A string containing the current time in Moscow and the number of times the endpoint has been called.


### Endpoint: /visits
* Description: This endpoint returns the current counter value. The counter is incremented each time the root endpoint (/) is called.
* HTTP Method: GET
* Response: A string containing the current counter value.