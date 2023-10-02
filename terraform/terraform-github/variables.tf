variable "token" {
  type        = string
  description = "github token`"
  sensitive   = true
}

variable "repo_name" {
  description = "github repository"
  type        = string
  default     = "test"
}

variable "repo_description" {
  description = "description of repository"
  type        = string
  default     = "text"
}