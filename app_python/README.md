# Python Web Application 

[![Python App](https://github.com/aibek99/devops-labs/actions/workflows/app_python.yaml/badge.svg)](https://github.com/aibek99/devops-labs/actions/workflows/app_python.yaml)

The application displays the current date and time, as this is the first lab assignment for the DevOps course at the university

## Installation

***We highly recommend that you set up a Python environment to install dependencies:***
```
$ python3 -m venv env
$ source env/bin/activate
```

Clone the repository and install the dependencies:

```
$ git clone https://github.com/aibek99/devops-labs
$ cd devops-labs/app_python
$ pip install -r requirements.txt
```

## Running the Application

Start the application with the run.py script:

```
$ python run.py
```

The application should now be running at http://localhost:5000.

## Running the Tests

```
$ pytest tests
```

## Running the Linter
```
$ pylint app
```

## Docker 
To build the image run the following command:
```
docker build -t devopspy .
```

To run the image run:
```
docker run --rm -p 5000:5000 devopspy
```

* `--rm` here stands for deleting the container right after it is stopped

Or if you want to pull the image from the docker hub:


```
docker pull aibekbakirov/devopspy:v1.0
```

## Contacts

* email: `aibek.bakirov99@gmail.com`
