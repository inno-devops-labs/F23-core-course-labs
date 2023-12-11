# Go Application CI

[![Go App](https://github.com/NodirBobiev/devops-labs/actions/workflows/app_go.yaml/badge.svg)](https://github.com/NodirBobiev/devops-labs/actions/workflows/app_go.yaml)

This repository utilizes a GitHub Actions workflow to build, test, and release a Go application. The following best practices have been used in the CI setup:

## Workflow Triggers

1. **Path Filtering**: The workflow is only triggered when there are changes in the `app_go` directory or the workflow file itself. This saves resources and time by not running the workflow when unrelated changes are made in the repository.

## Workflow Environment Variables

1. **Maintainability**: The Docker image name is defined as an `environment` variable at the beginning of the workflow. This improves maintainability by centralizing the value and making updates easier.

## Testing Job

1. **Parallel jobs**: `Test` and `release` jobs are separated and will run in parallel, reducing the duration of the entire workflow.

2. **Latest Ubuntu version**: The `test` job runs on the latest version of Ubuntu, ensuring compatibility with the most recent system updates.

3. **Checkout action**: The latest version of GitHub's `actions/checkout` action is used to efficiently fetch and manage the repository contents.

4. **Go setup action**: The latest version of `actions/setup-go action` is used to set up and manage Go versions, ensuring maximum compatibility and performance.

5. **Go module caching**: Caches Go dependencies to significantly speed up build times.   

6. **Working directory**: The `working-directory` property is used to define the location of the Go application, making it easier to manage paths in the workflow.   

## Release Job

1. **Dependency on test job**: The `release` job depends on the test job, ensuring that the release happens only when tests pass.

2. **Docker Buildx action**: The latest version of `docker/setup-buildx-action` is used to create a Buildx environment with multi-platform and caching support.

3.  **Docker Login**: We securely log in to Docker Hub using `secrets` for the Docker Hub `username` and `password`.
   
4. **Docker Build and Push action**: The latest version of `docker/build-push-action` is used to build and push Docker images, with built-in caching support and improved build arguments handling.

5. **Tagging**: Docker images are tagged with the `commit SHA` and `latest` tag, ensuring a clear history of past releases and easy access to the most recent stable version.