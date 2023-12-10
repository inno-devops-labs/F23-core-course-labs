FROM python:3.10

WORKDIR /app
COPY . /app

RUN adduser newuser && chown -R newuser /app
USER newuser

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m",  "gunicorn", "-b", ":8000", "app:app"]
