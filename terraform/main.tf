module "app_python" {
  source = "./docker"

  image          = "dashvayet/python_app"
  container_name = "python_app_new"
}

module "app_cpp" {
  source = "./docker"

  image          = "dashvayet/app_cplusplus"
  container_name = "app_cplusplus"
  external_port  = 10000
  internal_port  = 10000
}

module "yandex_cloud" {
  source   = "./cloud"
  vm_name  = "test-name-updated"
  hostname = "test-hostname"
}

module "github" {
  source = "./github"
}

# module "github_teams" {
#   source = "./github_teams"
#
#   github_organization = "ElestriasOrg"
# }
