# Python Moscow time Web App

## Description 
This is a simple python web app to display current time in Moscow.

## Requirements 
Python 3.9

## Set up:
1. Install requirements: 
    ```
    pip3 install -r requirements.txt
    ```
2. Create `.env` file with the following content (or you can change parameters):
   ```
    SERVER_HOST=127.0.0.1
    SERVER_PORT=8080
    ```
## Start app:
```
python3 -m app_python 
```

## Docker:
### How to build?
1. Create `.env` file with the following content:
   ```
    SERVER_HOST=0.0.0.0
    SERVER_PORT=8080
    ```
2. Run command
   ```
   docker build -t app_python:latest .
   ```
### How to pull?
```
   docker pull lnsfna/app_python
   ```
### How to run?
* If built locally:
  ```
   docker run -d -p 8080:8080 --name app_python app_python:latest
   ```
* If pulled from DockerHub:
```
   docker run -d -p 8080:8080 --name app_python lnsfna/app_python:latest
   ```
## Usage:

Now you can go to `http://127.0.0.1:8080/` and `http://127.0.0.1:8080/time` to test app.



