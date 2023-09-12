# Moscow Time Web App
## Description

Simple web app to fetch current time in Moscow.

## Pre-requirements

- Python 3.11
- Poetry

## Getting started

Install dependencies

```bash
poetry install
```

Run application

```bash
gunicorn main:app
```

## Miscellaneous

Run linter

```bash
ruff main.py
```

Run tests

```bash
pytest
```

## Docker

Build container

```bash
docker build -t docker.io/platun0v/devops-lab2 .
```

Run container

```bash
docker run -it --rm -p 8000:8000 docker.io/platun0v/devops-lab2 guincorn main:app -b 0.0.0.0:8000
```

Push container

```bash
docker push docker.io/platun0v/devops-lab2
```

Pull container

```bash
docker pull docker.io/platun0v/devops-lab2
```
