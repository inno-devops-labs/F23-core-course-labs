output "python_container_id" {
  description = "Container ID"
  value       = module.app_python.container_id
}

output "rust_container_id" {
  description = "Container image"
  value       = module.app_rust.container_id
}

output "vm_instance_external_ip" {
  value = module.yandex_cloud.instance_external_ip
}

output "github_repo_full_name" {
  value = module.github.repo_full_name
}
