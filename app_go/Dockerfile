# Stage 1: Build the Go application
FROM golang:1.21-bullseye as builder

# Set the working directory inside the container
WORKDIR /build

# Copy the Go application source code into the container
COPY go.mod .

RUN go mod download
COPY . .
RUN go build -o main main.go

# Stage 2: Create the final image
FROM alpine:latest
RUN addgroup -g 1000 mygroup && adduser -u 1000 -G mygroup -s /bin/sh -D myuser

WORKDIR /app

COPY --from=builder build/main .

COPY templates /app/templates

COPY static /app/static

USER myuser

EXPOSE 80

CMD ["./main"]