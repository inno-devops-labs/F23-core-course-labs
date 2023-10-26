variable "token" {
  type        = string
  description = "token of yandex cloud"
  sensitive   = true
}

variable "zone" {
  description = "zone in yc"
  type        = string
  default     = "ru-central1-a"
}

variable "vm_name" {
  description = "vm in yc"
  type        = string
  default     = "terraform-app"
}

variable "network_name" {
  description = "yc network"
  type        = string
  default     = "network1"
}

variable "subnetwork_name" {
  description = "yc subnetwork"
  type        = string
  default     = "subnet1"
}

variable "fid" {
  description = "foulder id"
  type        = string
  default     = "b1ghpemhhp65c6i1lti6"
}