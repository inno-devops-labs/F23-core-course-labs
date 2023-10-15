terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
      version = "0.99.1"
    }
  }
}

locals {
    folder_id = "b1gi66qp044sp21suurc"
    cloud_id = "b1gdqj8qui1cv1o7up0f"
}

provider "yandex" {
  cloud_id = local.cloud_id
  folder_id = local.folder_id
  service_account_key_file = "./authorized_key.json"
}