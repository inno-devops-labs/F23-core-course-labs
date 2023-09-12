#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN useradd -m --no-log-init relisqu 
USER relisqu

WORKDIR /python-app

COPY requirements.txt requirements.txt
COPY entrypoint.sh /entrypoint.sh
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt  && chmod +x /entrypoint.sh


EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]