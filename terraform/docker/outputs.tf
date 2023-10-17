output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.my_python_app.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.image_python_app.id
}
