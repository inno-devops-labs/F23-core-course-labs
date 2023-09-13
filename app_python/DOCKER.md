## Best practices for creating docker image
1. `dockerignore` for excluding unneeded files is used
2. **Dockerfile linter:** I used linter to ensure quality. Linter used is [hadolint installed via docker image](https://hub.docker.com/r/hadolint/hadolint).
3. **Choosing the right base image**: for base image, official docker image for python is used, which is a safe common approach.
4. **Using COPY**: for transparency, COPY instead of ADD is used
5. **Non-root user:** To improve security, all commands are executed under a new, non-root user.