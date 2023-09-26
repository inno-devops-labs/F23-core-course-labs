variable "server_name" {
  type        = string
  default     = "dshamikNewServer"
}

variable "ami_value" {
  type        = string
  default     = "ami-830c94e3"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
}

variable "region" {
  type        = string
  default     = "us-west-2"
}