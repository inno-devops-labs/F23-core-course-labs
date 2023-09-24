output "image_id" {
  description = "App Image ID"
  value       = docker_image.app_python_image.id
}

output "container_id" {
  description = "App Container ID"
  value       = docker_container.app_python.id
}
