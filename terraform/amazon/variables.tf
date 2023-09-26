variable "server_name" {
  description = "Server name"
  type        = string
  default     = "annadlu_server_2"
}

variable "ami" {
  description = "Ami"
  type        = string
  default     = "ami-830c94e3"
}

variable "instance_type" {
  description = "Instance type"
  type        = string
  default     = "t2.micro"
}

variable "region" {
  description = "Region"
  type        = string
  default     = "us-west-2"
}
