FROM alpine:3.18.3 AS test
RUN apk --no-cache add bash nmap curl nmap-ncat

RUN addgroup -g 2000 localuser \
    && adduser -u 2000 -G localuser -s /bin/sh -D localuser
USER 2000

COPY . .
CMD ["./test.sh"]

FROM test AS production
ENTRYPOINT ["./main.sh", "moodle.innopolis.university"]
EXPOSE 8000