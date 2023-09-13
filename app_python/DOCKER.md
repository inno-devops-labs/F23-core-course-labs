# Docker Best Practices

In this file I will describe what best practices I used while creating the Docker image for the application.

## 1. Security

I am running the application inside the Docker image as a non-root user. By granting only the necessary permissions and specifying clear boundaries I am ensuring the proper security level.

## 2. Avoid Caching for Requirements

By specifying `--no-cache-dir` while installing requirements, I reduce number of layers in the image what optimises performance and resources.

## 3. Using `.dockerignore`

By removing unnecessary files in `.dockerignore` I am lowering the image size and reduce build time.

## 4. Base Image Selection

I am using the official Docker image and specifying explicitly the version of the base image: `python:3.9`.

## 4. Base Image Selection

I am using the official Docker image and specifying explicitly the version of the base image: `python:3.9`.