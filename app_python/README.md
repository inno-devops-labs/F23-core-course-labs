##About

Web app that shows current Moscow time
Displays the number of visits using /visits endpoint

##Build

Create virtual environment and activate it

`python -m venv venv`

On Windows

`.\venv\Scripts\activate`

On Linux or macos

`source venv/bin/activate`

Install packages

`pip install -r ./requirements.txt`


##Run application

`uvicorn main:app`

Application is available at `127.0.0.1:8000`

##Unit Tests

`pytest ./test/test.py`

#Docker

## Build

`docker build -t wareverdud/lab2 .`

###Or

## Pull

`docker pull wareverdud/lab2`

## Run

`docker run -p 8000:8000 wareverdud/lab2`

Application is available at `http://127.0.0.1:8000/`

## CI

CI pipeline has 4 stages:

1. Lint the code
2. Test the code
3. Check possible snyk vulnerabilities
4. Build docker image and push it to the docker hub