terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

resource "docker_image" "dvechtomova_image" {
  name         = var.image
  keep_locally = false
}

resource "docker_container" "python_app" {
  image = docker_image.dvechtomova_image.image_id
  name  = var.container_name
  ports {
    internal = 8080
    external = var.external_port
  }
}
