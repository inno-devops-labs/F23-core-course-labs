terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

resource "docker_image" "app_image" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "app_container" {
  image = docker_image.app_image.image_id
  name  = var.container_name
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}