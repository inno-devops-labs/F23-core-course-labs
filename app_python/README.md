# App showing Moscow time

## Docker

### Build

```
docker build . -t dvechtomova/app_python:latest
podman build . -t dvechtomova/app_python:latest
```

### Pull

```
docker pull dvechtomova/app_python:latest
podman pull dvechtomova/app_python:latest
```

### Run

```
docker run --rm -it -p 8080:8080 dvechtomova/app_python:latest
podman run --rm -it -p 8080:8080 dvechtomova/app_python:latest
```

## Test

```
poetry run python -m pytest
```
