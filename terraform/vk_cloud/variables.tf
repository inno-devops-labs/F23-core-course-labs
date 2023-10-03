variable "password" {
  description = "Password for Vk Danila's cloud "
  type        = string
}

variable "image_flavor" {
  description = "Image for VMs"
  type        = string
  default     = "Ubuntu-22.04-202208"
}

variable "compute_flavor" {
  description = "Unit type"
  type        = string
  default     = "Basic-1-2-20"
}

variable "key_pair_name" {
  type    = string
  default = "anna"
}

variable "availability_zone_name" {
  type    = string
  default = "MS1"
}