# Python Time App

## Description

This app is a web service to get time in Moscow.

## Software Requirements
* Python 3.11+

## Dependencies

* Refer to `requirements.txt` for Python dependencies.

## Setup
```
pip3 install -r requirements.txt
```

## Usage 

```
python3 app_main.py <port to listen>
```

You can check the time endpoint at `http://localhost:<port>/time`

## QA

* `make lint` for linting (requires `flake8` to be installed) 
* `make test` for testing (requires `pytest`)