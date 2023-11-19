# Moscow Time Web App

## Table of contents

- [Description](#description)
- [Pre-requirements](#pre-requirements)
- [Build](#build)
- [Pull](#pull)
- [Run](#run)
- [Project repository](#project-repository)
- [CI Workflow](#ci-workflow)
- [Unit Tests](#unit-tests)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creator](#creator)
- [Copyright and license](#copyright-and-license)

## Description

Simple web app to show time at Moscow timezone. This app was created for course of DevOps engineering in Innopolis University.

Moreover, you can mount your volume folder to `/volume/` folder inside container. Now app uses this folder to save visits inside `visits` file. `/visits` endpoint returns this number.

## Pre-requirements

- Docker

## Build

To build docker container use the following command:

`docker build -t moscow-time-flask-app .`

## Pull

It is possible to pull the container from docker hub. To do is use the following command:

`docker pull nabiull2020/moscow-time-flask-app:latest`

## Run

To run the container use the following command:

`docker run -p 8000:8000 nabiull2020/moscow-time-flask-app:latest`

or if you built it manually:

`docker run -p 8000:8000 moscow-time-flask-app`

The application will then be accessible at http://localhost:8000/

## Project repository

```text
app_python/
├── app.py
├── PYTHON.md
├── README.md
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── tests/
    └── app_tests.py
```

## CI Workflow

Jobs:

1. **Build**

    - Python Setup - setup python 3.11

    - Cache dependencies - use cache to store dependencies

    - Dependencies install

    - Vulnerability check - using Snyk to check for vulnerabilities

    - Vulnerability report - generate report of vulnerabilities

    - Linter

    - Tests

2. **Docker**

    - Login - login to docker hub

    - Build and Push - build docker image and push it to docker hub

I used Snyk in build stage in case to reduce dependencies installations.

## Unit Tests

You can find unit tests in `tests` folder.

Run test using:

`python -m unittest discover -s tests -p '*_tests.py'`

## Bugs and feature requests

Not found yet ;)

## Contributing

Not available at this moment

## Creator

<https://github.com/DamirNabiull>

## Copyright and license

Code and documentation copyright 2023 the authors.