FROM python:3.11.5-alpine

LABEL iviosab.moscow_time.created="2023-09-11T10:11:43+00:00"
LABEL iviosab.moscow_time.authors="Mosab Mohamed"
LABEL iviosab.moscow_time.source="https://github.com/IVIosab/core-course-labs/tree/main/app_python"
LABEL iviosab.moscow_time.version="0.0.1"
LABEL iviosab.moscow_time.title="Moscow Time"
LABEL iviosab.moscow_time.description="This image creates a simple web app that displays moscow time (intended for docker learning purposes)"
LABEL iviosab.moscow_time.base.digest="e5d592c422d6e527cb946ae6abb1886c511a5e163d3543865f5a5b9b61c01584"

WORKDIR /app

COPY . /app

RUN adduser myuser -D && chown -R myuser /app \
    && pip3 install -r requirements.txt

USER myuser

EXPOSE 5000

ENTRYPOINT [ "python3", "app.py"]