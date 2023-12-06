# Web application - Moscow time

[![DevOps Python App CI](https://github.com/vladimirKa002/devops-course-labs/actions/workflows/python.yml/badge.svg?branch=Lab3)](https://github.com/vladimirKa002/devops-course-labs/actions/workflows/python.yml)

## Motivation
The goal of the project is to allow users see current Moscow time in a browser page.


## Description
The project is implemented using Python Flask framework. It provides one route '/' to the
main page where Moscow time is displayed. The project is tested using pytest framework.

The web application provides the following functionality:
- Display current Moscow time
- Update the time when the page refreshes


## Installation
In order to install the project one has to firstly clone the repository:  
`git clone https://github.com/vladimirKa002/devops-course-labs.git`

Then install necessary dependencies:  
`pip install -r requirements.txt`


## Usage

### Manual

To run the application use the command:  
`python app_python/app.py`

Then open `http://127.0.0.1:5000/` in your web browser. You will see a message like as follows:  
`Current Moscow time is 2023-09-06, 08:51:18.794`

You can also point to `/visits`. Here you can see amount of visits of the time webpage.

Below are the routes with descriptions:
`/` - show current moscow time
`/visits` - visits count of the time webpage

### Docker

#### How to build?

Run the following command to build the docker image:  
`docker build -t app_python .`

#### How to pull?

In order to pull the Docker container image run this command:  
`docker pull vladimirka002/innopolis-devops-python-app`

#### How to Run?

You can run the application using the following command:  
`docker run -p 5000:5000 vladimirka002/innopolis-devops-python-app`

The application will be accessible via the following link: `http://localhost:5000/`


## Unit Tests

To test the application use the following command which will invoke pytest:  
`python -m pytest`


## Author
Vladimir Kalabukhov, v.kalabukhov@innopolis.university