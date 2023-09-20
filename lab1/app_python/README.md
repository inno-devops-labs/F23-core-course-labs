# Python Flask Web Application

This is a simple Python Flask web application that shows the current time in Moscow.

## Dockerized Application

This application has been Dockerized for easy deployment. Here are the instructions to build, pull, and run the Docker image

### Building the Docker Image

Run the following command to build the Docker image:

    docker build -t aisenbeast/my_web_app .

### Pulling the Docker Image

Run the following command to pull the Docker image:

    docker pull aisenbeast/my_web_app:latest

### Running the Docker Image

After building or pulling the image, you can run it with the following command:

    docker run -p 4000:5000 aisenbeast/my_web_app:latest


This will start the application and map port 4000 of your machine to port 5000 in the Docker container. You can then access the application in your web browser at `http://localhost:4000`.


## Unit Tests
The unit tests for this application are in the `tests/test_app.py` file. They test the `home` and `time` endpoints of the application. To run the tests, use the following command: `pytest` **IMPORTANT**: run this command in root directory.