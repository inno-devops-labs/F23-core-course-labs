# App showing Moscow time

## Build

```
pip install --no-cache-dir "poetry~=1.2.0"
poetry install --no-cache --no-interaction
poetry export -f requirements.txt > requirements.txt
pip install --no-cache-dir -r requirements.txt
```

## Run

```
gunicorn -k uvicorn.workers.UvicornWorker -w 4 --bind 0.0.0.0:8080 app:app
```

## Test

```
poetry run python -m pytest
```
