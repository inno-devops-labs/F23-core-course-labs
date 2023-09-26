variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

variable "repo_name" {
  type        = string
  description = "Specifies the GitHub repository name"
}

variable "owner" {
  type        = string
  description = "Specifies the GitHub repository owner"
}

variable "github_organization" {
  type        = string
  description = "Specifies the GitHub organization"
}
