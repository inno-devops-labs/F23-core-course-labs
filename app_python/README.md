# Moscow Time Web App

## Description
Web app which show current Moscow time.\
DevOps course, Innopolis University

## Start
### Pre-install
- `Python 3.9`
- `flask` library - framework
- `pytz` library - for getting Moscow time
- `Docker`

### Run from terminal
`python app.py`

### Run using Docker
- Build: 
    `docker build -t python-moscow-time .`
- Push: 
    `docker tag python-moscow-time annadluzhinskaya/python-moscow-time:latest`
    `docker push annadluzhinskaya/python-moscow-time:latest`
- Pull: 
    `docker pull annadluzhinskaya/python-moscow-time:latest`
- Run:
    `docker run -p 8000:8080 annadluzhinskaya/python-moscow-time:latest`

## Project structure

```text
app_python/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│    └── time_tests.py
├── app.py
├── DOCKER.md
├── Dockerfile
├── PYTHON.md
├── README.md
└── requirements.txt
```
