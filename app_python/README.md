##About

Web app that shows current Moscow time

##Build

Create virtual environment and activate it

`python -m venv venv`

On Windows

`.\venv\Scripts\activate`

On Linux or macos

`source venv/bin/activate`

Install packages

`pip install -r ./requirements.txt`


##Run application

`uvicorn main:app`

Application is available at `127.0.0.1:8000`

##Test

`pytest ./test/test.py`