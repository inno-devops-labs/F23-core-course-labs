output "container_id" {
  description = "ID of the classicClock container"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "ID of the classicClock image"
  value       = docker_image.nginx.id
}