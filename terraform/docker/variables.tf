variable "image_name" {
  type = string
}

variable "container_name" {
  type = string
}

variable "container_ports_external" {
  type    = number
  default = 8000
}