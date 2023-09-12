# Build Stage
FROM golang:1.20-alpine as build

WORKDIR /app

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags="-s -w -extldflags \"-static\"" -o go_app


# Run Stage
FROM alpine:3.18.3 as final

WORKDIR /

COPY --from=build /app/go_app /app/go.env /

COPY --from=build /app/templates /templates

RUN adduser -D user1

USER user1

EXPOSE 3000

CMD ["./go_app"]