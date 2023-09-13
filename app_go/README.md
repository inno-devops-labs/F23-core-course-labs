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