# Variables for the docker container

variable "container_name" {
  description = "name of the app container"
  type = string
  default = "app_python"
}

variable "app_external_port" {
  description = "listening port for the app server"
  type = number
  default = "8080"
}