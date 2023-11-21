# Builder stage
ARG PYTHON_VERSION=3.9
ARG PYTHON_DISTROLESS_IMAGE=nzgeg3s0/python-distroless:3.9-debian11

FROM python:${PYTHON_VERSION}-slim-bullseye AS builder

WORKDIR /home/
COPY requirements.txt .

ARG VIRTUAL_ENV=/home/venv

RUN python -m venv ${VIRTUAL_ENV} && \
    ${VIRTUAL_ENV}/bin/python -m pip install --upgrade pip && \
    ${VIRTUAL_ENV}/bin/python -m pip install -r requirements.txt

# ------------------------------------------------------------------
# Application stage

# FROM ${PYTHON_DISTROLESS_IMAGE}
FROM python:3

ARG PYTHON_VERSION

COPY ./ /app/

RUN cd /app; pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app/src

ENTRYPOINT ["python", "run.py", "-b", "0.0.0.0:8000", "app:app"]
