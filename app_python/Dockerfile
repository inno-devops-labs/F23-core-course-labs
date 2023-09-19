FROM python:3.10-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN adduser --disabled-password app && pip install --no-cache-dir -r requirements.txt
COPY ./src ./src
RUN chmod -R a-w+x+r /usr/src/app 
USER app
EXPOSE 5000
ENV PYTHONPATH .
ENTRYPOINT ["python3", "src/web/__main__.py"]

