[![Python Workflow](https://github.com/vladislav5ik/core-course-labs/actions/workflows/python.yml/badge.svg)](https://github.com/vladislav5ik/core-course-labs/actions/workflows/python.yml)

# Time-app

Time-app is a Python web application that displays the current time in Moscow.

### Additional features
App has endpoints:
- `/metrics` that returns metrics in Prometheus format.
- `/health` that returns the status of the application.
- `/docs` that returns the documentation of the application in openAPI format.
- `/visits` that returns the number of visits.

## Installation using docker
### Build docker image
To build the Docker image, clone the repo, and use the following command inside `app_python` directory:
```
docker build --tag timeapp .
```
### Run docker container
To run the Docker container after building it, use the following command:
```
docker run -p 8080:8080 timeapp:latest
```
### Pull docker image
To pull an image from a Docker registry, use the following command:
```
docker pull vladspigin/timeapp:latest
```

## Installation
### Getting started
1. Setup a Python virtual environment
2. Install dependencies
3. Run the application

### Setup virtual environment
```
python -m venv venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements-base.txt
```

### Run
```
uvicorn app.main:app
```
Now you can open `http://127.0.0.1:8000/` in your browser to check the time. Also you can check documentation at `/docs` path.

### Development
For development, install additional dependencies:
```
pip install -r requirements-dev.txt
```
Run this command to set up the git hook scripts:
```
pre-commit install
```

Run the app:
```
python dev.py
```
### Unit Tests
Run tests:
```
pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
