Containerization Lab - Docker
Bonus Task: Exploring Multi-Stage Builds for Go Application
Create Dockerfile:

Perform linting with make docker-lint using hadolint.
Followed Best Dockerfile Practices by:
Including a .dockerignore file.
Implementing multi-stage builds with distinct build and production stages.
Reducing the number of layers.
Optimizing build cache utilization.
Build and Test Docker Image:

Testing integrated within the Docker build process.
Push Image to Docker Hub:

Execute make docker-push to push the image.
Run and Verify Docker Image:

Retrieve the Docker image from Docker Hub.
Execute the image and validate functionality with make docker-pull.
Task 2: Docker Best Practices
Security

Enhance Docker Image Security:

Implemented Docker Security Best Practices:
Avoided unnecessary privileges.
Utilized rootless containers with the user nobody.
No binding to specific UID.
Set executables as owned by root and made them not writable (755 permission on project files).
Reduced attack surface.
Implemented multistage builds with three stages in the Dockerfile.
Utilized trusted base images, specifically distroless base images, to reduce attack surface by keeping only runtime dependencies.
Maintained layer sanity, organizing layers to avoid redundancy between different build stages.
Employed linting and vulnerability scanning.
Ran Docker runtime as non-root.
Write DOCKER.md:

You are currently reading it.
Enhance README.md:

Added a dedicated Docker section.