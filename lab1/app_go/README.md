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
## Usage:
Build app:
```
 go build -o app_go  
```
Run app:
```
 ./app_go
 ```


Now you can go to `http://127.0.0.1:8081/` and `http://127.0.0.1:8081/joke` to test app.

If you used another variables in `.env` file, refer to `http://<SERVER_HOST>:<SERVER_PORT>/`.



