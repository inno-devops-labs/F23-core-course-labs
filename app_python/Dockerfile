FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask pytz
RUN useradd -m -d /home/appuser -s /bin/bash appuser

USER appuser

EXPOSE 80

CMD ["python", "app.py"]
