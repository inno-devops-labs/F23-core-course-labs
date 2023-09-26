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
  username = "a.evdokimov@innopolis.university"

  # The password of the account
  password = var.vkcs_password

  # The tenant token can be taken from the project Settings tab - > API keys.
  # Project ID will be our token.
  project_id = "b70079a1e424446293c160eb4e349974"

  # Region name
  region = "RegionOne"

  auth_url = "https://infra.mail.ru:35357/v3/"
}
