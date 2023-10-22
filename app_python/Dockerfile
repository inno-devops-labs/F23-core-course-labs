FROM python:alpine

WORKDIR /app

COPY requirements.txt .

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir -r requirements.txt \ 
    && addgroup -S app && adduser -S app -G app \
    && chown -R app:app . 

COPY . .

EXPOSE 5000

USER app

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "interface" ]
