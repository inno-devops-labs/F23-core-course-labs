# Python Web Application Development

Author: Daniil Okrug

## Overview
The application displays Moscow time. In this project I used Flask framework because of its convenience and simplicity in web application development.

## Structure
The main file is app.py which contains routes '/' and '/time'. First route renders index.html page with Moscow time. Second route provides time in Moscow timezone.

The project has a templates folder that contains HTML pages to render on the client side.

## Testing
For testing and determining the percentage of test coverage pytest and pytest-cov are used. All tests are now in the tests folder. 

## Docker

### Build
Local image building: \
`docker build -t app_python:lab2 .` \
`app_python:lab2` - can be any name you like for the image

### Docker Hub
Pull image from Docker Hub \
`docker pull bellissimo/devops-inno-daniil-okrug:lab2`

### Run
Running localy builded image: \
`docker run -d -p 5000:5000 app_python:lab2`

Running image from Docker Hub: \
`docker run -d -p 5000:5000 bellissimo/devops-inno-daniil-okrug:lab2`
