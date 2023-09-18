# Simple Web App

## Description
This a web app written in Python that displays the current time in Moscow.

## Technologies used
- Flask
- datetime

## Running the app directly on the host OS
Once in the folder containing this doc (`app_python`), start a virtual enviroment, install the requirements, and you're good to go. Commands below

    python3 -m venv .venv

    . .venv/bin/activate

    pip install -r requirements.txt

    flask run

After successfully running the app. Navigate to http://127.0.0.1:5000 to view the result.

## Running the app using Docker
Once in the folder containing this doc (`app_python`), run the following commands to build the docker image and run a container

    docker build -t devops_msk_time .

    docker run -dp 5000:5000 devops_msk_time

Alternatively, you could also pull the image from *Dockerhub* instead of building it

    docker run -dp 0.0.0.0:5000:5000 kurohata7/devops_msk_time

After successfully running the container. Navigate to http://127.0.0.1:5000 to view the result.

## Running unit tests:
Once in the folder containing this doc (`app_python`), you can use the following to run the unit test suit and generate the coverage report:

    pip install -U pytest

    python3 -m pip install coverage

    python3 -m pytest

    coverage run -m pytest

    coverage report
