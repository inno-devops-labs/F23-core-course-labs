output "internal_ip_address_app_python" {
  value = yandex_compute_instance.app-python-vm.network_interface.0.ip_address
}

output "external_ip_address_app_python" {
  value = yandex_compute_instance.app-python-vm.network_interface.0.nat_ip_address
}
