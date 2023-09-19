[![Python CI](https://github.com/Q-Tify/core-course-labs-devops/actions/workflows/python-ci.yml/badge.svg?branch=lab3)](https://github.com/Q-Tify/core-course-labs-devops/actions/workflows/python-ci.yml)

# Python Web Application Project: Moscow Time Display

## Description

This project aims to develop a Python web application that displays the current time in Moscow. The application will provide users with an interface to view the current date and time in Moscow, which can be particularly useful for users in different time zones or anyone interested in real-time information.

## Table of Contents

- [Project Name](#project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [License](#license)
  - [Author](#author)

## Installation

Provide instructions on how to install and set up your Python web project. Include any prerequisites and steps needed to get the project up and running. You can use code blocks to show commands.

```bash
# Clone the repository
git clone https://github.com/Q-Tify/core-course-labs-devops.git

# Change to the project directory
cd core-course-labs-devops
cd app_python

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On macOS and Linux:
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# To run use:
flask run

# Don't forget to export variables:
export FLASK_APP=application.app
export FLASK_ENV=development

# Also there is a pre-commit option:
pre-commit install
pre-commit run --all-files

```

## Usage
Upon accessing the application in your web browser, you will see the current date and time in Moscow displayed on the homepage.

## Features
- Display the current date and time in Moscow.
- User-friendly web interface.
- Responsive design for various devices.
- Easy-to-understand and clean user interface.

## Technologies Used
- Python: The core programming language used for the backend development.
- Flask: A lightweight and flexible web framework for building web applications in Python.
- HTML/CSS: Frontend design and structure using HTML and CSS.
- Datetime Module: Python's datetime module for handling date and time-related operations.
- Docker: Containerization technology used to package and deploy the application in a consistent and isolated environment, ensuring portability and ease of deployment across various platforms and environments.

## Project Structure

The project structure is organized as follows:
- application/: Directory for the application.
- init.py: The starting application file.
- app.py: The main Python file for setting up the Flask application.
- routes.py: The main Python file for setting up the Flask routes.
- static/: Directory for static assets (CSS, images, etc.).
- templates/: Directory containing HTML templates.
- index.html: The HTML template for displaying the current time in Moscow.
- tests/: Directory for tests.
- venv/: Directory for virtual environment.
.gitignore: File which tells git which files to ignore.
- config.py: Configuration file for the Flask application.
- README.md: Project documentation file.
- PYTHON.md: Best practices documentation file.
- requirements.txt: List of Python packages required for the project.
- .dockerignore: File specifying which files and directories should be ignored when creating a Docker image, ensuring only necessary files are included.
- Dockerfile: The Dockerfile that defines how the Docker image for the application should be built.
- Docker.md: Documentation file providing instructions and best practices for using Docker in the project.

## License
This project is licensed under the MIT License.

## Author
Arseniy Rubtsov

<br>

# Docker section
This project includes a Dockerfile that allows you to containerize the Python.
## This particular case
```
git clone https://github.com/Q-Tify/core-course-labs-devops/tree/lab2
cd app_python
docker build -t arseniy5443/moscowtime:latest .
docker run -p 80:5000 --rm arseniy5443/moscowtime:latest

docker login
docker push arseniy5443/moscowtime:latest

docker pull arseniy5443/moscowtime
```

## How to build docker image?
```
docker build -t [image name]:[image tag] [path to dockerfile]
```

## How to run docker container?
```
docker run -p [local port]:[docker port] --rm [image name]:[image tag]

docker run -d -p [local port]:[docker port] --rm --name [container name] [image name]:[image tag]

docker start [container name]
docker stop [container name]
```

Possible to add ENV:
```
docker run -p [local port]:[docker port] -e PORT=80 [image name]:[image tag]
```
Or to take it from file, create dir config and there .env file, put there all variables and use command:
```
docker run -p [local port]:[docker port] --env-file ./config/.env [image name]:[image tag]
```

## How to upload to docker hub?

```
docker login
```
It is important that the name of the image should contain docker username + / + image name:
```
docker push [docker username]/[image name]:[image tag]
```

To rename image:
```
docker tag [old image] [docker username]/[new image]
```

## How to download image from docker hub?
```
docker pull [image name]
```

<br><br>

## How to delete all stopped containers?
```
docker container prune
```

## How to delete all images?
```
docker image prune -a
```

## How to see all containers?
```
docker ps -a
```

## How to see all images?
```
docker images
```

## How to delete:
- all stopped containers
- all networks not used by at least one container
- all dangling images
- all dangling build cache
```
docker system prune
```

<br>

# Unit Tests
To run the tests for this application you can use precommit, with linting the app will be tested:
```
pre-commit install
pre-commit run --all-files
```
Or you can run test separately with command:
```
flask test
```

<br>

# CI Workflow

### Overview

This project uses GitHub Actions for Continuous Integration (CI) to automate various tasks such as code linting, testing, and building Docker images. The CI workflow ensures that the project maintains code quality and is always ready for deployment.

### Workflow Details

The CI workflow is defined in the [.github/workflows/python-ci.yml](.github/workflows/python-ci.yml) file. It is triggered automatically on every push or pull to the `app_python` directory or changes to the workflow file itself.

Here's what the workflow does:

1. **Python Build Job**
   - It runs on an Ubuntu-based environment.
   - Sets up Python 3.10.
   - Installs project dependencies from `requirements.txt`.
   - Performs linting using Flake8 and Black.
   - Executes Python unit tests with pytest.

2. **Docker Job**
   - It runs on Ubuntu as well and depends on the Python Build Job.
   - Logs in to Docker Hub using Docker secrets for secure access.
   - Sets up Docker Buildx for multi-platform image building.
   - Builds a Docker image using the `Dockerfile` in the `app_python` directory.
   - Pushes the built Docker image to Docker Hub.
