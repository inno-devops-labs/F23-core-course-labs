# Lab 1
## Description 
Web app which displays current Moscow time

## Framework 
In this project FastApi framework is used

Start server:
```
uvicorn src.main:app --reload
```

## Docker
### How to build?
```
docker build -t seakysneka1/webserv_python .
```
### How to pull?
```
docker pull seakysneka1/webserv_python:latest
```
### How to run?
```
docker run -p 8000:8000 seakysneka1/webserv_python
```

## Unit Tests
For testing I used **pytest** framework:

Tests:
- Check that time is updating
- Check responce code
- Check String matching
```
python3 -m pytest test_main.py
```

## CI workflow
CI stages:
- Build
    1. Set up Python 3.11
    2. Cache dependencies
    3. Install dependencies
    4. Linter
    5. Tests
- snyk 
    1. Checkout
    2. Run snyk
- push_to_registry
    1. Check out the repo
    2. Log in to Docker Hub
    3. Extract metadata (tags, labels) for Docker
    4. Build and push Docker image

## CI best Practices
1. Github action trigering: The workflow initiates in response to 'push' events occurring within the repository. Utilizing the 'paths' attribute, the workflow is specifically instructed to activate only when changes are pushed to the CI configuration file ('.github/workflows/app_python.yaml') or any files except *.md within the 'app_python/'  directory.
2. Snyk Security Check Job: This particular job is dedicated to enhancing security by conducting a thorough examination of potential vulnerabilities within the Python dependencies.
3. Handling Secrets: GitHub's secret storage is employed for the secure management of confidential information.
4. Cashing
5. Defaults Configuration: It establishes 'bash' as the default shell and promote consistency throughout the execution of various steps.





