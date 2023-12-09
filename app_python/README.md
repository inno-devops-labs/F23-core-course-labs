# Application to display current time in Moscow

![](https://github.com/5ur3/devops-core-course-labs/actions/workflows/python_app.yml/badge.svg)

### Description
Application was written in python using [falcon framework](https://falconframework.org/). It uses python standard library to retrieve current time in UTC+3 timezone, and it's only 10 lines of code.

### Collecting dependencies
`$ pip install -r requirements.txt`

### Running
`$ python3 -m gunicorn app:app`

### Running from a docker container
`$ docker pull midnoon/devops-lab:latest`
`$ docker run -p 8000:8000 midnoon/devops-lab:latest`

### Unit Tests
To run tests:
`$ python3 -m unittest app_test.Test`

### Visits counter
Application counts the number it was visited in visits file. In /monitoring/docker-compose.yml this visits file was mounted into /monitoring/visits for consistent logging

### CI Workflow
On each push, CI workflow is triggered. It installs dependencies, runs linter, tests the application, builds and pushes docker image to dockerhub. 
