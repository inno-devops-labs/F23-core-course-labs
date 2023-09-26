variable "server_name" {
  description = "Name of the server"
  type        = string
  default     = "DevOpsCourseAppServerInstance"
}

variable "ami_value" {
  description = "ami"
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