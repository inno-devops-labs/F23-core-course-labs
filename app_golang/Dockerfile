FROM golang:1.21.1

WORKDIR /app
COPY go.mod /app/
COPY go.sum /app/
COPY main.go /app/

RUN go mod download

EXPOSE 8008
CMD ["go", "run", "main.go"]