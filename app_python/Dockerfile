#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster


WORKDIR /python-app

COPY requirements.txt requirements.txt
COPY entrypoint.sh /entrypoint.sh
COPY . .

RUN useradd -m --no-log-init relisqu  &&  pip3 install --no-cache-dir -r requirements.txt  && chmod +x /entrypoint.sh
USER relisqu



ENTRYPOINT ["/entrypoint.sh"]