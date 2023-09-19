## How it works

1. After GET request on '/' server sends an html document where moscow time is already displayed
2. html document sends request for css file, and server responses to this request
3. If user tries to enter some url which is different from '/', he gets 404 HTTP status and application redirects user to '/'
4. For creating the html document application uses Jinja2 templating engine
3. Moscow time is calculated based on fact that time offset in Moscow is UTC+3

## Docker usage
    - build image locally: `cd app_python` then `docker build --tag app_python .`
    - run: `docker run -p 5555:5555 app_python` if you built image locally. In order to run image loaded from dockerhub use `docker run -p 5555:5555 linkstaple/app_python`. The application is available on 127.0.0.1:5555
    - pull image: `docker image pull linkstaple/app_python`

## CI workflow information
CI contains setting up for python v3.11, dependencies installation, linting (with `ruff` linter), testing. In the end the workflow builds in image using docker and pushes it to docker hub. The latest image from push can be found in dockerhub: `linkstaple/app_python_ci:latest`

## Unit Tests
unit tests are executed using pytest, which is getting installed during the workflow