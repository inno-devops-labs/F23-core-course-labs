# Moscow Time Web App

A simple Flask web app that displays the current time in Moscow without using HTML templates.

## Table of Contents

- [Moscow Time Web App](#moscow-time-web-app)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
  - [App Description](#app-description)
  - [Docker](#docker)
    - [Delete your container](#delete-your-container)
    - [Delete your image](#delete-your-image)

## Prerequisites

- Python 3.x
- Flask
- pytest
- pytest-flask

## Installation

1. Install the required libraries:

```
pip install flask pytest pytest-flask
```

## Usage

1. Run the web app using:

```
python app.py
```

2. Open your browser and navigate to `http://127.0.0.1:5000/`. Refresh the page to update the displayed time.
![Alt Text](files/screen_shot.png)

## Testing

1. To run the unit tests, execute:

```
pytest
```

2. Ensure that the test passes and corresponds to the expected functionality of the app.

## App Description

Please refer to [PYTHON.md](PYTHON.md) for an explanation of the best practices and choices made in the app.

## Docker
* In order to build docker image manually, get app_python directory run there: 
  ```
  docker build -t your-app-image .
  ``` 
* If you wish to get image from Docker Hub, run: 
  ```
  docker pull bovvlet/app_python:latest
  ```
* And run it on backround with: 
  ```
  docker run -d bovvlet/app_python
  ```
* If you strugle to find IP on which your service is running, use this command and find it:
  ```
  docker inspect bovvlet/app_python | grep IPAddress
  ```
### Delete your container
* Find your running container:
  ```
  docker ps
  ```
* Stop it:
  ```
  docker stop {your docker container id}
  ```
* Remove it:
  ```
  docker rm {your docker container id}
  ```
### Delete your image
* Find your image:
  ```
  docker images
  ```
* Remove it:
  ```
  docker rmi {your docker image id}
  ```