![app_python badge](https://github.com/zRrrGet/core-course-labs/actions/workflows/app_python_ci.yaml/badge.svg)

# Python Web Application
## Overview
This web application displays Moscow time.
## Dependency installation
```
pip install -r requirements.txt
```
## Usage
You can run it on any ASGI server. For example, on `uvicorn`:
```
uvicorn main:app
```
## Unit Tests
```
python3 -m pytest test.py
```
## Docker
You can run app in docker to have an isolated container.
### Build
```
docker build -t zrrrget/app_python .
```
For test
```
docker build -t zrrrget/app_python_test --target test .
```
### Pull
```
docker pull zrrrget/app_python
```
```
docker pull zrrrget/app_python_test
```
### Run
Port 8000 is exposed.
```
docker run -p 8000:8000 zrrrget/app_python
```
```
docker run zrrrget/app_python_test
```
## CI
Crucial steps triggered on push:
- Run Snyk to check for vulnerabilities
- Lint python
- Run pytest
- Build test docker, test image and push
- Build production docker and push