FROM python:3.8-slim-buster AS builder
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

RUN adduser --disabled-password --gecos "" runuser && chown -R runuser /app
USER runuser
EXPOSE 5000
CMD ["python", "app.py"]