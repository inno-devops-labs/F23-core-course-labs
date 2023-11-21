FROM python:3.10-alpine3.18

WORKDIR /app
RUN apk --no-cache add curl

COPY requirements.txt /app/
RUN adduser --disabled-password app && pip install --no-cache-dir -r requirements.txt
COPY ./src ./src
RUN chmod -R a-w+x+r /app
USER app
EXPOSE 5000
ENV PYTHONPATH .
ENTRYPOINT ["python3", "src/web/__main__.py"]

