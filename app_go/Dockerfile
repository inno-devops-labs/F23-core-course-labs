FROM golang:1.17 AS build

WORKDIR /app

COPY . .

RUN go build -o main

FROM debian:bullseye-slim

WORKDIR /app

COPY --from=build /app/main .

RUN useradd -r -u 1001 newuser

# Change the ownership of the application files to the non-root user
RUN chown newuser:newuser /app/main

USER newuser

EXPOSE 8080

CMD ["./main"]
