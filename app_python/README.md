# Pywatch

Pywatch is a simple python web application that displays the current time in Moscow.

## Installation

Install the dependencies using [pip](https://pip.pypa.io/en/stable/).

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m uvicorn main:app
```

You should see output like this:

```bash
INFO:     Started server process [55990]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Then you can check the time in Moscow by visiting `http://127.0.0.1:8000`:

```bash
curl http://127.0.0.1:8000 # "2023-09-05T23:25:40.902380+03:00"
```

## Docker

### Build image

```bash
docker build -t sl1depengwyn/python_devops .
```

### Or pull

```bash
docker pull sl1depengwyn/python_devops
```

### Run image

```bash
docker run -p 80:80 sl1depengwyn/python_devops
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

To run the tests:

```bash
pytest
```
