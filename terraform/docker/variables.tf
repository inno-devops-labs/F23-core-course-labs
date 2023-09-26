variable "image_name" {
  description = "Docker image name"
  type        = string
  default     = "annadluzhinskaya/python-moscow-time:latest"
}

variable "container_name" {
  description = "Docker container name"
  type        = string
  default     = "my_container"
}

variable "internal_port" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "external_port" {
  description = "External port"
  type        = number
}
