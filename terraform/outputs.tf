output "container_id" {
  description = "Id of the Docker container"
  value       = docker_container.python-app.id
}

output "image_id" {
  description = "Id of the Docker image"
  value       = docker_image.python-app.id
}