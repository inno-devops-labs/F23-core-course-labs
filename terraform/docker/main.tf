terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "moscow_time_app" {
  name         = var.moscow_time_app_image_name
  keep_locally = false
}

resource "docker_container" "moscow_time_app" {
  image = docker_image.moscow_time_app.image_id
  name  = var.moscow_time_app_container_name
  ports {
    internal = 80
    external = var.moscow_time_app_external_port
  }
}