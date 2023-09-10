# Python App

This app shows the current Moscow time in ISO format

## Setup
```
pip install fastapi
pip install "uvicorn[standard]"
```

## Run
Use `app_python.main` to run the project from the root, or just `main` if you're in the `app_python` directory
```
uvicorn app_python.main:app --reload
```

## Test
Run this in the `app_python` directory
```
pip install httpx
pip install pytest
pytest
```

## Docker
This app is containerized via Docker

### Build
```
docker build -t image_name .   
```

### Pull
```
docker pull xdkomel/myimage:0.0.1
```

### Run
```
docker run -d --name container_name -p 80:80 image_name
```