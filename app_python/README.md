# Application to display current time in Moscow

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
