# Use the official Go base image
FROM golang:1.21-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . .

# Build application
RUN CGO_ENABLED=0 GOOS=linux go build -o go_app

# Second stage of docker build
FROM alpine:3.18.3 as final

# Set the working directory in the container
WORKDIR /

# Add required package
RUN apk --no-cache add tzdata=2023c-r1

# Copy built application
COPY --from=build /app /

# Run application
CMD ["./go_app"]