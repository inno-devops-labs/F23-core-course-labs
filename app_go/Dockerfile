FROM golang:alpine
RUN adduser -D -g '' newuser
USER newuser
WORKDIR /home/newuser
COPY . .
RUN go build -o main main.go
EXPOSE 3000
CMD ["./main"]
