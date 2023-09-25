variable "moscow_time_app_image_name" {
  description = "Value of the name for the Docker image for Moscow Time App"
  type        = string
  default     = "edikgoose/moscow-time-app:latest"
}

variable "moscow_time_app_container_name" {
  description = "Value of the name for the Docker container for Moscow Time App"
  type        = string
  default     = "moscow-time-app"
}

variable "moscow_time_app_external_port" {
  description = "Docker external port for Moscow Time App"
  type        = number
  default     = 8081
}
