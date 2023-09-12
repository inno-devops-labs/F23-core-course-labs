# Go Chuck Norris Jokes Web App

## Description
This is a simple go web app to display Chuck Norris jokes.

## Requirements
Go 1.19

## Set up:
1. Install requirements:
    ```
   go install github.com/joho/godotenv/cmd/godotenv@latest
    ```
2. Create `.env` file with the following content (or you can change parameters):
   ```
    SERVER_HOST=127.0.0.1
    SERVER_PORT=8081
    ```
## Start app:
Build app:
```
 go build -o app_go  
```
Run app:
```
 ./app_go
 ```
## Docker:
### How to build?
1. Create `.env` file with the following content:
   ```
    SERVER_HOST=0.0.0.0
    SERVER_PORT=8081
    ```
2. Run command
   ```
   docker build -t app_go:latest .
   ```
### How to pull?
```
   docker pull lnsfna/app_go
   ```
### How to run?
* If built locally:
  ```
   docker run -d -p 8081:8081 --name app_go app_go:latest
   ```
* If pulled from DockerHub:
```
   docker run -d -p 8081:8081 --name app_go lnsfna/app_go:latest
   ```
## Usage:
Now you can go to `http://127.0.0.1:8081/` and `http://127.0.0.1:8081/joke` to test app.



