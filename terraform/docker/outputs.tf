output "image_id" {
  description = "Container image"
  value       = docker_image.app_image.id
}

output "container_id" {
  description = "Container ID"
  value       = docker_container.app_container.id
}