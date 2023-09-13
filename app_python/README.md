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

