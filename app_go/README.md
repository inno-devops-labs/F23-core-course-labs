# Godirector

> Simple https requests proxy which redirects user to the requested site.  

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python website")


## Features


- The following environmental variables can be changed to configure the application
    - `PORT` - port to listen. Defaulted to `8080`. 
    - `DEFAULT_REDIRECT_URL` - fallback redirect URL which will be used in case if the client has not provided the `q` parameter.

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
go test  ./... -v
```


## Docker

- How to build? 
    - `docker build -t app_go .`
- How to pull? 
    - `docker pull 0x22d1ab/app_go`
- How to run?  
    - `docker run --rm -it -p 8080:8080 --name app_go app_python 0x22d1ab/app_go `