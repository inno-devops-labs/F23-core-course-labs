module "app-python" {
  source = "./docker"
  image_name = "kurohata7/devops_msk_time"
  container_name = "devops_msk_time"
}
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
}
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# module "yandex-cloud" {
#   source = "./yandex"
#   zone = "ru-central1-a"
# }

module "github" {
  source = "./github"
  github_token = var.github_token
}

module "github-teams" {
  source = "./github-teams"
  github_organization = "FirstRaccoonInaTrenchCoat"
  github_token = var.github_token
}
