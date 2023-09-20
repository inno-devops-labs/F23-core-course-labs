# Python Web Application - Moscow Time Display

![Python CI](https://github.com/Ahmad-mtos/core-course-labs/actions/workflows/main/badge.svg)


## Description

This Python web application displays the current time in Moscow. It's a simple yet useful tool for users who want to know the time in the Moscow time zone.

## Features

- Shows the current time in Moscow.
- Automatically updates the displayed time upon page refreshing.

## Technologies Used

- Flask: A lightweight and flexible Python web framework.

## Installation and Setup

To run this Python web application, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Ahmad-mtos/core-course-labs.git
```

2. Navigate to the project directory:

```bash
cd app_python
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the required Python packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

5. Run the Flask application:

```bash
python app.py
```

6. Open your web browser and go to http://localhost:5000/. You will see the current time in Moscow, which will automatically update upon page refreshing.

## Docker

### How to Build

To build the Docker image for this application, follow these steps:

1. Open your terminal and navigate to the project directory where your Dockerfile is located.

2. Build the Docker image using the following command:

   ```bash
   docker build -t flask_image.
   ```

### How to Pull

If you prefer not to build the image locally, you can pull it from Docker Hub. Follow these steps:

1. Open your terminal.

2. Pull the Docker image from Docker Hub using the following command:

```
docker pull xmtosx/moscow-time
```

### How to Run

Once you have the Docker image, you can run the application in a Docker container. Follow these steps:

1. Run the Docker container using the following command:

```
docker run -p 8080:5000 xmtosx/moscow-time
```

Note: if you have built the image, use the name you have given to that image, e.g. flask_image.

2. Access the Moscow Time Display web application by opening your web browser and navigating to:

```
http://localhost:8080/time
```

You should now see the current time in Moscow, which will automatically update upon page refreshing.

## Unit Tests

The project incorporates a suite of unit tests to ensure the accuracy and reliability of the codebase. These unit tests comprehensively validate various components and functionalities within the application. Below is a summary of the primary test cases and best practices applied:

- **Test Display Moscow Time Endpoint**: This test checks the `/time` endpoint of the Flask application to ensure it provides valid Moscow time information.

- **Test Get Moscow Time Function**: This test directly evaluates the `get_moscow_time()` function, which retrieves Moscow time.

For a more detailed description of the unit tests and the best practices followed in testing, consult the [PYTHON.md](./PYTHON.md) file.