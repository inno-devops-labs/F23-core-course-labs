## Best practices for Dockerfile used:

- **Multi-stage build**: I've used the multi-stage build to separate the *pip wheel build process* and the final runtime environment. This helps to keep the final image size small and reduces the attack surface by only including necessary dependencies in the final image.

- **Exact dependencies versions**: In build stage I've specified exact versions for the packages installed using apk add. Also, all pip dependecies have exact versions. This ensures that the same versions of the packages are installed consistently across different environments, making the build process more reproducible.

- **Non-root user**: The Dockerfile creates a non-root user `timeapp` and sets it as the user to run the application. Running the application as a non-root user improves security.

- **Healthcheck**: Healthcheck command periodically checks the `/` path of the application to determine if the application is responding correctly. Healthchecks help to ensure that the application is running properly and will be used in future by container orchestration systems to determine the health of the container.

- **.dockerignore file**: The Dockerfile references a .dockerignore file, which specifies files and directories that should be excluded from the build context. This helps to reduce the build time and the size of the final image by excluding unnecessary files like `__pycache__` or `venv`.

- **Using variables**: The Dockerfile uses environment variables (`APP_PORT` and `APP_HOST`) to configure the application's port and host. This allows for flexibility in configuring the application without modifying the Dockerfile itself and less chance to make mistake in Dockerfile itself.
- **Dockerfile lint using pre-commit**: I've installed [Haskell Dockerfile Linter](https://github.com/hadolint/hadolint) to check Dockerfile.
