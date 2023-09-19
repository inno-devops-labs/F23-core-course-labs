# Moscow Time Display Web App

This is a simple Flask web application that displays the current Moscow time. The application updates the time every second without requiring a page refresh.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Linting](#lint)
- [Docker](#docker)

## Features

- Displays the current Moscow time.
- Updates the time every second using JavaScript.

## Getting Started

These instructions will help you set up and run the project on your local machine.

## Prerequisites

- Python (3.6 or higher)
- Flask (`pip install flask`)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/PlutoEx/DevOps-course-labs.git
   cd app_python

2. Install dependencies:

   ```sh 
   pip install -r requirements.txt
   
## Usage

1. Run the flask app:
   
   ```sh
   python -m venv .venv
   .venv/Scripts/Activate
   flask run

2. Enter the app in browser at: http://127.0.0.1:5000/

## Tests

* I add some tests to check moscow time, using **pytest** library

* To run it:

   ```sh
  pytest tests.py
  
## Lint

* I add flake8 lint to locate grammatical and styling errors

* To run it:

    ```shell
  flake8

## Docker

* Build dockerfile:

    ```shell
    docker build -t app_python:latest .

 that build docker images with name 'app_python' and tag 'latest'


* Then check image with
    ```shell
    docker images

* Run it:
    ```shell
    docker run -it --rm app_python:latest
  
-it: Enables interactive mode for seeing output and interacting with the container.

--rm: Automatically removes the container when it exits.
  

* If everything OK, push it into Docker Hub, authorize first
    ```shell
    docker login -u <username>
    <password>
    docker tag app_python:latest <username>/app_python:v1
    docker push <username>/app_python:v1

* To get image from Docker Hub
    ```shell
    docker pull <username>/app_python:v1
  
* And run it:
    ```shell
    docker run -it --rm <username>/app_python:v1

## Continuous Integration (CI) with GitHub Actions

This project uses GitHub Actions for continuous integration (CI). The CI workflow includes the following steps:

- **Dependencies**: Install project dependencies.
- **Linting**: Run linting to check code quality.
- **Tests**: Execute tests to ensure code correctness.
- **Docker Build & Push**: Build a Docker image and push it to Docker Hub.

### How to Run CI Workflow

The CI workflow runs automatically on every push to the repository. You can also trigger it manually if needed.

### Docker Hub Image

The Docker image built during CI is available on Docker Hub at:

- Image: `expluto/app_python:latest`

You can pull and run the Docker image using standard Docker commands.

#### How to Build Locally:

1. Clone this repository.
2. Build the Docker image:

   ```bash
   docker build -t app_python:latest .