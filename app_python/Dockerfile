FROM python:3-alpine3.15

WORKDIR /application

COPY . /application

RUN adduser someuser -D && chown -R someuser /application && pip install --no-cache-dir -r requirements.txt

USER someuser

EXPOSE 8080

CMD ["python", "./src/app.py"]