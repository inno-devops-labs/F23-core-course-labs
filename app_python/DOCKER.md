# Docker Best Practices

## Linter

I used [Hadolint](https://hadolint.github.io/hadolint/) linter to check Dockerfile

## Rootless user without specific UID

I created a user without root permissions and specific UID.

## Multi-Stage Build

For python app I used multistage build: **prepare** and **runtime**.

I used it to logically separate runtime from prepare state.

## Images

I used official lightweight python image based on alpine.

## Expose

I exposed only needed port

## COPY

I used COPY instead of ADD according to [Dockerfile best practices](https://sysdig.com/blog/dockerfile-best-practices/)

## .dockerignore

I used .dockerignore to reduce image from useless files.

## WORKDIR

I used WORKDIR to setup working directory. Moreover, I used absolute paths.