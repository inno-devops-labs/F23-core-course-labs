# Python Time App

## Setup
```
pip3 install -r requirements.txt
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
You can pull my own [container builds](https://hub.docker.com/u/ar7ch) from `ar7ch/devops_lab3_app_python`:
```
make docker-pull
```

### Run
`make docker-run` will start the container listening on port 8080 on host side.
Alternatively,
```
docker run <other options> -it -p <your port>:80 ar7ch/devops_lab3_app_python
```

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

* `make lint` for linting (requires `flake8` to be installed) 
* `make test` for testing (requires `pytest`)

## CI
Information about CI pipeline workflow
* Workflow is defined in `.github/workflows/app_python.yml`;
* It runs on every push to `lab3` branch and on every pull request to `main` branch;
* It performs linting and testing;
* It performs scanning for vulnerabilities using Snyk;
* If linting, testing, and security jobs succeed, it builds docker image and pushes it to Docker Hub on every push to `main` branch.