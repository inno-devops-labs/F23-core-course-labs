FROM alpine:3.18.3 AS test
RUN apk --no-cache add bash=5.2.15-r5 nmap=7.93-r1 curl=8.3.0-r0 nmap-ncat=7.93-r1

RUN addgroup -g 2000 localuser \
    && adduser -u 2000 -G localuser -s /bin/sh -D localuser
USER 2000

COPY . .
CMD ["./test.sh"]

FROM test AS production
ENTRYPOINT ["./main.sh"]
EXPOSE 8000