# C# Web Application

This is a simple ASP.net web application that shows the current time in Moscow. Run in port 5001

## Dockerized Application

This application has been Dockerized for easy deployment. Here are the instructions to build, pull, and run the Docker image

### Building the Docker Image

Run the following command to build the Docker image:

    docker build -t aisenbeast/dotnet-docker .

### Pulling the Docker Image

Run the following command to pull the Docker image:

    docker pull aisenbeast/dotnet-docker:latest

### Running the Docker Image

After building or pulling the image, you can run it with the following command:

    docker run -p 4000:5001 aisenbeast/dotnet-docker:latest


This will start the application and map port 4000 of your machine to port 5001 in the Docker container. You can then access the application in your web browser at `http://localhost:4000`.
