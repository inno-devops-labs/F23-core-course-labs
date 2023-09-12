# Docker

This is a document dedicated to everything about the docker image(s)

## Building docker image

```
cd app_python
docker built -t app_python
```

## Running docker image

```
docker run -p 5000:5000 --rm app_python
```