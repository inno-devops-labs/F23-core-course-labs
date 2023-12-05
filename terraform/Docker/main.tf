terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_python" {
  name         = "lnsfna/app_python"
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.python_container_name

  ports {
    internal = 8080
    external = 8080
  }
}

resource "docker_image" "app_go" {
  name         = "lnsfna/app_go"
  keep_locally = false
}

resource "docker_container" "app_go" {
  image = docker_image.app_go.image_id
  name  = var.go_container_name

  ports {
    internal = 8081
    external = 8081
  }
}

