terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_python_image" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python_image.image_id
  name  = var.container_name

  ports {
    internal = 5000
    external = var.container_ports_external
  }
}
