# Best Practices for Dockerizing a Flask App

## Linting

To ensure that my Dockerfile follows best practices, I used [Hadolint](https://github.com/hadolint/hadolint) linter to check for any issues.

## Non-root user

I created a non-root user and ran all commands under that user. This reduces the attack surface and improves security.

## .dockerignore

I used a .dockerignore file to reduce the build context. This ensures that only necessary files are included in the Docker image.

## COPY vs ADD

As recommended by Docker, I used COPY instead of ADD to copy files into the container.

## Minimize attack surface

I exposed only the necessary port for the Flask app to listen on. Additionally, I used the official Docker image of Python (python:3.9-slim-buster) which is regularly updated and maintained.

## Use absolute paths and WORKDIR

I used absolute paths and WORKDIR to set the working directory inside the container. This ensures that the application code is copied to the correct location and improves maintainability.

By following these best practices, I can ensure that Docker image is secure, efficient, and easy to maintain.
