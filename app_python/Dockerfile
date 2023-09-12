
FROM python:3.9-alpine AS prepare

COPY . /app_python

RUN adduser -D rootlessuser && chown -R rootlessuser /app_python

USER rootlessuser

WORKDIR /app_python

RUN pip install --no-cache-dir -r requirements.txt

FROM prepare AS runtime

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]
