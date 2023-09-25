# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster as build

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py /app
COPY templates/ /app/templates

FROM python:3.7-slim

ENV APP_USER=myuser

# Create user and provide Standart permissions
RUN useradd -s /bin/bash -m ${APP_USER}
RUN groupadd docker
RUN usermod -aG docker ${APP_USER}

WORKDIR /app

# Copy only needed files with no edit permission
COPY --from=build --chown=$APP_USER:$APP_USER /app/requirements.txt requirements.txt
COPY --from=build --chown=$APP_USER:$APP_USER /app/app.py app.py
COPY --from=build --chown=$APP_USER:$APP_USER /app/templates ./templates

RUN pip3 install -r requirements.txt

USER ${APP_USER}

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]