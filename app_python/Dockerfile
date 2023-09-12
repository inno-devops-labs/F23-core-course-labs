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

FROM ${PYTHON_DISTROLESS_IMAGE}

ARG PYTHON_VERSION

COPY ./src /app/
COPY --from=builder /home/venv /home/venv

ENV PYTHONPATH=/home/venv/lib/python${PYTHON_VERSION}/site-packages

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["python", "run.py", "-b", "0.0.0.0:8000", "app:app"]
