# Dockerfile details

This Dockerfile creates a Docker image for a Go application using multi-stage builds and following industry-standard Docker best practices.

## Docker Best Practices

1. **Multi-stage builds**: By using multi-stage builds, this `Dockerfile` separates the build stage from the final release stage. This approach helps minimize the size of the final Docker image by including only the necessary files and dependencies.

3. **WORKDIR in the build stage**: The `WORKDIR` instruction sets the working directory to `/app` for the build stage, keeping application files separate from system files and allowing the container to work within the appropriate context.

4. **COPY and testing**: The `COPY` instruction copies application files into the `/app` directory. Then, the `go test` command runs tests on the `/app/internals/handlers` package, ensuring the application passes tests before proceeding to the next stage.

5. **Building the application**: The `go build` command compiles the Go application into an executable binary named `main`, which will be copied to the final stage.

6. **Lightweight base image**: The base image used for the build and the final stage is `alpine`, a lightweight Alpine Linux-based image. Choosing this image reduces the overall size of the final Docker image.

7. **Non-root user**: The `adduser` command creates a new user named `appuser` with user `ID 1000` and adds the user to the `users` group. Running the application with a non-root user is a security best practice, as it minimizes the potential attack surface in case of a vulnerability.

8. **WORKDIR and USER in the release stage**: The `WORKDIR` instruction sets the working directory to `/app` for the final stage. The `USER` instruction switches the current user to appuser, ensuring the application will run as a non-root user.

9. **Copying the built application**: The `COPY` instruction, with the `--from=build` flag, copies the compiled Go binary named main from the build stage to the final stage. The `--chown=appuser:users` flag sets the ownership of the copied binary to the non-root user and the `users` group.

10. **EXPOSE**: The `EXPOSE` instruction declares the port (`8080`) the application listens on, making it easier for other developers and tools to know which port to bind.

11. **CMD**: The `CMD` instruction provides a default executable command for the container, launching the Go application using the `/app/main` binary.

By implementing these Docker best practices, the resulting Docker image is lightweight, secure, and efficiently built.