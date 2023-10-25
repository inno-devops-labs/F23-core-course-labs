variable "token" {
  type        = string
  description = "Specifies the Yandex PAT token or `Yandex_Cloud_TOKEN`"
  sensitive   = true
}

variable "zone" {
  description = "Name of zone in Yandex Cloud"
  type        = string
  default     = "ru-central1-a"
}

variable "vm_name" {
  description = "Name of the virtual machine in Yandex Cloud"
  type        = string
  default     = "terraform-app"
}

variable "network_name" {
  description = "Name of the network in Yandex Cloud"
  type        = string
  default     = "network1"
}

variable "subnetwork_name" {
  description = "Name of the subnetwork in Yandex Cloud"
  type        = string
  default     = "subnet1"
}

variable "fid" {
  description = "Foulder ID in YC"
  type        = string
  default     = "b1gkp5mnhp65cbi1lti9"
}