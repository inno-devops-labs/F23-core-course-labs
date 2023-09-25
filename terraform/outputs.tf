output "container_id" {
  value = { for docker_app in keys(var.docker_apps) : docker_app => module.docker_module[docker_app].container_id }
}

output "image_id" {
  value = { for docker_app in keys(var.docker_apps) : docker_app => module.docker_module[docker_app].image_id }
}

output "yc_internal_ip" {
  value = module.yandex_module.internal_ip
}

output "yc_external_ip" {
  value = module.yandex_module.external_ip
}
