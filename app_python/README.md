# Time-app

Time-app is a Python web application that displays the current time in Moscow.

## Installation
### Getting started
1. Setup a Python virtual environment
2. Install dependencies
3. Run the application

### Setup virtual environment
```
python -m venv venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements-base.txt
```

### Run
```
uvicorn app.main:app
```
Now you can open `http://127.0.0.1:8000/` in your browser to check the time. Also you can check documentation at `/docs` path.

### Development
For development, install additional dependencies:
```
pip install -r requirements-dev.txt
```
Run this command to set up the git hook scripts:
```
pre-commit install
```

Run the app:
```
python dev.py
```
Run tests:
```
pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
