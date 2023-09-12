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

## Contact information:
@purfreak in Telegram.