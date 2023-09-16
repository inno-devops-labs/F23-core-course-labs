![CI status badge](https://github.com/Klemencya/core-course-labs/actions/workflows/python-app-ci.yml/badge.svg?event=push&branch=lab3)

# Current Moscow time application 

This application is using standard Python libraries `datetime` and `zoneinfo` to respond with current moscow time on a simple GET / request.
The application based on Django framework.

## How to run
### Prerequisite:
Django and Python installed ([installation guide](https://docs.djangoproject.com/en/4.2/intro/install/))

### Running from command line
```
cd app_python
python manage.py runserver
```
Server runs on default localhost path http://127.0.0.1:8000/ which can be opened in any browser. The page displays current time in Moscow timezone.

## Docker

You can pull the latest version and **run** it by the following command:
```
docker run -it -p 8000:8000 klemencja/app_python
```
The application will be deployed on your http://127.0.0.1:8000/

To **build** the updated version you may change the directory to `core-course-labs` and run `docker build` 
```
cd core-course-labs
docker build app_python -t app_python
```

To just **pull** an image from dockerhub you can use:
```
docker pull klemencja/app_python
``` 

## Unit tests
The project contains unit tests for main page view in the `test_views.py` file.
To run it you can use the Pycharm `Run` button as well as django command:
`python manage.py test`
It will find all the tests and run them.