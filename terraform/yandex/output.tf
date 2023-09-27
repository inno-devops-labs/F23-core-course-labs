output "instance_id" {
  description = "ID of VM"
  value       = yandex_compute_instance.vm.id
}

output "external_ip" {
  value = yandex_compute_instance.vm.network_interface[0].nat_ip_address
}