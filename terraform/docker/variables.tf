variable "image_name" {
  description = "Name of the docker image"
  type        = string
  default     = "nabiull2020/moscow-time-flask-app:latest"
}

variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "my-container"
}

variable "internal_port" {
  description = "Internal port value"
  type        = number
  default     = 8000
}

variable "external_port" {
  description = "External port value"
  type        = number
  default     = 8000
}