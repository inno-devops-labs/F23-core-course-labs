![workflow](https://github.com/TeaWhyDee/DOE-course-labs/actions/workflows/github-actions.yml/badge.svg)

# The app

The is a simple web application built with Flask and guicorn as HTTP server.\
It has two endpoints:

* `/ ` : Displays the current time in Moscow.
* `/visits ` : Displays the count of visits of the root endpoint.

## Running the app

1. Clone the repo, and cd into the "app\_python" directory.

2. install requirements:

   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application (it uses guicorn):

   ```
   python run.py -b 0.0.0.0:8000 app:app
   ```

## Unit Tests

Run tests:

```
python -m unittest tests.test
```

## Docker

Pull and run the Docker container:

```bash
docker pull nzgeg3s0/doe-lab2
docker run --cap-drop=all -p 8000:8000 nzgeg3s0/doe-lab2
```

Or build the image yourself:

```bash
docker build --build-arg=PYTHON_VERSION=3.9 -t doe-lab2 .
```

Take note of PYTHON\_DISTROLESS\_IMAGE environment variable, you can substitute it for your own base image.
To build the base image (Dockerfile is in `python-distroless` folder) you can use this command:

```bash
docker build --build-arg=PYTHON_BUILDER_IMAGE=al3xos/python-builder:3.9-debian11 --build-arg=GOOGLE_DISTROLESS_BASE_IMAGE=gcr.io/distroless/cc -t python-distroless:3.9-debian11 .
```

## Docker Compose

Run the app using Docker Compose:

```bash
docker compose up
```

## CI

To run the pipeline, the following secrets need to be specified:

* **DOCKER\_IMAGE** - DockerHub image path like \<user>/\<package>.
* **DOCKER\_PASSWORD** - DockerHub password (or token).
* **DOCKER\_USERNAME** - DockerHub username.
* **SNYK\_TOKEN** - Snyk token.

The GitHub Actions pipeline is as follows:

1. Check for volnerabilities in the dependencies using Snyk.
2. Run unit tests.
3. If the furst two jobs are sucessfull, build and publish the Docker image.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

* The Flask web framework: [Flask](https://flask.palletsprojects.com/)
* The Pytz library for timezone support: [Pytz](https://pythonhosted.org/pytz/)
