# Dockerfile details

This Dockerfile is used to create a Docker image for a Python application following Docker best practices.

## Docker Best Practices

1. **Slim base image:** The base image used is `python:3.10-slim`, which is a lightweight image based on the official Python image. This reduces the overall size of the final Docker image.

2. **WORKDIR:** The `WORKDIR` instruction sets the working directory to `/app`. This keeps the application files separate from the system files and allows the container to start in the correct context.

3. **Requirements first:** `COPY` and `RUN` instructions are optimized by copying the `requirements.txt` file and running `pip install` before adding the rest of the application files. This allows Docker to cache the installation step, speeding up subsequent image builds when application dependencies are unchanged.

4. **Non-root user:** A new user `appuser` is created, and user ID `1000` is assigned to this user. This user is a member of the `users` group. This is a security best practice, as it reduces the potential damage if an attacker gains control of a container.

6. **Testing:** The `pytest tests` command is run to ensure that the application passes tests before building the final image. If tests fail, the build will not continue, promoting a high-quality codebase.

7. **EXPOSE:** The `EXPOSE` instruction declares the port (`5000`) the application listens on, making it easier for other developers and tools to know which port to bind.

8. **CMD:** The `CMD` instruction provides a default executable command for the container, launching the Python application with `run.py`.

9. **Docker Ignore:** The .dockerignore file ensures that only necessary directories and files are copied when running the `COPY . .` instruction, minimizing the copied data and keeping the Docker context clean.