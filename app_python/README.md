# Lab 1
## Description 
Web app which displays current Moscow time

## Framework 
In this project FastApi framework is used

Start server:
```
uvicorn main:app --reload
```

## Testing:
For testing I used **pytest** framework:

```
python3 -m pytest test_main.py
```

## Docker
### How to build?
```
docker build -t seakysneka1/webserv_python .
```
### How to pull?
```
docker pull seakysneka1/webserv_python:latest
```
### How to run?
```
docker run -p 8000:8000 seakysneka1/webserv_python
```