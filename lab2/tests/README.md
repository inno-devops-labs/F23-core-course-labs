# Moscow Time Web Application

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/CyberTDan/DevOps/Python%20CI%20with%20Docker?label=CI%20Build)](https://github.com/CyberTDan/DevOps/actions)

## Brief Project Description

This is a simple web application built with Python and Flask that displays the current Moscow time. It serves as a basic example of creating a web application with a Python web framework and displaying real-time data.

## Unit Tests

### Running Unit Tests

Before running the unit tests, make sure you have installed the required dependencies, including Flask and pytest. You can install them using pip:

```bash
pip install Flask pytest
```

## CI Workflow

This project includes a continuous integration (CI) workflow using GitHub Actions. The CI workflow has the following essential steps:

1. **Dependencies:** It installs Python dependencies specified in the `docker_install.txt` file.

2. **Linter:** It checks the codebase for code style and quality using [pylint](https://pypi.org/project/pylint/) (you can replace this with your preferred linter).

3. **Tests:** It runs unit tests using [pytest](https://docs.pytest.org/en/latest/).

4. **Docker Integration:** The workflow also includes Docker-related steps to build and push a Docker image to Docker Hub. The image can be used to deploy the application in a containerized environment.

You can view the status of the CI build using the badge at the top of this README.

### Docker Image

The Docker image for this project is available on Docker Hub: [trihlebdv/dev_hw3](https://hub.docker.com/r/trihlebdv/dev_hw3).

Feel free to use this image to deploy the Moscow Time Web Application in a containerized environment.
