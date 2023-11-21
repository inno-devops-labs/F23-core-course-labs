FROM golang:alpine3.18 as build
EXPOSE 80

ARG appdir=/goapp
WORKDIR ${appdir}
COPY . .
RUN \
    apk add make=4.4.1-r1 --no-cache &&\
    make test &&\
    make build

FROM gcr.io/distroless/static-debian12:nonroot as production
USER nobody:nobody
ENV GOAPP_PORT=80
COPY --from=build ${appdir}/goapp /
COPY --from=build ${appdir}/goapp/healthcheck/healthcheck /bin/healthcheck
CMD ["/goapp"]
