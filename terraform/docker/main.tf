terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

resource "docker_image" "gilvanov_image" {
  name         = var.image
  keep_locally = false
}

resource "docker_container" "app" {
  image = docker_image.gilvanov_image.image_id
  name  = var.container_name
  rm    = true
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}