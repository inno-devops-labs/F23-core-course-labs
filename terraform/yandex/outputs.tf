output "internal_ip_address-app-python" {
  value = yandex_compute_instance.vm-app-python.network_interface.0.ip_address
}

output "external_ip_addres-app-python" {
  value = yandex_compute_instance.vm-app-python.network_interface.0.nat_ip_address
}

resource "local_file" "ansible_inventory" {
  content = templatefile("inventory.tmpl",
    {
      vm-app-python-address = yandex_compute_instance.vm-app-python.network_interface.0.nat_ip_address
    }
  )
  filename = "../../ansible/inventory/yandex.yaml"
}
