FROM python:3.11.5-alpine3.18

WORKDIR /app

COPY . /app

RUN adduser myuser -D && chown -R myuser /app \
    && pip3 install -r requirements.txt \
    && apk --no-cache add curl=8.4.0-r0

USER myuser

EXPOSE 5000

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "wsgi" ]

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:5000/ || exit 1
