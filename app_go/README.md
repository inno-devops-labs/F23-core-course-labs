# Go Time App

![Go app status](https://github.com/ar7ch/core-course-labs/actions/workflows/.github/workflows/app_go.yml/badge.svg?branch=lab3)

## Description

This app is a web service to get time in Innopolis.

## Software requirements
* Go 1.20

## Build
Creates a `goapp` binary in project root:
```
make build
```

## Usage
```
./goapp <port>
```

Go to `http://localhost:<port>/time` to get time.

## Persistent Data

This app counts the amount of requests for `/time` endpoint. You can get the amount of requests by accessing `/visits` endpoint. The counter is stored at `/appdata/visits.txt` file, where `/appdata` is a Docker volume.

## Docker
You can use dockerized version of the app.
### Build
To build your own container, 
```
make docker tag=<your tag>
```
If no tag specified, tag `latest` is used.
### Pull
You can pull my own [container builds](https://hub.docker.com/u/ar7ch/devops_lab2_app_go/general) from `ar7ch/devops_lab2_app_go`:
```
make docker-pull
```
### Run
`make docker-run` will start the container listening on port 8080 on host side.
Alternatively,
```
docker run <other options> -it -p <your port>:80 ar7ch/devops_lab2_app_go 
```
You can change the port app is listening within the container (from 80 to something) using `GOAPP_PORT` environment variable.

### Docker QA
```
make docker-lint
make docker-check
```

## QA
### Unit Tests

```
make unit-tests
```

