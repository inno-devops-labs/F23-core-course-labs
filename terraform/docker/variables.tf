variable "image_name" {
  type        = string
  description = "The name of the Docker python_app image."
  default     = "vladimirka002/innopolis-devops-python-app:latest"
}

variable "container_name" {
  type        = string
  description = "The name of the Docker container."
  default     = "innopolis-devops-python-app"
}