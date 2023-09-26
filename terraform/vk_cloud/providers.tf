terraform {
  required_providers {
    vkcs = {
      source  = "vk-cs/vkcs"
      version = "~> 0.1.12"
    }
  }
}

provider "vkcs" {
    # As I got banned from both yandex and vk cloud for no reason, i use cloud account of other student
    username = "d.korneenko@innopolis.university"

    # The password of the account
    password = var.password

    # The tenant token can be taken from the project Settings tab - > API keys.
    # Project ID will be our token.
    project_id = "9527808136d146a8a0d6bd9fbf7e8764"
    
    # Region name
    region = "RegionOne"
    
    auth_url = "https://infra.mail.ru:35357/v3/" 
}