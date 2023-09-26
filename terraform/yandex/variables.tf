# https://cloud.yandex.ru/docs/iam/operations/iam-token/create
variable "yandex_token" {
  type        = string
  description = "Specifies token for authentication in Yandex Cloud. For example, IAM "
  sensitive   = true
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
