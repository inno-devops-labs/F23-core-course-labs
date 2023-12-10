terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///Users/arina/.docker/run/docker.sock"
}

resource "docker_image" "app_python" {
  name         = "amoriodi/app_python:latest"
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.container_name
  ports {
    internal = 8080
    external = 8000
  }
}
