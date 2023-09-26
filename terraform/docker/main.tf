terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_elixir" {
  name         = "nikitosing/app_elixir:${var.docker_image_tag}"
  keep_locally = false
}

resource "docker_container" "app_elixir" {
  image = docker_image.app_elixir.image_id
  name  = var.container_name

  ports {
    internal = 4000
    external = var.port
  }

  env = [
    "SECRET_KEY_BASE=${var.SECRET_KEY_BASE}"
  ]
}
