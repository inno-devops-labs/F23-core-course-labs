## Python app

### Prepare to work
- Run `pip install flask`

### Run web app
python main.py

## Docker

This section provides instructions on how to containerize and run the application.

### Build

To build the Docker image, navigate to the app_python directory and run the following command:

```docker build -t myapp .```

### Pull

To pull the Docker image from a remote repository, use the following command:

```docker pull muurrk/myapp:first-image```

### Run

To run the application as a Docker container, execute the following command:

```
docker run -p <port>:8080 myapp
```