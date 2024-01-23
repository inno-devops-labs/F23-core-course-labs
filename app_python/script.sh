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
print_success "Stopping and removing containers based on artkochergin/updated-python-app image..."
docker stop $(docker ps -a -q --filter ancestor=artkochergin/updated-python-app) && docker rm $(docker ps -a -q --filter ancestor=artkochergin/updated-python-app) || print_error "Failed to stop and remove containers."

# Delete the local image version
print_success "Deleting the local artkochergin/updated-python-app:latest image version..."
docker rmi -f artkochergin/updated-python-app:latest || print_error "Failed to delete the local image."

# Build the Docker image using buildx for the specified platform and push to Docker Hub
print_success "Building and pushing artkochergin/updated-python-app:latest image to Docker Hub..."
docker buildx build --platform linux/arm64 -t artkochergin/updated-python-app:latest --push . || print_error "Failed to build and push the image."

# Build and run the application using Docker Compose, with the --build flag to rebuild the images
print_success "Building and running the application using Docker Compose..."
docker-compose up --build -d || print_error "Failed to build and run the application."

# Display a final success message
print_success "Script execution completed successfully!"
