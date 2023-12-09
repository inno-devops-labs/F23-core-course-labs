# Terraform configuration to deploy a Docker container

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

# use local docker
provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# application from the previous lab
resource "docker_image" "app_python" {
  name = "beleet/devops_lab3_app_python:latest"
}

# create a container resource
resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name = var.container_name
  ports {
      internal = 80 
      external = var.app_external_port
  }
}