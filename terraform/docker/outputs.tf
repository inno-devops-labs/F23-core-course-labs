output "image_id" {
  description = "My image ID"
  value       = docker_image.nginx.id
}

output "container_id" {
  description = "My Container ID"
  value       = docker_container.nginx.id
}