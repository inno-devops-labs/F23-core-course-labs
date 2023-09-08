FROM python:3.9-alpine

WORKDIR /app

RUN adduser -D simpleuser

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

USER simpleuser

EXPOSE 8090

ENTRYPOINT ["python3", "app.py"]
