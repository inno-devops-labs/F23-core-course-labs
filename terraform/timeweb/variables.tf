variable "timeweb_token" {
  type        = string
  description = "Specifies the TimeWeb cloud provider token"
  sensitive   = true
}

variable "instance_name" {
  description = "Value of the Name tag for the Timeweb instance"
  type        = string
  default     = "Reasonable Cygnus"
}

variable "timeweb_ssh_pubkey" {
  description = "Path to the SSH key used to manage instances"
  type        = string
  default     = "~/.ssh/timeweb.pub"
  sensitive   = true
}

