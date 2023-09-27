output "yandex-ip-address" {
  description = "Ip address of vm"
  value       = yandex_compute_instance.terraform.network_interface[0].nat_ip_address
}
