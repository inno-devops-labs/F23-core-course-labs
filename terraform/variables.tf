variable "docker_apps" {
  type = map(object({
    image_name     = string
    container_name = string
    internal_port  = number
    external_port  = number
  }))
  description = "Docker apps to run"
  default = {
    "nginx" = {
      image_name     = "nginx:latest"
      container_name = "nginx"
      internal_port  = 80
      external_port  = 8080
    }
  }
}

variable "yc_token" {
  description = "Yandex Cloud token"
  sensitive   = true
}

variable "yc_cloud_id" {
  description = "Yandex Cloud ID"
}

variable "yc_folder_id" {
  description = "Yandex Cloud folder ID"
}

variable "yc_zone" {
  description = "Yandex Cloud zone"
}

variable "ssh_pubkey" {
  description = "SSH public key"
  default     = "~/.ssh/id_rsa.pub"
  sensitive   = true
}
