# Time App

- Sample app that shows current time for DevOps course

## Used technology

- HTML, CSS, JS.
- Python (packages: Flask, Gunicorn).
- Docker (images: alpine, nginx).

## Endpoints

```bash
$ flask routes
Endpoint            Methods  Rule
------------------  -------  -----------------------
home                GET      /
```

## Development

`python` and `pip` are used, make sure you have them installed and available in `$PATH` then execute the following:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py

development# or
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Unit Tests

Unit tests are found on the [tests directory](./tests). To run:

```bash
python -m pytest
```

## Release

```bash
export DOCKERHUB_ID=<YOUR_DOCKERHUB_ID>
export APP_NAME=app_python

# To build app image
docker build -t $DOCKERHUB_ID/$APP_NAME .

# Testing the built image locally (http://localhost:8080)
docker run -p5000:5000 $DOCKERHUB_ID/$APP_NAME

# Tag image with last commit SHA (and/or use semantic versioning)
docker tag $DOCKERHUB_ID/$APP_NAME $DOCKERHUB_ID/$APP_NAME:$(git rev-parse --short HEAD)

# Login and push image to dockerhub
docker login -u $DOCKERHUB_ID # Enter password/token when prompted
docker push $DOCKERHUB_ID/$APP_NAME --all-tags
```

## CI

- The workflow is done using Github actions
- The workflow includes:
  - buulding, testing and linting job
  - building and deploying image on dockerhub
  - checking security valnurabilities with Synk
- The workflow uses ubuntu as a base for every job
