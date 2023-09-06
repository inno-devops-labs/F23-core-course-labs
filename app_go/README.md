# Godirector

> Simple https requests proxy which redirects user to the requested site.  

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python website")


## Features


- Configuration of the application is managed in the `config.py`
    - The following environmental variables can be changed
        - `CLOCK_TZ` - timezone to display. Shows Europe/Moscow by default.
        - `HOST` - host to listen. Defaulted to `0.0.0.0` to accept all requests. 
        - `FORMAT` - default format to display datetime in.

## Installation

```bash
# Install python3 using your distro's package manager
sudo apt update && sudo apt install python3 python3-pip python3-flask gunicorn

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Running the application

```bash
go run main.go
```

## Usage


```bash
https://<APP_HOST>/?q=<REDIRECT_URL>
```

- For example, in order to get redirect to the google

```
https://localhost:8000/?q=https://google.com
```

## Development

### Testing

- Tests can be invoked with go test command
```bash
go test
```


 
