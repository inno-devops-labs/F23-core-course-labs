# Use official base image
FROM golang:1.19-alpine AS build

# Set working directory
WORKDIR /app

# Copy file with project requirements
COPY go.mod go.sum ./

# Install go dependencies
RUN go mod download

# Copy all necessary files
COPY . .

# Build binary and add new user info
RUN CGO_ENABLED=0 GOOS=linux go build -o app_go && echo "user:x:1000:1000:User:/:" > /etc_passwd


FROM alpine:3.18.3 AS final

# Set working directory
WORKDIR /

# Copy binary file and .env file
COPY --from=build /app/app_go /app/.env ./

# Copy directory with html templates
COPY --from=build /app/templates  /templates

# Copy passwd file
COPY --from=build /etc_passwd /etc/passwd

# Run container from non-root user
USER user

# Expose ports
EXPOSE 8081 8081

# Run application
CMD [ "./app_go" ]
