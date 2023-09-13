# My Python Web App

This is a simple Python web application that displays the current time in Moscow.

## Overview

``` python
from flask import Flask
from datetime import datetime
import pytz
```

### Code here is imports of libraries that I will use later

``` python
app = Flask(__name__)
@app.route('/')
```

### Here I created flask application and defined a route

```python
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return f'Current time in Moscow: {current_time}'
```

### This function is getting current time in Moscow and then returns it in web client

``` python
if __name__ == '__main__':
    app.run()
```

### Here I just run my application  

## Usage

1. Install the required dependencies (Flask).
2. Run the application using `python app.py`.
3. Open your web browser and visit `http://localhost:5000` to see the current time in Moscow.

## Docker Containerization

This Docker container runs the Python web application and displays the current time in Moscow. The application is packaged and isolated within a Docker container.

To build the Docker image for our application, follow these steps:

1. Open your terminal and navigate to the app_python directory where the Dockerfile is located.

2. Run the following command to build the Docker image. Replace khays-python-app with your preferred image name:

    `docker build -t khays-python-app .`

### Pulling the Docker Image

If you want to pull the Docker image from Docker Hub instead of building it locally, you can use the following command:

`docker pull khays/khays-python-app:latest`

### Running the Docker Container

Once you have the Docker image built or pulled, you can run the Docker container with the following command:

`docker run -p 5000:5000 khays-python-app`

This command maps port 5000 on your local machine to port 5000 within the Docker container. You can access the application by opening a web browser and navigating to `http://localhost:5000`.

## Author

Khabib Khaysadykov
