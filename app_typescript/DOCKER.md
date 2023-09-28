# Docker

## Dockerfile Best Practices

This document outlines best practices observed in the given Dockerfile.

### Base Image Selection

- Using the official Node base image from *Dockerhub* as well as specifying node version to ensure compatibility with the Vite app.

### Create a Non-Root User

- The Dockerfile creates a non-root user named "newuser" with the `-D` flag, which ensures that the user won't have a password set, enhancing security.

### COPY instead of ADD

- The `COPY` instruction is used to copy the current directory (represented by `.`) into the container.

### Use the USER Instruction

- After creating the non-root user, the `USER` instruction switches to using the "newuser" account. This limits the container's privileges, which is a security best practice.

### Expose Ports Explicitly

- The `EXPOSE` instruction is used to indicate which port the container will be listening on.

### Use an Entry Point

- The `ENTRYPOINT` instruction specifies the command to run when the container starts. In this case, it runs the dev server of the app. Using an entry point is a good practice for defining the container's primary executable and preventing the user from overriding.

### RUN in a single layer

- Even though in this scenario only on command was necessary to prepare the image, it is present under a single `RUN` command to ensure layer sanity. If multiple commands were needed, they would have simply been grouped by `&&` under a single `RUN` command.

### .dockerignore

- A *.dockerignore* file is present in the same directory as the *Dockerfile* to ensure only the needed files are copied into the container.

These practices promote security, efficiency, and clarity in Dockerfile development.

## Multi-Stage builds
Multi-stage builds in Docker are a feature that allows the user to create a Docker image using multiple build stages, each with its own set of instructions and dependencies. The user can selectively copy artifacts from one stage to another, leaving behind everything that's not needed in the final image.

Multi-stage builds are not applicable in this scenario as all artifacts created while building are needed in the final image. They would be useful if we were using a compiled language e.g. C++, Go. We could compile our code to build a binary file in one stage, and then copy over only the binary to the second stage.
