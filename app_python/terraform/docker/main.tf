provider "docker" {
  host = var.docker_host

}

resource "docker_image" "app_python" {
  name         = var.docker_image_name
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.docker_container_name
  ports {
    internal = var.docker_container_internal_port
    external = var.docker_container_external_port
  }
}
