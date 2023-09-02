# Python Web Application 

The application displays the current date and time, as this is the first lab assignment for the DevOps course at the university

## Installation

***We highly recommend that you set up a Python environment to install dependencies:***
```
$ python3 -m venv env
$ source env/bin/activate
```

Clone the repository and install the dependencies:

```
$ git clone https://github.com/NodirBobiev/devops-labs
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