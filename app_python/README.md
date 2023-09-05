# Innopolis University DevOps [F23] | Lab1

## Overview
The service provides information about current time in Europe/Moscow timezone.

## Build
To build the project you should have Python3 executable.
Install dependencies go to `./app_python` directory and run the following commands:
```shell
python3 -m venv env
source env/bin/activate
pip3 install --no-cache-dir -r requirements.txt
pre-commit install
```

## How to test?
In latest version of the project there are 3 properly documented tests.
To run tests go to the `./app_python` directory and run the following command:
```shell
pytest
```

## How to run?
1. Clone this repo.
2. Go to the `./app_python` directory of the cloned repo.
3. Run the following command:
    ```shell
    flask --app src/app run
    ```
4. Now the service can be used

## Usage
The server's URL is `http://127.0.0.1:5050/`.
Obtain the page from the browser or make a GET request from any HTTP client.
The resulting response is a text string with current Moscow time.

## Contact
* Author: Iskander Nafikov
* E-mail: i.nafikov@innopolis.university
