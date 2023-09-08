# Moscow Time Web App

## Table of contents

- [Description](#description)
- [Pre-requirements](#pre-requirements)
- [Build](#build)
- [Pull](#pull)
- [Run](#run)
- [Project repository](#project-repository)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creator](#creator)
- [Copyright and license](#copyright-and-license)

## Description

Simple web app to show time at Moscow timezone. This app was created for course of DevOps engineering in Innopolis University.

## Pre-requirements

- Docker

## Build

To build docker container use the following command:

`docker build -t moscow-time-flask-app .`

## Pull

It is possible to pull the container from docker hub. To do is use the following command:

`docker pull nabiull2020/moscow-time-flask-app:1.0.0`

## Run

To run the container use the following command:

`docker run -p 8000:8000 nabiull2020/moscow-time-flask-app:1.0.0`

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

## Bugs and feature requests

Not found yet ;)

## Contributing

Not available at this moment

## Creator

<https://github.com/DamirNabiull>

## Copyright and license

Code and documentation copyright 2023 the authors.