FROM golang:1.20-alpine AS build

WORKDIR /app

COPY . .

RUN go test /app/internals/handlers

# won't rely on C libraries, use Alpine's base image
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -o main ./cmd/


FROM alpine:3.14

# time zone data
RUN apk add --no-cache tzdata

RUN adduser -D -u 1000 appuser -G users

WORKDIR /app

USER appuser

COPY --from=build --chown=appuser:users /app/main /app/main

EXPOSE 8080

CMD ["/app/main"]