output "vpc_network_id" {
  description = "ID of the Yandex VPC network"
  value       = yandex_vpc_network.network-1.id
}
