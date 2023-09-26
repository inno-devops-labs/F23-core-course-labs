variable "yandex_cloud_token" {
  description = "Yandex Cloud OAuth token"
  type        = string
}

variable "yandex_cloud_vm_name" {
  description = "Yandex Cloud virtual machine name"
  type        = string
  default     = "edikgoose-compute-instance"
}

variable "yandex_cloud_id" {
  description = "Yandex Cloud id"
  type        = string
}

variable "yandex_cloud_folder_id" {
  description = "Yandex Cloud folder id"
  type        = string
}

variable "yandex_cloud_zone" {
  description = "Yandex Cloud zone"
  type        = string
  default     = "ru-central1-a"
}