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
    url    = "cr.yandex/crpsmrhh2qi32dnr42gk/nginx:1.25.2-alpine3.18"
    digest = "sha256:433dbc17191a7830a9db6454bcc23414ad36caecedab39d1e51d41083ab1d629"
  }
}
