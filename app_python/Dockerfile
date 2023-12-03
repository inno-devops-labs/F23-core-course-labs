FROM python:3.11-alpine AS build-env

COPY . /app
RUN adduser -D localuser && chown -R localuser /app
USER localuser
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements/prod.txt

FROM gcr.io/distroless/python3:latest
COPY --from=build-env /app /app_python
COPY --from=build-env /home/localuser/.local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

ENV PORT 8000
EXPOSE $PORT

ENTRYPOINT ["python", "-m", "uvicorn", "app_python.src.main:app", "--host", "0.0.0.0", "--port", "8000"]