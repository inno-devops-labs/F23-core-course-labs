# Docker Configuration and Best Practices

This document provides an overview of the Docker setup for the project and outlines best practices followed for creating Docker images.

## Dockerfile

The project uses a Dockerfile for building Docker images. Below is the structure of the Dockerfile:

* Create 'Dockerfile' file and write there:

    ```dockerfile
    RUN useradd -m -r -u 1001 myuser

    USER myuser
    
    FROM python:3.11-alpine
    
    WORKDIR /app_python
    
    COPY . /app_python
    
    # Install needed packages from requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt
    
    RUN chmod 755 /app
    
    EXPOSE 8000
    
    CMD ["python", "-m", "venv", ".venv", "&&", ".venv/Scripts/Activate", "&&", "flask", "run"]
    #CMD ["python -m venv .venv && . .venv/bin/activate.bat && flask run"]

  

* Check style with linter hadolint. I am using online version https://hadolint.github.io/hadolint/


* Build dockerfile:

    ```shell
    docker build -t app_python:latest .

 that build docker images with name 'app_python' and tag 'latest'


* Then check image with
    ```shell
    docker images

* Run it:
    ```shell
    docker run -it --rm app_python:latest
  
-it: Enables interactive mode for seeing output and interacting with the container.

--rm: Automatically removes the container when it exits.
  

* If everything OK, push it into Docker Hub, authorize first
    ```shell
    docker login -u <username>
    <password>
    docker tag app_python:latest <username>/app_python:v1
    docker push <username>/app_python:v1

* Check my Docker Image here: 
https://hub.docker.com/layers/expluto/app_python/v1/images/sha256:eef04ddb0b77f0a31358331af52889eb204da2eaeb36ff43f66d76601357489c?uuid=4367C404-F620-45CA-AD9C-F9BA768DBD15


* To get image from Docker Hub
    ```shell
    docker pull <username>/app_python:v1
  
* And run it:
    ```shell
    docker run -it --rm <username>/app_python:v1
    






