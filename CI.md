# Continuous Integration (CI) for Moscow Time Web Application

This repository includes a CI workflow using GitHub Actions to build and test the Moscow Time Web Application. The CI workflow automates the process of building the application, running linting checks, executing unit tests, and pushing a Docker image to Docker Hub.

## CI Workflow Overview

The CI workflow is triggered on every push to the `main` branch and for pull requests targeting the `main` branch. It runs on an Ubuntu-based runner and consists of the following steps:

1. **Checkout code**: This step checks out the code from the repository, making it available for the subsequent steps.

2. **Cache Python packages**: To improve workflow efficiency, Python dependencies are cached using GitHub Actions' caching mechanism. This step checks for cached dependencies and restores them if available, reducing the time required for dependency installation. The cache key is generated based on the contents of the `requirements.txt` file.

3. **Set up Python**: This step sets up the Python runtime environment, specifying Python 3.9 for the workflow.

4. **Install dependencies**: Python dependencies specified in `docker_install.txt` are installed using `pip`. This step is responsible for installing the necessary packages required for the application.

5. **Run linter**: The linting step uses `pylint` to perform code quality checks on Python scripts located in the `scripts/` directory. Linting helps maintain code consistency and identify potential issues.

6. **Run tests**: Unit tests for the application are executed using `pytest`. This step ensures that the application functions correctly and detects any regressions.

7. **Docker Login**: Docker Hub credentials are used for logging in to Docker Hub to push the Docker image. The username and password are stored as GitHub secrets for security.

8. **Build Docker image**: This step builds a Docker image named `trihlebdv/dev_hw3:latest` based on the Dockerfile located in the repository. The Docker image encapsulates the Moscow Time Web Application.

9. **Push Docker image**: The final step pushes the Docker image to Docker Hub, making it available for deployment.

## Python Package Caching

One of the key optimizations in this CI workflow is the caching of Python dependencies. Caching is implemented using GitHub Actions' caching mechanism. Here's how it works:

- The `cache` action is used to check for cached Python dependencies stored in `~/.cache/pip`.

- If a cache hit occurs (i.e., cached dependencies are found and match the cache key), the dependencies are restored, skipping the installation step.

- If there is a cache miss (i.e., dependencies have changed), the workflow proceeds to install the dependencies specified in `docker_install.txt`.

- The cache key is generated based on the contents of the `requirements.txt` file to ensure that the cache is invalidated when the dependencies change.

This caching strategy reduces the time required for dependency installation, making the CI workflow more efficient.

For more details on the CI workflow, refer to the [GitHub Actions workflow configuration](.github/workflows/python-ci-with-docker.yml).

Feel free to customize and extend this CI workflow as needed for your project.
