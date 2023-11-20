output "container_id" {
  value = docker_container.app_container.id
}
output "image_id" {
  value = docker_image.app_image.image_id
}
