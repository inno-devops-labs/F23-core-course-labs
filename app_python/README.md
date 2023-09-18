## Functionality
This app shows current moscow time. When you refresh the page, time is also updated.
to run

## How to run
! you need docker to run this application

Execute following commands:
1. `docker build -t imagename .`
2. `docker run -d --name containername -p 80:80 imagename`

## How to push image to docker hub
1. `docker login`
2. `docker push username/repository_name`

## Unit Tests
`pytest` is used for testing.

There is one unit test in `src/test_main.py`

To run it type `pytest`
