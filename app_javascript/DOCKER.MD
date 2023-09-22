# Best Practices for Dockerizing a React App

## Linting

To ensure that my Dockerfile follows best practices, I used [Hadolint](https://github.com/hadolint/hadolint) linter to check for any issues.

## Non-root user

I created a non-root user and ran all commands under that user. This reduces the attack surface and improves security.

## .dockerignore

I used a .dockerignore file to reduce the build context. This ensures that only necessary files are included in the Docker image.

## COPY vs ADD

As recommended by Docker, I used COPY instead of ADD to copy files into the container.

## Multi-stage build

I used a multi-stage build to minimize the size of the final image. This involves using two separate Docker images: one for building the application and another for running it. This reduces the size of the final image and improves performance.

## Specific Node.js version

I used a specific Node.js version (node:20-alpine) instead of the latest to ensure consistency. This ensures that my application runs on a known and stable version of Node.js.

## Expose only necessary ports

I exposed only the necessary port (port 80) for the Nginx server. Additionally, I removed the default Nginx configuration file to avoid conflicts with our own configuration.

By following these best practices, I can ensure that my Docker image is secure, efficient, and easy to maintain.
