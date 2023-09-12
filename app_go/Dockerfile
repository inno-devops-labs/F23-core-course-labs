FROM golang:1.20-bookworm

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY go.* ./
RUN go mod download

# Copy the application code and build it
COPY cmd/ cmd/
COPY internal/ internal/

RUN go build -o main ./cmd/main.go

# Expose the port
EXPOSE 9000

# Run the application
CMD ["./main"]