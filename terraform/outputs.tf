output "go_container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_go.id
}

output "go_image_id" {
  description = "ID of the Docker image"
  value       = docker_image.app_go.id
}

output "python_container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_python.id
}

output "python_image_id" {
  description = "ID of the Docker image"
  value       = docker_image.app_python.id
}

