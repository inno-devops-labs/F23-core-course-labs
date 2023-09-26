variable "python_container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "app_python"
}

variable "go_container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "app_go"
}