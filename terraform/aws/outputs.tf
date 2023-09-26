output "public_ip" {
  description = "Public ip"
  value       = aws_instance.app_server.public_ip
}