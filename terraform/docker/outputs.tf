output "container_id" {
  description = "Container ID"
  value       = docker_container.app.id
}

output "image_id" {
  description = "Container image"
  value       = docker_image.gilvanov_image.id
}