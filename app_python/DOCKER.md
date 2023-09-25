# Docker Best Practises

## Run as non-root user

Running the containerized application with non-privileged user accounts.

```dockerfile
RUN adduser -D localuser && chown -R localuser /app
USER localuser
```

## Use distroless images

Distroless are minimalistic container images that contain only the application
and its dependencies, reducing the attack surface and potential vulnerabilities.

```dockerfile
FROM gcr.io/distroless/python3
```

Example: https://github.com/GoogleContainerTools/distroless/blob/main/experimental/python3/README.md

## Multistage builds

As I've decided to use distroless image, I have to use multistage build 
for package collection. First images (alpine) uses `pip` to install all dependencies,
and distroless just copies built dependencies and just runs the application.

```dockerfile
FROM python:3.11-alpine AS build-env
...
FROM gcr.io/distroless/python3
COPY --from=build-env /app /app_python
COPY --from=build-env /home/localuser/.local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
```

Source: https://github.com/GoogleContainerTools/distroless/issues/171

## Exclude with .dockerignore

I use .dockerignore file to exclude unnecessary files such as *.md, venv, etc.

## Minimize the number of layers

As each command creates new layer of the image, so I've decided to use multi-line commands.

```dockerfile
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements/prod.txt
```

## Leverage build cache

Docker looks for an existing image in its cache, rather than creating a new, duplicate image.

```shell
docker build -t app_python --no-cache  .
```

## Linter

I used the following [linter](https://github.com/hadolint/hadolint) to make sure
my Dockerfile uses best practises.

```shell
docker run --rm -i ghcr.io/hadolint/hadolint < Dockerfile
```