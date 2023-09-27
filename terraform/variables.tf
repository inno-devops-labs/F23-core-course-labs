variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "app_python_container"
}

variable "github_token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}