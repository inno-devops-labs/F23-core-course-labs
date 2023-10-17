terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = "ru-central1-b"
  cloud_id  = var.cloud_id
  token     = var.yandex_token
  folder_id = var.folder_id
}

# https://terraform-provider.yandexcloud.net/Resources/serverless_container
resource "yandex_serverless_container" "nginx_container" {
  name               = "anothernginx"
  description        = "yet another nginx container deployed for known purposes"
  memory             = 256
  execution_timeout  = "15s"
  cores              = 1
  core_fraction      = 100
  service_account_id = var.service_account_id
  image {
    url    = var.image_url
    digest = var.image_digest
  }
}
