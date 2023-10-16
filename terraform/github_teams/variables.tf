variable "team_1" {
  type    = string
  default = "Team-Frog"
}

variable "team_2" {
  type    = string
  default = "Team-Rabbit"
}

variable "team_3" {
  type    = string
  default = "Team-Lion"
}

variable "repo_name" {
  description = "Repository name"
  type        = string
  default     = "DevOps-Course-Terraform-Repo"
}

variable "repo_description" {
  description = "Repository description"
  type        = string
  default     = "Description by terraform"
}

variable "github_organization" {
  type    = string
  default = "DevOps-Damir-Org"
}