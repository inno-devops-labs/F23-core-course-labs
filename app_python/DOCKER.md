# Docker Best Practices

In this document, I'll detail the best practices implemented in the Dockerfile for my Python web application, as well as some insights from my friend's Dockerfile for reference.

## Linter

I used [Hadolint](https://hadolint.github.io/hadolint/), a Dockerfile linter, to thoroughly check my Dockerfile for adherence to best practices. Linting tools like Hadolint help ensure the Dockerfile's quality and conformity with Docker best practices.

## User Privileges

In my Dockerfile, I have created a user without root permissions and assigned it a specific UID using the following commands:

```Dockerfile
RUN adduser -D simpleuser
USER simpleuser
```

This is a security best practice to minimize potential security vulnerabilities in the container. Running processes as a non-root user is recommended to enhance container security.

## Base Image Selection

I have chosen the official Python image based on Alpine Linux (`python:3.9-alpine`) as the base image for my Docker container. Alpine images are well-known for their small size and minimalistic nature, making them a preferred choice for lightweight and efficient containers.

## Exposing Ports

I have exposed port 8090 within the Docker container to make my application accessible via this port when the container is running. This is a common practice for allowing network access to specific services within the container.

## COPY vs. ADD

I have used the `COPY` command in my Dockerfile to copy files from the host into the container. This aligns with Docker best practices, as `COPY` is generally recommended over `ADD` for greater transparency and predictability in file copying.

## WORKDIR

I utilized the `WORKDIR` instruction to set the working directory inside the container to `/app`, enhancing code organization and maintainability.

## Version Compatibility

I have selected Python 3.9, which is compatible with my application's requirements. Ensuring compatibility between the base image and application dependencies is crucial to prevent compatibility issues.

These Docker best practices were incorporated into my Dockerfile to optimize security, maintainability, and efficiency in my Python web application container.
