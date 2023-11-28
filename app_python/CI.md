# Python Web Application CI

[![Python App](https://github.com/aibek99/devops-labs/actions/workflows/app_python.yaml/badge.svg)](https://github.com/aibek99/devops-labs/actions/workflows/app_python.yaml)

This file summarizes the best practices used in our GitHub Workflow, Python App.

## Overview
The workflow is triggered on each push event and consists of two jobs: `build-test` and `release`. `build-test` job verifies the Python application, and the `release` job builds and pushes a Docker image of the application to Docker Hub. Importantly, the release job depends on the successful completion of the `build-test` job.

## Best Practices
1. **Selective triggering of the workflow**: The workflow is configured to run only when there are changes in the `app_python` folder.

2. **Matrix strategy**: We're using a `matrix strategy` to test our application against multiple Python versions: `3.9` and `3.10`.

3. **Consistent environment**: The workflow runs on `ubuntu-latest` to ensure consistent build and test environments.

4. **actions/checkout@v4**: We are using the latest version of the checkout action to fetch the repository content.

5. **actions/setup-python@v4**: We're using the latest version of the setup-python action to configure the desired Python version.

6. **actions/cache@v3**: We are caching the `pip` packages required by the application to speed up the build process. This cache is keyed by the hash of the `requirements.txt` file to ensure that it is updated whenever the dependencies change.

7. **Dependency vulnerability scanning**: We are utilizing the `Snyk` action to perform vulnerability scanning on our application's dependencies and monitor the project for security issues.

8. **Running tests**: We're using `pytest` to run the application's tests. This allows us to validate our application against different Python versions.

9. **Docker Buildx setup**: We're configuring `Docker Buildx` to make our build process more efficient and gain access to additional features such as multi-platform builds.

10.  **Docker Login**: We securely log in to Docker Hub using `secrets` for the Docker Hub `username` and `password`.

11. **Docker Build and Push**: We're using the latest version of the `docker/build-push-action@v5` action to build our Docker image and push it to Docker Hub with the following tags: the current `Git commit SHA` and `latest`.

By following these best practices, our GitHub Workflow ensures a consistent, secure, and efficient CI process for our Python Application.