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

    coverage run -m pytest

    coverage report

## CI/CD
This project uses Github Actions as its CI tool. The CI workflow will run on Ubuntu in the `app_python` directory following any `push` events. The workflow contains multiple stages:

### Python
0. Cache check: The workflow will first check for cached dependencies from previous runs, if successful, it will restore them to speed up the next step and increase efficiency. [Ref](https://github.com/actions/cache)
1. Dependency installation: The workflow will install dependecies from `requirements.txt` in addition to ruff and pytest iff not cached.
2. Linting: The workflow will run Ruff to lint all the python code using the config in `ruff.toml`.
3. Testing: The workflow will then run any tests present in the repo using Pytest.

### Security
4. Vulnerability testing: The code will be tested for any vulnerabilities and the CI pipeline will be halted if any are found. This step also makes use of the cache from the previous step.

### Deployment
5. Docker Login: At this stage, the workflow will use secrets stored in the repo to login to a Docker Hub account. [Ref](https://github.com/docker/login-action)
6. Docker Push: Finally, the workflow will build a docker image following the config in the repo and push it to Docker Hub. [Ref](https://github.com/docker/build-push-action)
