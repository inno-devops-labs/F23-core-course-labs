FROM python:3.10

WORKDIR /app

RUN adduser newuser && chown -R newuser /app
USER newuser

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m",  "gunicorn", "-b", ":8000", "app:app"]
