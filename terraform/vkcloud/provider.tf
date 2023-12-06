# Based on the documentation from here:
# https://mcs.mail.ru/docs/ru/manage/tools-for-using-services/terraform/reference/configuration#fayl_konfiguracii_provaydera_terraform

terraform {
  required_providers {
    vkcs = {
      source  = "vk-cs/vkcs"
      version = "~> 0.1.12"
    }
  }
}

provider "vkcs" {
  username   = var.login
  password   = var.password
  project_id = var.project_id
  region     = "RegionOne"
  auth_url   = "https://infra.mail.ru:35357/v3/"
}