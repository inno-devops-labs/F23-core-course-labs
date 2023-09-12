# Best practices for dockerizing application

## .dockerignore

I used a .dockerignore file, so that only necessary files are included in the Docker image.

## Linting

To ensure following best practices I used [hadolint](https://github.com/hadolint/hadolint) linter to check for any issues.

## COPY and RUN

I used COPY instead of ADD, also I combined RUN commands to reduce the number of layers.

## Official base image

I used the official Docker image of Python (python:3.8-slim-buster) which is maintained and safe.

## Non-root user

I created a non-root user and ran all commands under that user. This reduces the attack surface and improves security.
