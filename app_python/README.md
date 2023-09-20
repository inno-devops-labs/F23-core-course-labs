## Python web app
![workflow badge](https://github.com/p50000/core-course-labs/actions/workflows/app_python.yaml/badge.svg)

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

### CI
CI pipeline is done via GitHub Actions. Every push to the repository would trigger a workflow described in`.github/workflows/python-app.yml`. The workflow is the following:

- Lint the code with `ruff`
- Run unit tests in `myproject/myprojecttests.py`
- Build the Docker image and push it to Docker Hub
- Run snyk

