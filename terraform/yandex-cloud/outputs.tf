output "vm_1_public_ip" {
  value = yandex_compute_instance.vm_1.network_interface[0].nat_ip_address
}

output "vm_2_public_ip" {
  value = yandex_compute_instance.vm_2.network_interface[0].nat_ip_address
}

output "subnet_id" {
  value = data.yandex_vpc_subnet.default_a.subnet_id
}

output "last_ubuntu" {
  value = data.yandex_compute_image.last_ubuntu.id
}