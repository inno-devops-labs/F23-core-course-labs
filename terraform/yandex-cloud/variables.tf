variable "yandex_token" {
  description = "Token of service accounti in yandex cloud"
  type        = string
  sensitive   = true
}

variable "yandex_folder_id" {
  description = "ID of target folder of yandex cloud"
  type        = string
  default     = "b1gq1nfb08rgqmrqosie"
}

variable "yandex_cloud_id" {
  description = "ID of target cloud of yandex cloud"
  type        = string
  default     = "b1ghasns8c3brvelo56n"
}

variable "yandex_zone" {
  description = "Zone to deploy"
  type        = string
  default     = "ru-central1-a"
}