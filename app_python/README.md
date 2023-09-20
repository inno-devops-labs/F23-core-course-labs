## Python web app

This is a web application which displays current time in moscow time zone. It is written using Django as a framework.

### To install
1. Clone the repository
2. Install django:

     `pip3 install django`
3. Run the app:

    `python manage.py runserver`

Go to http://localhost:8000/display_time/ to see current time

### Unit Tests
1. Run tests using the following command:

`python manage.py test myproject.tests.CurrentMskTimeTest`

### To run via docker image
It's possible to pull and run the application as an image from Docker hub. Installed docker is required.
1. Pull the image

    `docker pull rentacat45/python-web-app`

2. Run the container

    `docker run -it -p 8000:8000 rentacat45/python-web-app`

Access through http://localhost:8000/display_time/ to see current time

