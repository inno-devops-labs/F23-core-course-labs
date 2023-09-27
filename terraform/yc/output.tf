output "internal_ip_address_vm_1" {
  description = "Internal IP Address"
  value       = yandex_compute_instance.DevOps.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  description = "External IP Address"
  value       = yandex_compute_instance.DevOps.network_interface.0.nat_ip_address
}