# Containerization Lab - Docker

## Task 1: Dockerize Your Application


Dockerfile Creation:

Begin by creating a Dockerfile.
Ensure linting using hadolint is incorporated via make docker-lint.
Include a .dockerignore file to specify items to be excluded from the Docker build context.
Implement multi-stage builds to optimize the image size.
Minimize layers to enhance efficiency.
Leverage build cache for improved build performance.
Dockerfile
Copy code
# Start with a base image
FROM base-image:tag AS builder

# Add necessary files and perform build steps

# Final image
FROM another-image:tag
COPY --from=builder /app/output /app
Build and Test Docker Image:

Integrate testing into the Docker build process as a single stage.
bash
Copy code
# Makefile
docker-build:
    docker build -t your-image-name:tag .
Run the build process with make docker-build.
Push Image to Docker Hub:

Enable pushing the image to Docker Hub with the following command:
bash
Copy code
# Makefile
docker-push:
    docker push your-dockerhub-account/your-image-name:tag
Push the image using make docker-push.
Run and Verify Docker Image:

Pull the Docker image from Docker Hub with:
bash
Copy code
# Makefile
docker-pull:
    docker pull your-dockerhub-account/your-image-name:tag
Execute the pulled image and validate functionality.
bash
Copy code
docker run -it your-dockerhub-account/your-image-name:tag
Ensure make docker-pull retrieves the image from Docker Hub.

## Task 2: Docker Best Practices

Avoid Unnecessary Privileges:

Utilizing rootless containers by specifying a non-root user (appuser).
Not binding to a specific UID in the adduser command.
Ensuring executables are owned by root and not writable, with appropriate permissions (755) on project files.
Reduce Attack Surface:

Implementing multistage builds with three distinct stages, which helps in minimizing the final image size and potential vulnerabilities.
Utilizing a trusted base image (python:3.11-alpine3.18) to ensure a secure starting point.
Layer Sanity:

Organizing layers to optimize caching mechanisms and promote layer reuse.
Avoiding the creation of redundant layers and maintaining layer separation between different build stages.
Linting and Vulnerability Scanning:

Employing linting tools to ensure Dockerfile best practices.
Integrating vulnerability scanning tools to identify and address potential security issues.
Running Docker Runtime as Non-root:
