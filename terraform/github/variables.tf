
variable "my_token" {
  type        = string
}

variable "repository_name" {
  description = "Repository name"
  type        = string
  default     = "core-course-labs"
}

variable "default_branch" {
  description = "Default repository branch"
  type        = string
  default     = "main"
}

variable "repository_description" {
  description = "Description for repository"
  type        = string
  default     = "Lab for DevOps 2023 Innopolis University course"
}

variable "repository_visibility" {
  description = "Repository visibility"
  type        = string
  default     = "public"
}

variable "repository_require_conversation_resolution" {
  description = "Require conversation resolution"
  type        = bool
  default     = true
}

variable "repository_enforce_admins" {
  description = "Enforce admins"
  type        = bool
  default     = true
}

variable "repository_required_approving_review_count" {
  description = "Number of required appovers"
  type        = number
  default     = 0
}