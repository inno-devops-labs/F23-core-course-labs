# Unpyclock
> Simple Flask application which displays current time in the Moscow 


[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python website")
![Deploy workfow](https://github.com/lcensies/core-course-labs/blob/main/.github/workflows/deploy.yml/badge.svg)



## Features


- Configuration of the application is managed in the `config.py`
    - The following environmental variables can be changed
        - `CLOCK_TZ` - timezone to display. Shows Europe/Moscow by default.
        - `HOST` - host to listen. Defaulted to `0.0.0.0` to accept all requests. 
        - `FORMAT` - default format to display datetime in.



## Installation

```bash
# Install python3 using your distro's package manager
sudo apt update && sudo apt install python3 python3-pip python3-flask gunicorn

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Running the application

- In order to start the application in debug, you can run
```bash
flask run
```

- In the production you have to use suitable web server, for example gunicorn
```bash
cd ../ && gunicorn --bind 0.0.0.0:8000 app_python.wsgi:app && cd -
```

## Usage

- ![](assets/2023-09-06-09-33-50.png)


## Development

### Testing

- In order to run tests for this application, you can can invoke pytest (assuming that you have dependencies from the `requirements.txt` installed)
```bash
python3 -m pytest
```

## Docker

- How to build?
    - `docker build -t app_python .`
- How to pull?
    - `docker pull 0x22d1ab/app_python:stable`
- How to run?
    - `docker run --rm -it -p 8000:8000 --name app_python 0x22d1ab/app_python:stable`

## CI

### Trigger Events:
- Workflow name: "Build unpyclock"
- Triggered on two events:
  - `push`: When changes are pushed to the repository (files within 'app_python/' or '.github/workflows/unpyclock.yml').
  - `pull_request`: When pull requests are opened or updated (files within 'app_python/' or '.github/workflows/unpyclock.yml').

### Environment Variables:
- `PYTHON_VERSION`: Set to "3.11".

### Jobs:
1. **lint**:
   - Lints Python code using the `ruff` tool.
   - Runs on Ubuntu 22.04 runner.
   - Sets working directory to 'app_python'.
   - Steps:
     - Check out the code.
     - Set up Python version and cache pip dependencies.
     - Install project dependencies including 'ruff'.
     - Run linting using 'ruff'.

2. **test**:
   - Runs tests using pytest.
   - Matrix configuration for Ubuntu 22.04 and Ubuntu 20.04 runners.
   - Sets working directory to 'app_python'.
   - Steps include installing 'pytest' and running tests using pytest.

3. **snyk-check**:
   - Checks for vulnerabilities in project dependencies using Snyk.
   - Runs on Ubuntu 22.04 runner.
   - Sets up Python, installs dependencies, and runs Snyk.
   - Uses a Snyk token from GitHub secrets.

4. **build_push**:
   - Builds and pushes a Docker image to Docker Hub.
   - Runs on Ubuntu 22.04 runner.
   - Depends on 'lint', 'test', and 'snyk-check' jobs.
   - Steps:
     - Sets up Docker Buildx for multi-platform image building.
     - Logs in to Docker Hub using GitHub secrets credentials.
     - Builds and pushes a Docker image with 'latest' tag to Docker Hub.

**Note**:
- The 'test' job runs on two Ubuntu versions using the `matrix` strategy.
- A section to run Snyk code tests is commented out, likely due to GitHub runner issues.
- Assumes variables like `secrets.DOCKERHUB_USERNAME` and `secrets.DOCKERHUB_TOKEN` are stored in GitHub secrets for Docker Hub authentication.