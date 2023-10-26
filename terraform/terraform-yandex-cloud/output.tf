output "internal_ip_address_vm_1" {
  description = "internal ip"
  value       = yandex_compute_instance.DevOps.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  description = "external ip"
  value       = yandex_compute_instance.DevOps.network_interface.0.nat_ip_address
}