output "python_container_id" {
  description = "Container ID"
  value       = module.app_python.container_id
}

output "rust_container_id" {
  description = "Container image"
  value       = module.app_rust.container_id
}
