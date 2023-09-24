module "app-python" {
  source = "./docker"
  image_name = "kurohata7/devops_msk_time"
  container_name = "devops_msk_time"
}

module "yandex-cloud" {
  source = "./yandex"
  zone = "ru-central1-a"
}

module "github" {
  source = "./github"
}

module "github-teams" {
  source = "./github-teams"
}
