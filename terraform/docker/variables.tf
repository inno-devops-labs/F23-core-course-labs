variable "image_name" {
  type        = string
  default     = "dshamik/dshamik_msk_time:latest"
}

variable "container_name" {
  type        = string
  default     = "new-container"
}

variable "internal_port" {
  type        = number
  default     = 8090
}

variable "external_port" {
  type        = number
  default     = 80
}