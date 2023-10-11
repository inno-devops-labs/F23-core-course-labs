# build wheels
FROM python:3.9-alpine as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk --no-cache add \
        gcc=12.2.1_git20220924-r10 \
        musl-dev=1.2.4-r2

COPY requirements-base.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements-base.txt


# run app
FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /app/wheels /wheels

RUN pip install --no-cache --no-cache-dir /wheels/*

COPY . /app/

ENV APP_PORT ${APP_PORT:-8080}
ENV APP_HOST ${APP_HOST:-"0.0.0.0"}

EXPOSE ${APP_PORT}

HEALTHCHECK  --interval=10s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://${APP_HOST}:${APP_PORT}/ || exit 1

RUN adduser --system \
            --disabled-password \
            --no-create-home \
            --home=/app \
            timeapp
USER timeapp
CMD ["sh", "-c", "uvicorn --host $APP_HOST --port $APP_PORT app.main:app"]
