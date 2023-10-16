terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.98.0"
    }
  }
}

locals {
  folder_id = var.folder_id
  cloud_id  = var.cloud_id
}

provider "yandex" {
  cloud_id                 = local.cloud_id
  folder_id                = local.folder_id
  service_account_key_file = "/home/tea/yandex-cloud/authorized_key.json"
}
