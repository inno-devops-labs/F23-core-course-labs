[![Python webserver](https://github.com/Chiplinka/core-course-labs/actions/workflows/app_python.yaml/badge.svg?branch=lab3)](https://github.com/Chiplinka/core-course-labs/actions/workflows/app_python.yaml)
[![Javascript webserver](https://github.com/Chiplinka/core-course-labs/actions/workflows/app_javascript.yaml/badge.svg?branch=lab3)](https://github.com/Chiplinka/core-course-labs/actions/workflows/app_javascript.yaml)

## Lab 1

I decided to use javascript because I have little experience using it. An interesting fact is that Javascript is the most popular programming language in the world and is in great demand among various organizations.

## Description
Web server which shows page with current time

## Run server 
```
node main.js
```

## Docker
### How to build?
```
docker build -t seakysneka1/webserv_js .
```
### How to pull?
```
docker pull seakysneka1/webserv_js:latest
```
### How to run?
```
docker run -p 5000:5000 seakysneka1/webserv_js
```

### Unit tests
I used mocha. Mocha is a popular and highly flexible JavaScript testing framework used for both browser and Node.js applications. It provides a simple and intuitive interface for writing and organizing test suites and test cases.

To run tests:
```
npx mocha tests/test_main.js
```

## CI workflow
- Build
    1. Setup node
    2. Install dependencies
    3. Lint code
    4. Snyk
- push_to_registry
    1. checkout the repo
    2. Log in to Docker Hub
    3. Extract metadata (tags, labels) for Docker
    4. Build and push Docker image