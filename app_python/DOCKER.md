## Here are best practices that I employed within the Dockerfile:

1. Using an appropriate base image: In the given Dockerfile, the base image "python:3.10.12" is used, which is a good practice as it provides the necessary environment for running a Python application.

2. Specifying a non-root user: By using the "USER" instruction (not provided in the given snippet), you can run the container with a non-root user. 

3. Setting a working directory: The "WORKDIR" instruction is used to set the working directory within the container to "/app". 

4. Copying files into the container: The "COPY" instruction copies the "main.py" file into the "/app" directory of the container. 

5. Exposing container ports: The "EXPOSE" instruction exposes port number 8008, indicating that the container listens for incoming connections on that port. 

6. Using a CMD instruction: The "CMD" instruction defines the command that the container should run by default. 


# To run
```
docker run -p 8008:8008 --user 1001 app_python
```