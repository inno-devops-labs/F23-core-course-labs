terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = var.yandex_zone
  folder_id = var.yandex_folder_id
  cloud_id  = var.yandex_cloud_id
  token     = var.yandex_token
}
