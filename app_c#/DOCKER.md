# Docker Best Practices

## Linter

I used [Hadolint](https://hadolint.github.io/hadolint/) linter to check Dockerfile

## Rootless user without specific UID

I created a user without root permissions and specific UID.

## Multi-Stage Build

For C# app I used multistage build: **build** and **runtime**.

I used it to minimize the size of the final image. The final image consist only of runtime files.

## Images

I used official lightweight python image based on alpine.

## Expose

I exposed only needed port - 80. I read that is normal for this port to be open.

## COPY

I used COPY instead of ADD according to [Dockerfile best practices](https://sysdig.com/blog/dockerfile-best-practices/)

## .dockerignore

I used .dockerignore to reduce image from useless files.

## WORKDIR

I used WORKDIR to setup working directory. Moreover, I used absolute paths.