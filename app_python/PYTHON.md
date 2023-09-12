### Reasons to use http.server


1. **Easy to set up**: `http.server` is included in the Python standard library, so there is no need to install any additional dependencies. 

2. **Simple code**: The `http.server` module provides a straightforward API, making it easy to understand and work with. It simplifies the process of handling HTTP requests and responses, enabling developers to focus on the logic of their application rather than dealing with low-level networking details.

3. **Quick prototyping**: `http.server` is great for prototyping or developing small applications because it provides a basic foundation for handling HTTP requests and responses. It allows you to quickly test your code and see the results in a browser, making it easy to make changes.

4. **Cross-platform compatibility**: Since `http.server` is part of the Python standard library, it is available on all major platforms (Windows, macOS, and Linux).

5. **Deployment flexibility**: Once application is built using `http.server`, it can be easily deployed to various hosting platforms or servers. 

While `http.server` is useful for developing simple Python applications, it may not be the best option for more complex or production-ready applications. However, for a small application such as a web application for displaying Moscow time, it is quite sufficient.

### Best practices used in web application

Some best practices used in the provided code are:

1. Code organization: The code is organized into a class named `TimeServer` which handles the HTTP request and response.
2. Separation of concerns: The code separates the HTTP server logic from the time-related logic. The `TimeServer` class is responsible for handling HTTP requests, and the time calculation and formatting are done within the `do_GET` method.
3. Variable naming: The variable names are descriptive and make the code more readable. 
4. Portability: The code uses the `socketserver` module to create a TCP server, making it platform-independent and allowing it to be run on any machine.
5. Usage of `if __name__ == '__main__'` guard: This practice ensures that the code within this block is only executed if the script is run directly and not when imported as a module.


### Coding Standarts

To follow coding standards, I ensured proper indentation and used descriptive variable and function names. I also followed the PEP 8 style guide, which includes conventions for naming, indentation, line length, and more. I tested the code manually, as because the project is small it is not practical for now to write tests for verification. I used the pylint tool to ensure the quality of the code.


## Docker Section

### Prerequisites
Before running the application, make sure you have Docker installed on your machine.

### Build the Image
To build the Docker image, navigate to the root directory of the project and run the following command:

```
docker build -t app_python .
```

### Pull the Image

```
docker pull wildqueue/devops-hw:tagname
```


### Run the Container
To run the Docker container, use the following command:

```
docker run -p 8008:8008 --user 1001 app_python
```


This command will start the container and map port 8008 from the container to port 8008 on your local machine.

Once the container is running, you can access the application by opening a web browser and navigating to http://localhost:8008.

### Stop the Container
To stop the container, first identify the container ID or name by running:

```
docker ps
```


Then, stop the container by running:

```
docker stop <<container_id_or_name>>
```

Or by 

```
ctrl+c
```