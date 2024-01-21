# Docker Best Practices

## 1. Use Specific Base Image Tags

- **Best Practice**: Avoid the `latest` tag for base images. Instead, specify a version for predictable and repeatable builds.
- **Implementation**: In the Dockerfile, `python:3.11-slim` is used instead of `python:latest`.

```dockerfile
FROM python:3.11-slim
```

## 2. Run as a Non-root User

- **Best Practice**: Avoid running applications inside the container as the root user to enhance security.
- **Details**: When creating a non-root user, it's vital to set proper permissions for directories and files the application might need to access. This action restricts the container from running as root and defines clear boundaries for what the application user can and cannot access.
- **Implementation**: In the Dockerfile, a new user `appuser` is created, given ownership of the `/app` directory, and then set as the current user.

```dockerfile
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser
```

## 3. Minimize the Number of Layers

- **Best Practice**: Reduce the number of layers in the Docker image by combining commands.
- **Implementation**: In the Dockerfile, installation commands and cleanup are combined in a single `RUN` instruction.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

## 4. Health Checks

- **Best Practice**: Implement health checks to confirm the service in the container is operating as expected.
- **Implementation**: A health check is added in the Dockerfile.

```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1
```

## 5. Use `.dockerignore`

- **Best Practice**: Exclude unnecessary files from the build context with a `.dockerignore` file. This action reduces the build time, minimizes the image size, and prevents potential security risks.
- **Implementation**: A `.dockerignore` file is recommended to exclude unnecessary files.

```plaintext
__pycache__/
*.pyc
*.pyo
*.egg-info/
*.log
*.git/
Dockerfile
*.md
```

## 6. Logging

- **Best Practice**: Direct application logs to the `stdout` and `stderr` streams, allowing Docker to manage them.
- **Implementation**: In the Flask application, logging is configured to output to `stdout` using StreamHandler.

```python
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
```

## 7. Avoid Storing Secrets in the Image

- **Best Practice**: Do not store secrets or sensitive data in the Docker image. Instead, use environment variables, Docker secrets, or the orchestration platform's secrets management.
- **Implementation**: Secrets are not embedded in the Dockerfile. They should be passed in at runtime using environment variables or other secure mechanisms.

