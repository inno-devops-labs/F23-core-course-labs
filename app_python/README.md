# App for showing Moscow time

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install --no-cache-dir -r requirements.txt
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

## Contributing
Project are open to contributing, any forks are welcome.
For using my pre-commit hook run formatter/create-pre-commit-hook script

## Authors and acknowledgment
Eduard Zaripov - e.zaripov@innopolis.university