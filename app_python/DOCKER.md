# Implemented Docker Best Practices

## 1. Use an Official Base Image

Start with an official Python runtime as a parent image from Docker Hub. This ensures that we are using a trusted and maintained base image.

```Dockerfile
FROM python:3.10-slim-bullseye
```

## 2. Set Environment Variables and use build ARGs

Set environment variables for Flask application within the Dockerfile.

```Dockerfile
ARG port=1010

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=$port
```

## 3. Create a Working Directory

Create a working directory inside the container, and set it as the current working directory. This is where your application code will be copied.

```Dockerfile
WORKDIR /app
```

## 5. You requirements file

Copy the requirements.txt file and install Python dependencies. Using requirements.txt ensures strong versioning of python deps.

```Dockerfile
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
```

## 6. Use .dockerignore file

# Security best practices

## 1. Used docker scan

It displayed that there are no any High or Medium severity vulns, so I consider it as passed step.

## 2. Avoid root run

```Dockerfile
# Add new non-root user
RUN useradd defaultuser

# Use this user to make container root-less
USER defaultuser
```

## 3. Default non-root user has only executable permissions for binaries

defaultuser aren't able to write binaries since it's owner by root

## 4. Expose only one necessary port

## 5. Use COPY/ADD wisely

Use COPY since it's more friendly

## 6. Lint Dockerfile via hadolint

```bash
$ brew install hadolint
$ hadolint Dockerfile
```

And for my Dockerfile it produces no any errors or warning!
