# Python Web Application

## Overview

This is simple Python web application, that shows current time in Moscow

## Requirements

Before usage, you should install packages listed in requirements.txt file. To install all the dependencies, execute
the command below.

 ```
 pip3 install -r requirements.txt
 ```

## Build

There is Makefile in the project.
 ```
 # Run linters
 make lint 
 
 # Run formatters
 make format
 
 # Run app
 make run
 ```

## Usage
To get current moscow time run `curl 127.0.0.1:8000` or enter `127.0.0.1:8000` in any browser.

## Contact

Telegram: @art22m