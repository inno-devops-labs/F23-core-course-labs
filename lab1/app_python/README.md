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
## Usage:
Start app:\
    ```
    python3 -m app_python 
    ```

Now you can go to `http://127.0.0.1:8080/` and `http://127.0.0.1:8080/time` to test app.

If you used another variables in `.env` file, refer to `http://<SERVER_HOST>:<SERVER_PORT>/`.



