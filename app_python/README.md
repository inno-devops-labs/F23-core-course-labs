# Web application for getting current Moscow time 
Application written in `aiohttp` Python framework:
`src/` - folder with source files
`app.py` - entry point of application
`time_provider.py` - service for getting current time
`http_wrapper.py` - service for http wrapping of content for beautriful output

# Getting started
```
cd app_python
```

## Poetry installation
```
curl -sSL https://install.python-poetry.org | python3 -
```

## Install dependencies
```
poetry install
```

If previous commands don't work, just use
```
pip install aiohttp pytz 
```

# Run Application
```
python src/app.py
```

# Check the result
Open URL in browser
`http://localhost:8080/`

# Unit tests
`/test` - unit tests
`pytest` - use for testing

# Docker

## Pull
```bash
docker pull vlasovegorl/devops-python-app:latest
```

## Build
```bash
docker build -t vlasovegorl/devops-python-app:latest .
```

## Run
```bash
docker run -p 8000:8000 -it vlasovegorl/devops-python-app:latest
```
Application will be available on port 8000