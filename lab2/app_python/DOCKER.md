# Containerization Lab - Docker

## Task 1: Dockerize Your Application


1. Create a `Dockerfile`:
- Linting can be done with `make docker-lint`. I have used `hadolint` for this purpose.
- [Best Dockerfile practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) I used:
    * Add `.dockerignore` file
    * Employ multi-stage builds
    * Minimize the number of layers
    * Leverage build cache

2. Build and Test Docker Image:
- Testing is done as one stage within the Docker build process

3. Push Image to Docker Hub:
- `make docker-push` to push image.
[Here is my Dockerhub repository](https://hub.docker.com/repository/docker/ar7ch/devops_lab2_app_python/general).

4. Run and Verify Docker Image:
- Retrieve the Docker image from your Docker Hub account.
- Execute the image and validate its functionality.
    * `make docker-pull` pulls the image from Dockerhub.
## Task 2: Docker Best Practices

Security 

1. Enhance your docker image by implementing [Docker Security Best Practices](https://sysdig.com/blog/dockerfile-best-practices/).
- Security best practices that I implelented:
    - Avoid unnecessary privileges
        * Rootless containers (user appuser)
        * No bind to specific UID (I don't specify UID in `adduser`)
        * Make executables owned by root and not writable (setting 755 on project files)
    - Reduce attack surface
        * Multistage builds - there are 3 build stages in my Dockerfile
        * Use trusted base images - I use trusted `python:3.11-alpine3.18` base image
    - Layer sanity - my layers are organized to
        1. employ caching mechanism and re-use layers
        2. avoid creating redundant layers or keeping redundant layers between different build stages
    - Employing linting and vulerability scanning
    - Running Docker runtime as nonroot

2. Write `DOCKER.md`:
- You are reading it.

3. Enhance the README.md:
- Added **Docker** section.
  
## Bonus Task: Multi-Stage Builds Exploration

**To earn an additional 2.5 points:**

1. Dockerize Previous App:
- Craft a `Dockerfile` for the application from the prior lab.
- Place this Dockerfile within the corresponding `app_*` folder.
    * Check `app_go` directory.

2. Follow Main Task Guidelines:
   - Apply the same steps and suggestions as in the primary Dockerization task.

3. Study Docker Multi-Stage Builds:
   - Familiarize yourself with Docker multi-stage builds.
   - Consider implementing multi-stage builds, only if they enhance your project's structure and efficiency.

### Guidelines

- Utilize appropriate Markdown formatting and structure for all documentation.
- Organize files within the lab folder with suitable naming conventions.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Utilize Docker to containerize your application, adhering to best practices. Explore Docker multi-stage builds for a deeper understanding, and document your process using Markdown.
