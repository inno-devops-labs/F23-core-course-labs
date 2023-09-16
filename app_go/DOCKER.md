## Best practices for Dockerfile used:

- **Multi-stage build**: I've used the multi-stage build to separate the *go build* and the final runtime environment. This allowed to use scratch image in runtime. Multi-stage helps to keep the final image size small and reduces the attack surface by only including necessary dependencies in the final image.

- **Exact dependencies versions**: In build stage I've specified exact versions for the packages installed using apk add (package `tzdata`). This ensures that the same versions of the packages are installed consistently across different environments, making the build process more reproducible.

- **Non-root user**: The Dockerfile creates a non-root user `timeapp` and sets it as the user to run the application. Running the application as a non-root user improves security.

- **.dockerignore file**: The Dockerfile references a .dockerignore file, which specifies files and directories that should be excluded from the build context. This helps to reduce the build time and the size of the final image by excluding unnecessary files like old builds and files included in gitignore.

- **Using variables**: The Dockerfile uses environment variable (`APP_PORT`) to configure the application's port. This allows for flexibility in configuring the application without modifying the Dockerfile itself and less chance to make mistake in Dockerfile itself.

- **Dockerfile lint using pre-commit**: I've installed [Haskell Dockerfile Linter](https://github.com/hadolint/hadolint) to check Dockerfile.
