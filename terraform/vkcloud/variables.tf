variable "image_flavor" {
  type = string
  default = "Ubuntu-22.04-202208"
}

variable "compute_flavor" {
  type = string
  default = "Basic-1-2-20"
}

variable "key_pair_name" {
  type = string
  default = "keypair-terraform"
}

variable "availability_zone_name" {
  type = string
  default = "MS1"
}

variable "login" {
  description = "VK cloud account login"
  type        = string
  sensitive   = true
}

variable "password" {
  description = "VK cloud account password"
  type        = string
  sensitive   = true
}

variable "project_id" {
  description = "VK cloud project id"
  type        = string
  sensitive   = true
}