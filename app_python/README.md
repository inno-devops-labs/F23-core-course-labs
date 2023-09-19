# Moscow Time Fetcher
![python-app workflo badge](https://github.com/kinjalik/core-course-labs/actions/workflows/python-app.yaml/badge.svg)

This application is a UNIX-way inspired service which fetch current time in Moscow.

## Getting started
1. Install Python 3.8 or higher
2. Install required dependencies
```bash
python -m pip install -r requirements.txt
```
3. Run the application
```bash
uvicorn main:app
```

## Miscellaneous
### Run linter
```bash
python -m pylint main.py
```

### Run unit tests
```bash
export PYTHONPATH=`pwd`/src
pytest src
```

## Troubleshooting
### I use Arch btw. How to install deps?
```bash
pacman -S uvicorn python-starlette
```

## Docker
### Build
```bash
docker build -t kinjalik/devops-course-app:python .
```

### Pull
```bash
docker pull kinjalik/devops-course-app:python
```

### Run
```bash
docker run -p 8000:8000 -it kinjalik/devops-course-app:python
```
Application will be available on port 8000

## CI
Primary CI workflow it `python-app.yaml` which performs:
- Lint check (HTML report is provided as artifact)
- Unit Test run (JUnit report is provided as arifact, it has pretty print in Summary of Action)
- Snyk security check (report uploaded to GitHub, so if any issue it will be shown)
- Publicatin to Dockerhub