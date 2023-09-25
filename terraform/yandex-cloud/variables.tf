variable "yc_token" {
  type        = string
  description = "Yandex Cloud API key"
  sensitive   = true
}

variable "yc_cloud_id" {
  type        = string
  description = "Yandex Cloud id"
}

variable "yc_folder_id" {
  type        = string
  description = "Yandex Cloud folder id"
}

variable "yc_zone" {
  type        = string
  description = "Yandex Cloud compute default zone"
  default     = "ru-central1-a"
}

variable "yc_image_id" {
  type        = string
  description = "Yandex Cloud image id, default is Ubuntu 22.04 LTS"
  default     = "fd8tf1sepeiku6d37l4l"
}

variable "preemptible" {
  description = "Specifies if the instance is preemptible"
  type        = bool
  default     = false
}

variable "allow_stopping_for_update" {
  description = "Allow terraform to stop the instance to update its properties"
  type        = bool
  default     = true
}

variable "is_nat" {
  description = "Provide a public address for instance to access the internet over NAT"
  type        = bool
  default     = true
}

variable "size" {
  description = "Size of the boot disk in GB"
  type        = number
  default     = 20
}

variable "cores" {
  description = "CPU cores for the instance"
  type        = number
  default     = 2
}

variable "memory" {
  description = "Memory size for the instance in GB"
  type        = number
  default     = 4
}

variable "core_fraction" {
  description = "Baseline performance for a core as a percent"
  type        = number
  default     = 100
}

variable "ssh_username" {
  description = "User for SSH access to the instance"
  type        = string
  default     = "devopscourse-user"
}

variable "ssh_pubkey" {
  description = "SSH public key file path for access to the instance"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
  sensitive   = true
}
