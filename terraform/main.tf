module "nginx_server" {
  source         = "./docker"
  image_name     = "nginx:latest"
  container_name = "my-nginx-app"
}

module "yandex-cloud" {
  source = "./cloud"
}

module "github" {
  source = "./github"
  github_token = var.github_token
}

module "github-teams" {
  source = "./teams"
  github_organization = "main-devops-org"
  github_token = var.github_token
}