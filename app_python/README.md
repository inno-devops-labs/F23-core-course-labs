# App for showing Moscow time

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install --no-cache-dir -r ./requirements/requirements-dev.txt
```

## Run

```bash
uvicorn src.main:app --port 8085
```
App will start at 8085 port

## Test
```bash
pytest .
```

## Docker
To build docker image:
```bash
docker build --tag edikgoose/moscow-time-app:1.0.0 .
```

To pull docker image:
```bash
docker pull edikgoose/moscow-time-app:1.0.0
```

To run docker image:
```bash
docker run -p 80:80 --name moscow-time-app edikgoose/moscow-time-app:1.0.0
```

## Contributing
Project are open to contributing, any forks are welcome.
For using my pre-commit hook run formatter/create-pre-commit-hook script

## Authors and acknowledgment
Eduard Zaripov - e.zaripov@innopolis.university