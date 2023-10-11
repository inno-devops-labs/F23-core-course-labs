terraform {
  required_providers {
    vkcs = {
      source  = "vk-cs/vkcs"
      version = "~> 0.1.12"
    }
  }
}

provider "vkcs" {
  # Your user account.
  username = "vlasov-egorl@ya.ru"

  # The password of the account
  password = var.vk_cloud_access_key

  # The tenant token can be taken from the project Settings tab - > API keys.
  # Project ID will be our token.
  project_id = "ac96e04f130a4203aaa80cdd235b7fa6"

  # Region name
  region = "RegionOne"

  auth_url = "https://infra.mail.ru:35357/v3/"
}
