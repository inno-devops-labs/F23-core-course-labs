variable "github_organization" {
  type = string
  default = "InnoDevopsCourseOrg"
}

variable "github_token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}