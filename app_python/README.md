# Python Web Application

This is a simple Python web application developed using Flask that displays the current time in Moscow. The time is fetched using the `datetime` and `pytz` libraries in Python.

## Overview

- [Project Structure](#project-structure)
- [Installation process](#installation-process)
- [Unit Testing](#unit-testing)
- [Usage](#usage)
- [Docker](#docker)
- [Contributing](#contributing)

## Project Structure

The project structure is as follows:

- `app.py` - This file contains the Flask application logic.
- `tests.py` - This file contains the unit tests for the application.
- `static/` - This folder contains the static files.
  - `style.css` - This CSS file contains the styles for the application.
- `templates/` - This folder contains the HTML templates.
  - `index.html` - This HTML template displays the current time.

## Installation process

1. Clone the repository:
    >`git clone https://github.com/relisqu/core-course-labs`

2. Navigate to the app_python folder:
    >`cd app_python`

3. Install the required dependencies:
    > `pip install flask`

## Unit Testing

`unittest` is a Python unit testing framework. It is a standard library module, so no installation is required.

1. Run the tests:
    > `python tests.py`

## Usage

Start the Flask development server by running
> `python app.py`

The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Docker

We also can run this application using Docker. This will require docker to be installed beforehand. After it we need to pull the Docker image from Docker Hub:

> docker pull relisqu/python-app

After pulling the image, a container can be started using the following command:

> docker run -p 5000:5000 relisqu/python-app

The application will then be accessible at 127.0.0.1:5000

## CI

## Contributing

If you'd like to improve this project or report issues, please open an issue or submit a pull request.
