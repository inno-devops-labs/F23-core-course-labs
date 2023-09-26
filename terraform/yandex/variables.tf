# https://cloud.yandex.ru/docs/iam/operations/iam-token/create
variable "yandex_token" {
  type        = string
  description = "Specifies token for authentication in Yandex Cloud. For example, IAM "
  sensitive   = true
}

variable "cloud_id" {
  type        = string
  description = "ID of the cloud workspace"
  sensitive   = true
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

