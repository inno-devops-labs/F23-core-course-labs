# Python Web Application

Simple Web application that displays Current Moscow time and date that is made using Django on DevOps course

## Installation

Clone the repository and install the dependencies:

```
$ git clone https://github.com/ShohKhan-dev/core-course-labs
$ cd app_python
$ pip install -r requirements.txt
```

## Running the Application

Start the application:

```
$ python manage.py runserver
```
It should run on Localhost: http://127.0.0.1:8000/

## Running the Tests

```
$ python manage.py test
```

It should run 2 tests.

## Running the Linting and Formatting
```
$ pre-commit run --all-files
```
