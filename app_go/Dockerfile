# build app
FROM golang:1.21.0-alpine AS builder
RUN apk --no-cache add tzdata=2023c-r1

WORKDIR /build
# app have no go.sum to check yet
COPY go.mod /build
RUN go mod download

COPY . .
RUN GOOS=linux go build -o /build/timeapp && \
    adduser --system \
            --disabled-password \
            --no-create-home \
            --home=/app \
            timeapp
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o /build/healthcheck  ./healthcheck/healthcheck.go
# run app
FROM scratch

WORKDIR /app
COPY --from=builder /build/templates /app/templates
COPY --from=builder /build/timeapp /app
COPY --from=builder /build/healthcheck /app
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

HEALTHCHECK --interval=1s --timeout=1s --start-period=2s --retries=3 CMD [ "/app/healthcheck" ]
ENV APP_PORT ${APP_PORT:-8080}
EXPOSE ${APP_PORT}

USER timeapp

ENTRYPOINT ["./timeapp"]
