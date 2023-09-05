# Innopolis University DevOps [F23] | Lab1 Bonus

## Overview
The service provides information about current time in Europe/Moscow timezone.

## Build
To run the application go to the `./app_kotlin` directory and run the following command:
```shell
./gradlew boot
```

## How to test?
In latest version of the project there are 2 tests.
To run tests go to the `./app_kotlin` directory and run the following command:
```shell
./gradlew test
```

## How to run?
1. Clone this repo.
2. Go to the `./app_kotlin` directory of the cloned repo.
3. Run the following command:
    ```shell
    ./gradlew bootRun
    ```
4. Now the service can be used

## Usage
The server's URL is `http://127.0.0.1:8080/`.
Obtain the page from the browser or make a GET request from any HTTP client.
The resulting response is a text string with current Moscow time.

## Contact
* Author: Iskander Nafikov
* E-mail: i.nafikov@innopolis.university
