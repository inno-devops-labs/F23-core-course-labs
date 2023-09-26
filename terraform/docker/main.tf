terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

resource "docker_image" "image" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "container" {
  image = docker_image.image.image_id
  name  = "new-container"
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}