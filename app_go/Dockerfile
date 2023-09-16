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

# run app
FROM scratch

WORKDIR /app
COPY --from=builder /build/templates /app/templates
COPY --from=builder /build/timeapp /app
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

ENV APP_PORT ${APP_PORT:-8080}
EXPOSE ${APP_PORT}

USER timeapp

ENTRYPOINT ["./timeapp"]
