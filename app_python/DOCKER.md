# Dockerfile details

This `Dockerfile` is used to create a Docker image for a Python application using multistage builds and following Docker best practices.

## Docker Best Practices

1. **Slim base image**: The base image used is `python:3.10-slim`, which is a lightweight image based on the official Python image. This reduces the overall size of the final Docker image.

2. **Multistage builds**: The `Dockerfile` uses to separate the build and release stages. This helps minimize the size of the final Docker image by only including the necessary files and dependencies in the release stage.

3. **Non-root user**: A new user `appuser` is created and used within the container. This is a security best practice, as it reduces the potential damage if an attacker gains control of a container.

4. **WORKDIR**: The `WORKDIR` instruction sets the working directory to `/app`. This keeps the application files separate from the system files and allows the container to start in the correct context.

5. **Requirements first**: `COPY` and `RUN` instructions are optimized by copying the `requirements.txt` file and running `pip install` before adding the rest of the application files. This allows Docker to cache the installation step, speeding up subsequent image builds when application dependencies are unchanged.

6. **Setting ownership**: The ownership of the `/app` directory is set to the `appuser`. This ensures that the non-root user has proper access to the application files and enforces a more secure environment.

7. **Testing**: The `pytest` command is run in the test stage to ensure that the application passes tests before proceeding to the release stage. If tests fail, the build will not continue, promoting a high-quality codebase.

8. **Copying necessary files**: The necessary files from the test stage are copied to the release stage using the `COPY --from=test --chown=appuser:appuser` instruction. This only copies the required files while preserving the ownership of `appuser`, reducing the final image size and maintaining a secure environment.

9. **EXPOSE**: The `EXPOSE` instruction declares the port (`5000`) the application listens on, making it easier for other developers and tools to know which port to bind.

10. **CMD**: The `CMD` instruction provides a default executable command for the container, launching the Python application with `run.py`.

11. **Docker Ignore**: The `.dockerignore` is added to ensure that only necessary directories and files are copied while running `COPY . .` instruction
