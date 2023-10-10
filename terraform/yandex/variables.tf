# https://cloud.yandex.ru/docs/iam/operations/iam-token/create
variable "yandex_token" {
  type        = string
  description = "Specifies token for authentication in Yandex Cloud. For example, IAM "
  sensitive   = true
}

variable "zone" {
  type = string
  default = "ru-central1-b"
}

variable "cloud_id" {
  type        = string
  description = "ID of the cloud workspace"
}

# https://cloud.yandex.com/en/docs/resource-manager/operations/folder/get-id
variable "folder_id" {
  type        = string
  description = "ID of the folder within the cloud"
  sensitive   = true
}

variable "service_account_id" {
  type        = string
  description = "Service account ID"
  sensitive   = true
}

variable "image_url" {
	type = string
	description = "URL of the Docker image including the container registry"
	default = "cr.yandex/crpsmrhh2qi32dnr42gk/nginx:1.25.2-alpine3.18"
}

variable "image_digest" {
	type = string
	description = "Hash of the Docker image"
	default = "sha256:433dbc17191a7830a9db6454bcc23414ad36caecedab39d1e51d41083ab1d629"	
}

variable "nginx_container_enabled" {
	type = bool
	description = "Specifies whether nginx container should be active"
	default = false
}

variable "vm_os_image_id" {
	type = string
	description = "Base image for virtual machines"
	default = "fd8clogg1kull9084s9o" 
}
# "fd8a67rb91j689dqp60h" # debian-11-v20230130
#  fd8ch5n0oe99ktf1tu8r | ubuntu-22-04-lts-v20221114 

variable "vm_name" {
  type = string
	default = "terraform-vm"
}

variable "vm_ram_gb" {
  type = number
  default = 2
}

variable "vm_cores" {
  type = number
  default = 2
}

variable "vm_user" {
  type = string
  default = "ubuntu"
}

variable "ssh_pubkey_path" {
  description = "Path to the SSH key used to manage instances"
  type        = string
  default     = "~/.ssh/yacloud.pub"
  sensitive   = true
}
