terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

resource "docker_image" "image_python_app" {
  name         = "purfreak/lab2_devops:latest"
  keep_locally = false
}

resource "docker_container" "my_python_app" {
  image = docker_image.image_python_app.image_id
  name = "my_python_app_new"
  ports {
    internal = 8000
    external = 5555
  }
}
