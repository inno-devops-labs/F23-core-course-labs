# Application to display current time in Moscow

### Description
Application was written in python using [falcon framework](https://falconframework.org/). It uses python standard library to retrieve current time in UTC+3 timezone, and it's only 10 lines of code.

### Collecting dependencies
`$ pip install -r requirements.txt`

### Running
`$ python3 -m gunicorn app:app`
