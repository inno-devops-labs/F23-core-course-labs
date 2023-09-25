module "docker_module" {
  source = "./docker"

  for_each = var.docker_apps

  image_name     = each.value.image_name
  container_name = each.value.container_name
  internal_port  = each.value.internal_port
  external_port  = each.value.external_port
}

module "yandex_module" {
  source = "./yandex-cloud"

  yc_token     = var.yc_token
  yc_cloud_id  = var.yc_cloud_id
  yc_folder_id = var.yc_folder_id
  yc_zone      = var.yc_zone
  ssh_pubkey   = var.ssh_pubkey

}
