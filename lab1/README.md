# Lab 1 - Web application

Azamat Shakirov B20-CS

a.shakirov@innopolis.university



![](https://github.com/Hephzibah8625/core-course-labs/actions/workflows/app-python.yaml/badge.svg)

## Overview

Application to display current time in Moscow in format YYYY-MM-DD HH:MM:SS

## Docker

Building docker container:

```bash
docker build dev-ops-lab-2 .
```

Or pulling from Docker Hub:

```bash
docker pull hephzibah301/dev-ops-lab-2:latest
```

To start docker image:

```bash
docker run -p 5000:5000 dev-ops-lab-2
```

Application will available via [http://127.0.0.1:5000](http://127.0.0.1:5000) 

## Build

Packages installation:

```bash
pip3 install -r requirements.txt
```

## Run

```python
python3 main.py
```

## Unit Tests

```python
pytest test.py
```

## CI Workflow

#### Workflow Steps

1. **Checkout**: Checks out the repository code.
2. **Set up Python**: Sets up the Python version specified (Python 3.9 in this case).
3. **Install dependencies**: Installs the project dependencies using the `requirements.txt` file.
4. **Lint with flake8**: Runs the flake8 linter to check for code style and formatting issues.
5. **Test with pytest**: Executes pytest to run the tests located in the `test.py` file.
6. **Checks for vulnerabilities**. Launches Snyk to ensure project security.
7. **Login to Docker registry**: Logs in to the Docker registry using the provided credentials stored as GitHub secrets.
8. **Set up Docker Buildx**: Sets up Docker Buildx, which is a Docker CLI plugin for multi-platform builds.
9. **Build and push**: Uses Docker Buildx to build the Docker image using the specified Dockerfile and pushes it to the Docker registry with the specified tags.

#### Secrets

This workflow relies on three secrets, `DOCKER_USERNAME` , `DOCKER_PASSWORD` and `SNYK_TOKEN`, which are used for logging in to the Docker registry and SNYK secuity platfom.

## Usage

After starting the application visit [http://127.0.0.1:5000](http://127.0.0.1:5000) or directly from terminal

```bash
curl http://127.0.0.1:5000
```

## Contact

a.shakirov@innopolis.university

