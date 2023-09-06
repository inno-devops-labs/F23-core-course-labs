FROM golang:1.21.0-alpine AS builder

ARG USER=appuser
ARG UID=10001  
RUN adduser \    
    --disabled-password \    
    --gecos "" \    
    --home "/nonexistent" \    
    --shell "/sbin/nologin" \    
    --no-create-home \    
    --uid "${UID}" \    
    "${USER}"

WORKDIR /app
COPY go.mod go.sum ./
# RUN go get -d -v
RUN go mod download && go mod verify

COPY . . 
RUN GOOS=linux go build -ldflags="-w -s" -o /bin/app_go

FROM scratch AS release

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /bin/app_go /bin/app_go

ENV PORT=8080
ENV GIN_MODE=release
EXPOSE $PORT

USER appuser:appuser

ENTRYPOINT ["/bin/app_go"]