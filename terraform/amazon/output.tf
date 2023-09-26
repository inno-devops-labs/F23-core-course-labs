output "public_ip" {
  description = "Public Ip"
  value       = aws_instance.app_server.public_ip
}
