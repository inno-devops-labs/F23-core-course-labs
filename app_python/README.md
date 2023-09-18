# Web application: current time in Moscow

## Overview:
A simple FastAPI application that displays the current time in Moscow, Russia.

## Running the application:
- **clone the repository to your local machine**
- **set up virtual environment**:

`python3 -m venv venv`
`source venv/bin/activate/`

- **install requirements**:
`cd app_python`
`pip3 install -r requirements.txt`

- **run the application**:
`uvicorn app:app reload`

## Docker:

### Building the Docker image:
```bash
docker build -t purfreak/lab2_devops:latest .
```

### Pulling the Docker image:
```bash
docker pull purfreak/lab2_devops:latest
```

### Running the Docker image:
```bash
docker run -d -p purfreak/lab2_devops:latest
```

## Usage:
You can view the current time in Moscow, Russia by visiting http://127.0.0.1:8000/.

## Unit tests
The application uses FastAPI's built-in `TestClient` to ensure that endpoints function as expected. I've applied several best practices in my testing approach:

- **isolation**: each test can run independently, ensuring no side effects,
- **coverage**: I aim for comprehensive coverage to ensure all functionalities are tested,
- **mocking**: external services are simulated using mocking for accurate testing.

To run the tests, use the command: `pytest`

## CI workflow
- **checkout**: clones the repository to the GitHub Actions runner,
- **set up Python**: initializes the Python 3.9 environment,
- **install dependencies**: installs the necessary Python packages from app_python/requirements.txt,
- **linting**: uses flake8 to check for linting errors in the codebase,
- **run tests**: executes unit tests with pytest to validate the application's functionality,
- **login to DockerHub**: authenticates using provided secrets,
- **build Docker image**: constructs a Docker image from the project,
- **push to DockerHub**: uploads the built image,
- **vulnerability check**: uses Snyk to scan for high-severity vulnerabilities in the project.

## Contact information:
@purfreak in Telegram.
