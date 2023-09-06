# Unpyclock
> Simple Flask application which displays current time in the Moscow 


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

- In order to start the application in debug, you can run
```bash
flask run
```

- In the production you have to use suitable web server, for example gunicorn
```bash
cd ../ && gunicorn --bind 0.0.0.0:8000 app_python.wsgi:app && cd -
```

## Usage

- ![](assets/2023-09-06-09-33-50.png)


## Development

### Testing



- In order to run tests for this application, you can can invoke pytest (assuming that you have dependencies from the `requirements.txt` installed)
```bash
python3 -m pytest
```
