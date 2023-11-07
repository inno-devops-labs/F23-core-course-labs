![app_bash badge](https://github.com/zRrrGet/core-course-labs/actions/workflows/app_bash_ci.yaml/badge.svg)
# Bash Web Application
## Overview
This web application checks if the host is available(can be pinged) or not.
## Dependency installation
Nmap package is required, install it using your package manager(you would need `ncat` and `nmap`).
## Usage
First argument is target host, second is server port to listen.

Example:

```
./main.sh moodle.innopolis.university
```
## Unit Tests
```
./test.sh
```
## Docker
You can run app in docker to have an isolated container.
### Build
```
docker build -t zrrrget/app_bash .
```
For test
```
docker build -t zrrrget/app_bash_test --target test .
```
### Pull
```
docker pull zrrrget/app_bash
```
```
docker pull zrrrget/app_bash_test
```
### Run
Port 9000 is exposed.
```
docker run -p 9000:9000 zrrrget/app_bash
```
```
docker run zrrrget/app_bash_test
```
## CI
Crucial steps triggered on push:
- Lint bash using shellcheck
- Run test
- Build test docker, test image and push
- Build production docker and push
```
