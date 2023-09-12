# Best practices for dockerizing application

## .dockerignore

I used a .dockerignore file, so that only necessary files are included in the Docker image.

## Linting

To ensure following best practices I used [hadolint](https://github.com/hadolint/hadolint) linter to check for any issues.

## COPY and RUN

I used COPY instead of ADD, also I used small RUN commands to reduce the number of layers.

## Official base image

I used the official Docker image of Node with LTS version 20 which is maintained and safe.

## Non-root user

I created a non-root user and ran all commands under that user. This reduces the attack surface and improves security.

## Expose only necessary ports

I exposed only the necessary port (port 5173) for the svelte application. This reduces the attack surface and improves security.

## Use of multi-stage builds

I used multi-stage builds to reduce the size of the image. The build process is done in the first stage and the final image is copied from the first stage.

By using multi-stage builds, the final production image only contains the necessary build output, ensuring a smaller and more efficient deployment.
