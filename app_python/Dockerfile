FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

ENV NAME app_python

CMD ["python", "app.py"]
