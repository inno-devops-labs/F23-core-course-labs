# Python Time App

## Description

This app is a web service to get time in Moscow.

## Software Requirements
* Python 3.11+

## Dependencies

* Refer to `requirements.txt` for Python dependencies.

## Setup
```
pip3 install -r requirements.txt
```

## Usage 

```
python3 app_main.py <port to listen>
```

You can check the time endpoint at `http://localhost:<port>/time`

## Docker
You can use dockerized version of the app.
### Build
To build your own container, 
```
make docker tag=<your tag>
```
If no tag specified, tag `latest` is used.
### Pull
You can pull my own [container builds](https://hub.docker.com/u/ar7ch) from `ar7ch/devops_lab2_app_python`:
```
make docker-pull
```

### Run
`make docker-run` will start the container listening on port 8080 on host side.
Alternatively,
```
docker run <other options> -it -p <your port>:80 ar7ch/devops_lab2_app_python
```

### Docker QA
```
make docker-lint
make docker-check
```

## QA

* `make lint` for linting (requires `flake8` to be installed) 
* `make test` for testing (requires `pytest`)