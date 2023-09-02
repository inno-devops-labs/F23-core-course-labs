
# Containerization Lab - Docker

## Bonus Task: Multi-Stage Builds Exploration for Go application


1. Create a `Dockerfile`:
- Linting can be done with `make docker-lint`. I have used `hadolint` for this purpose.
- [Best Dockerfile practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) I used:
    * Add `.dockerignore` file
    * Employ multi-stage builds - there are `build` and `production` stages in my Dockerfile
    * Minimize the number of layers
    * Leverage build cache

2. Build and Test Docker Image:
- Testing is done as one stage within the Docker build process

3. Push Image to Docker Hub:
- `make docker-push` to push image.
[Here is my Dockerhub repository](https://hub.docker.com/repository/docker/ar7ch/devops_lab2_app_go/general).

4. Run and Verify Docker Image:
- Retrieve the Docker image from your Docker Hub account.
- Execute the image and validate its functionality.
    * `make docker-pull` pulls the image from Dockerhub.
## Task 2: Docker Best Practices

Security 

1. Enhance your docker image by implementing [Docker Security Best Practices](https://sysdig.com/blog/dockerfile-best-practices/).
- Security best practices that I implelented:
    - Avoid unnecessary privileges
        * Rootless containers (user `nobody`)
        * No bind to specific UID
        * Make executables owned by root and not writable (setting 755 on project files)
    - Reduce attack surface
        * Multistage builds - there are 3 build stages in my Dockerfile
        * Use trusted base images - I use `distroless` base images. Those images only keep runtime dependencies of containers, reducing shell tools and redundant users thus reducing the attack surface.
    - Layer sanity - my layers are organized to
        1. avoid creating redundant layers or keeping redundant layers between different build stages
    - Employing linting and vulerability scanning
    - Running Docker runtime as nonroot

2. Write `DOCKER.md`:
- You are reading it.

3. Enhance the README.md:
- Added **Docker** section.