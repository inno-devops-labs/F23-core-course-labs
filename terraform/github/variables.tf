variable "token" {
  type        = string
  description = "Specifies the Github PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "owner" {
  description = "My Github owner"
  type        = string
  default     = "devops-organizational"
}