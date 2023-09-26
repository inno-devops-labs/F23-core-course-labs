variable "github_token" {
  description = "github token"
  type        = string
  sensitive   = true
}


variable "github_owner" {
  description = "github owner"
  type        = string
  default     = "devops-organizational"
}