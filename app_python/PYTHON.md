# Live Moscow Time Web App

## Overview

This web application displays the current time in Moscow. It features a dynamic and playful design with a color-changing container. The text inside the container has each letter displayed in a random color. It provides a fun and unique way to check the current time.

## Build locally

To run this application locally, follow these steps:

1. Navigate to the `app_pyhon` folder:

    ```bash
        cd app_python
    ```

1. Install project dependencies:

    ```bash
        pip3 install -r requirements.txt
    ```

1. Start the FastAPI application::

    ```bash
        uvicorn  src.main:app --host 0.0.0.0 --port 80 --reload
    ```

1. Open the application in your browser:

    ```bash
        http://localhost:8000
    ```

## Build with Docker locally

To run this application with Docker, follow these steps:

1. Navigate to the `app_python` folder:

    ```bash
        cd app_python
    ```

1. Build the Docker image:

    ```bash
        docker build -t app_python .
    ```

1. Run the Docker container:

    ```bash
        docker run -d -p 80:80 --name app_python app_python   
    ```

1. Open the application in your browser:

    ```bash
        http://localhost
    ```

## Build from Docker Hub

1. Pull the Docker image from Docker Hub:

    ```bash
        docker pull max3k/app_python
    ```

1. Run the Docker container:

    ```bash
        docker run -d -p 80:80 --name app_python max3k/app_python
    ```

1. Open the application in your browser:

    ```bash
        http://localhost
    ```

## Web Application Structure

### Project Structure

- Code is separated into different modules (e.g., `main.py`, `time.py`) for better maintainability.
- Static files (HTML, JavaScript, CSS) are placed in the `static` directory.

### Configuration

- Configuration settings are abstracted into a `settings.py` module.
- Requirements are managed using a `requirements.txt` file, allowing for easy dependency installation.

### Testing

- Tests are included in the `tests` directory to validate the functionality of the application.
- The `pytest` testing framework is used for writing and running tests.

### Frontend

- A basic HTML, JavaScript, CSS frontend is included in the `static` directory.
- The frontend is designed to fetch and display the current time from the backend in a dynamic and playful way.
- JavaScript is used to update the displayed time on the webpage.
- The frontend is intentionally made absurd and playful)

## Best Practices Applied

1. **Coding Standards**: The Python code adheres to PEP 8 coding style guidelines, ensuring consistency and readability.

1. **Testing**: Unit tests are included in the `tests` directory to validate application functionality using the `pytest` testing framework.

1. **Static Files**: Static files (HTML and JavaScript) are served correctly from the `static` directory, adhering to best practices.

## Framework Choice: FastAPI

### Pros

- **High Performance**: FastAPI is known for its high performance, making it suitable for building efficient web applications.

- **Automatic Documentation**: It automatically generates interactive documentation, simplifying API testing and usage. But I didn't use it in this project.

- **Asynchronous Support**: FastAPI supports asynchronous programming, allowing for concurrent request handling and improved performance.

- **Routing**: It offers a powerful routing system for defining routes and handling HTTP requests efficiently.

### Cons

- **Small Community**: FastAPI is a relatively new framework, so it has a smaller community compared to other frameworks.

## Linters

- **PEP 8**: Code follows PEP 8 guidelines for Python code formatting and style.

- **pytest**: Unit tests are written and executed using the pytest testing framework to ensure code reliability.

## Usage

- The main page displays the current time in Innopolis/Moscow.
- The text inside the container change colors for a playful effect.
- The time updates every second to reflect the current time.

## Contact

For any questions or issues, please contact:

- [Mikhail Fedorov](mailto:fedorovm093@gamil.com)
