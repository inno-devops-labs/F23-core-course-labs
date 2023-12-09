#!/bin/bash

# Function to display a message with a checkmark
function print_success() {
  echo -e "\033[1;32m✅ $1\033[0m"
}

# Function to display a message with a cross mark
function print_error() {
  echo -e "\033[1;31m❌ $1\033[0m"
}

# Stop and remove containers based on the specified image
print_success "Stopping and removing containers based on m4k4rich/updated-python-app image..."
docker stop $(docker ps -a -q --filter ancestor=m4k4rich/updated-python-app) && docker rm $(docker ps -a -q --filter ancestor=m4k4rich/updated-python-app) || print_error "Failed to stop and remove containers."

# Delete the local image version
print_success "Deleting the local m4k4rich/updated-python-app:latest image version..."
docker rmi -f m4k4rich/updated-python-app:latest || print_error "Failed to delete the local image."

# Build the Docker image using buildx for the specified platform and push to Docker Hub
print_success "Building and pushing m4k4rich/updated-python-app:latest image to Docker Hub..."
docker buildx build --platform linux/arm64 -t m4k4rich/updated-python-app:latest --push . || print_error "Failed to build and push the image."

# Build and run the application using Docker Compose, with the --build flag to rebuild the images
print_success "Building and running the application using Docker Compose..."
docker-compose up --build -d || print_error "Failed to build and run the application."

# Display a final success message
print_success "Script execution completed successfully!"
