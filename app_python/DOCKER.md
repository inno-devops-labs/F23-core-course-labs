# Docker

## Dockerfile Best Practices

This document outlines best practices observed in the given Dockerfile.

### Base Image Selection

- Using the official Python base image from *Dockerhub* as well as specifying the Python version to ensure compatibility with the Flask app.

### Create a Non-Root User

- The Dockerfile creates a non-root user named "newuser" with the `-D` flag, which ensures that the user won't have a password set, enhancing security.

### Set a Working Directory

- The `WORKDIR` instruction sets the working directory to `/msk_time`, which makes it clear where the subsequent commands will be executed. This enhances organization and readability.

### COPY instead of ADD

- The `COPY` instruction is used to copy the current directory (represented by `.`) into the container's `/msk_time` directory.

### Use the USER Instruction

- After creating the non-root user, the `USER` instruction switches to using the "newuser" account. This limits the container's privileges, which is a security best practice.

### Expose Ports Explicitly

- The `EXPOSE` instruction is used to indicate that the container will listen on port 5000.

### Use an Entry Point

- The `ENTRYPOINT` instruction specifies the command to run when the container starts. In this case, it runs a Flask application. Using an entry point is a good practice for defining the container's primary executable and preventing the user from overriding.

### RUN in a single layer

- Even though in this scenario only on command was necessary to prepare the image, it is present under a single `RUN` command to ensure layer sanity. If multiple commands were needed, they would have simply been grouped by `&&` under a single `RUN` command.

### .dockerignore

- A *.dockerignore* file is present in the same directory as the *Dockerfile* to ensure only the needed files are copied into the container.

These practices promote security, efficiency, and clarity in Dockerfile development.

## Multi-Stage builds
Multi-stage builds in Docker are a feature that allows the user to create a Docker image using multiple build stages, each with its own set of instructions and dependencies. The user can selectively copy artifacts from one stage to another, leaving behind everything that's not needed in the final image.

Multi-stage builds are not applicable in this scenario as all artifacts created while building are needed in the final image. They would be useful if we were using a compiled language e.g. C++, Go. We could compile our code to build a binary file in one stage, and then copy over only the binary to the second stage.
