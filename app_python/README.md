# Simple web application

This is a simple web application on flask. It displays current date and time in Moscow.

## Installation and Usage

Clone the repository

```
git clone https://github.com/JustSomeDude2001/core-course-labs
```

Navigate to the project directory

```
cd ./core-course-labs/app_python
```

Install the requirements

```
pip install -r requirements.txt
```

Run the app


```
python3 app.py
```

Afterwards, the date and time can be seen on `127.0.0.1:5000`

## Testing

After installing the application, go to the directory and run tests package using `pytest`

```
python3 -m pytest
```

Note that if your ping is higher than 2 minutes (which is highly unlikely) tests will always fail.