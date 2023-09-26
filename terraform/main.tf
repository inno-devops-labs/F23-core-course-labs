terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
}

resource "docker_image" "python-app" {
  name         = "relisqu/python-app:latest"
  keep_locally = false
}

resource "docker_container" "python-app" {

  image = docker_image.python-app.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8080
  }
}