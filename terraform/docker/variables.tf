variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "elixir_time"
}

variable "SECRET_KEY_BASE" {
  description = "key for cookie encryption"
  type        = string
  default     = "WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O"
}

variable "port" {
  description = "external port"
  type        = number
  default     = 80
}

variable "docker_image_tag" {
  description = "tag of target docker image"
  type = string
  default = "latest"
}