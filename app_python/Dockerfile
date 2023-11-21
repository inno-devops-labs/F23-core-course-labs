FROM python:3.8

RUN addgroup --g 1000 mygroup
RUN adduser -u 1000 -G mygroup -h /myuser-dir -D myuser
USER myuser

COPY ./run.py .
COPY ./requirements.txt .

VOLUME ["./visits", "./visits"]

RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python", "run.py"]