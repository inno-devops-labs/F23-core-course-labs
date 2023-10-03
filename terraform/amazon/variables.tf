variable "server_name" {
  description = "Server name"
  type        = string
  default     = "annadlu_server_2"
}

variable "ami" {
  description = "Ami"
  type        = string
  default     = "ami-0640ee265e4ae17ea"
}

variable "instance_type" {
  description = "Instance type"
  type        = string
  default     = "t2.nano"
}

variable "region" {
  description = "Region"
  type        = string
  default     = "us-west-2"
}

variable "key_name" {
  type        = string
  default     = "ssh-key"
}