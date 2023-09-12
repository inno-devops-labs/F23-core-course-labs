FROM python:3.8-slim

RUN useradd -m app
USER app

WORKDIR /app
COPY requirements.txt app.py /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

RUN pip install --no-cache-dir --no-warn-script-location -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
