variable "image_name" {
  type        = string
  description = "The name of the image to pull."
}

variable "container_name" {
  type        = string
  description = "The name of the container."
}

variable "internal_port" {
  type        = number
  description = "Internal port within the container."
}

variable "external_port" {
  type        = number
  description = "External port exposed out of the container."
}
