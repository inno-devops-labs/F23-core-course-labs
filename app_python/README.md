![app_python](https://github.com/DaniilOkrug/dev-ops-inno/workflows/Python%20CI/badge.svg)

# Python Web Application Development

Author: Daniil Okrug

## Overview

The application displays Moscow time. In this project I used Flask framework because of its convenience and simplicity in web application development.

## Structure

The main file is app.py which contains routes '/' and '/time'. First route renders index.html page with Moscow time. Second route provides time in Moscow timezone.

The project has a templates folder that contains HTML pages to render on the client side.

## Docker

The project uses Docker with two build stages. The first stage is build, where the main files needed for startup are copied. The second stage is needed for startup and this is where files with limited user rights are copied.

### Build

Local image building: \
`docker build -t app_python:lab2 .` \
`app_python:lab2` - can be any name you like for the image

### Docker Hub

Pull image from Docker Hub \
`docker pull bellissimo/devops-inno-daniil-okrug:lab2`

### Run

Running localy builded image: \
`docker run -d -p 5000:5000 app_python:lab2`

Running image from Docker Hub: \
`docker run -d -p 5000:5000 bellissimo/devops-inno-daniil-okrug:lab2`

## Unit tests

The tests are written using the pytest library and are located in the /tests folder.

Running tests: \
`python -m pytest` \
or \
`pytest`

For determining the percentage of test coverage pytest-cov is used.

Checking coverage: \
`python -m pytest --cov` \
or \
`pytest --cov`

## CI

CI consists of steps such as:

- Set up Python - preparing the environment with Python
- Install dependencies - install all necessary dependencies
- Linter - testing the linter code
- Tests - test with tests
- Login to Docker Hub - login to Docker Hub (secrets are used) for further uploading Docker image there.
- Build and push - docker image build and push to Docker Hub

The CI file is located at .github/worflows/python.ci
