variable "token" {
  type        = string
  description = "Github access token"
  sensitive   = true
}

variable "repository_name" {
  type        = string
  description = "Repository name"
  default     = "iu-devops-test"
}

variable "repository_description" {
  type        = string
  description = "Repository description"
  default     = "Test repository created by terraform"
}

variable "repository_visibility" {
  type        = string
  description = "Repository visibility"
  default     = "public"
}