# Moscow Time Display Web App

This is a simple Flask web application that displays the current Moscow time.
The application updates the time every second without requiring a page refresh.


## Table of Contents

- [Moscow Time Display Web App](#moscow-time-display-web-app)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Docker](#docker)
    - [Dockers Installation] (#dockers-installation)
    - [Dockers SetUp](#dockers-setup)
    - [Dockers Run Application](#dockers-run-application)
  - [Local Machine](#local-machine)
    - [Prerequisites](#prerequisites)
    - [Install Dependencies](#install-dependencies)
    - [Run Python Script](#run-python-script)
    - [Python Unit Tests](#python-unit-tests)

## Features

- Displays the current Moscow time.
- Updates the time every second using JavaScript.
- Use tools for dependencies or at least `requirements.txt` file for Python packages.
- Work with docker
- Use `.gitignore` file to exclude not relevant files from the git.
- Can save address and time for every connection in file `visits.txt`

## Getting Started

It's instructions will help you to run python web application on docker or in your local machine.

## Docker
### Dockers Installation
You easy can install docker image from docker-hub

```sh
docker pull stiveman1/app_python
```


### Dockers SetUp

First of all you might have `docker` in your local machine and `docker-buildx` for build images.

To set up docker we have file `Dockerfile` so we just need to be in same dir with this file and run simple command:

```sh
docker build -t 'image-name' .
```

Also you can create docker image using `docker-compose.yml` and get image with tag `stiveman1/app_python:v2` with command:

```sh
docker-compose build
```



### Dockers Run Application

To run the built docker image we just run simple command in terminal:

```sh
docker run 'image-name'
```

And us result we will get some data 

```text
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
```

First address is address inside docker container, and the second one is that's one with we can you to open in our browser.

## Local Machine
### Prerequisites

- Python (3.6 or higher)
- Poetry (`pip install --upgrade pip poetry==1.1.11`)

### Install Dependencies

To Install dependencies use poetry command:

```sh 
poetry config virtualenvs.create false
poetry install --no-dev
```
   
### Run Python Script

Run the flask application:
   
```sh
flask run --host 0.0.0.0 --port 8000
```
The access from browser at address: http://127.0.0.1:8000/

### Python Unit Tests

To run tests use this simple command

```sh
python -m unittest tests.py
```
