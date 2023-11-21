FROM alpine:3.18.3 AS test
RUN apk --no-cache add py3-pip=23.1.2-r0
RUN mkdir /data && chown app /data
VOLUME [ "/data" ]
RUN addgroup -g 2000 localuser \
    && adduser -u 2000 -G localuser -s /bin/sh -D localuser
USER 2000

COPY . .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
CMD ["python3", "-m", "pytest", "test.py"]

FROM test AS production
ENTRYPOINT ["python3", "-m", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
EXPOSE 8000