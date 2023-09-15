module "app_python" {
  source = "./docker"

  image          = "dvechtomova/python_app"
  container_name = "python_app"
}

module "app_rust" {
  source = "./docker"

  image          = "dvechtomova/rust_app"
  container_name = "rust_app"
  external_port  = 8081
}

module "yandex_cloud" {
  source = "./yandex_cloud"

  vm_name  = "test"
  hostname = "test"
}

module "github" {
  source = "./github"
}
