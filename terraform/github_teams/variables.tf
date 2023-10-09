variable "owner" {
  type        = string
  description = "Github owner"
  default = "edikgoose-organization"
}

variable "token" {
  type        = string
  description = "Github access token"
  sensitive   = true
}

variable "repository_name" {
  type        = string
  description = "Repository name"
  default     = "iu-devops-teams-test"
}

variable "repository_description" {
  type        = string
  description = "Repository description"
  default     = "Test repository for teams created by terraform"
}

variable "repository_visibility" {
  type        = string
  description = "Repository visibility"
  default     = "public"
}