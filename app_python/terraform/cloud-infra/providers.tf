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
  username = "a.levochkin@innopolis.university"

  # The password of the account
  password = var.vk_cloud_access_key

  # The tenant token can be taken from the project Settings tab - > API keys.
  # Project ID will be our token.
  project_id = "c76aqqafzvtxv1jqhbsvog8e0he2l2ol"
}