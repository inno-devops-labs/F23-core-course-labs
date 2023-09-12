# Docker

This is a document dedicated to everything about the docker image(s)

## Building docker image

```
cd app_python
docker built -t app_python
```

## Running latest docker image

```
docker run -p 5000:5000 --rm justsomedude22/app_python:latest
```

## How to push

```
docker push justsomedude/app_python:<tag>
```

## How to add a tag

```
docker tag app_python justsomedude22/app_python:<tag>
```

## How to pull

```
docker pull justsomedude22/app_python:<tag>
```