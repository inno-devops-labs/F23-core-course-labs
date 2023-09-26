variable "team_name_1" {
  description = "Team name 1"
  type        = string
  default     = "First"
}

variable "team_name_2" {
  description = "Team name 2"
  type        = string
  default     = "Second"
}

variable "team_name_3" {
  description = "Team name 3"
  type        = string
  default     = "Third"
}

variable "name" {
  description = "Repository name"
  type        = string
  default     = "terraform-lab"
}

variable "description" {
  description = "Repository description"
  type        = string
  default     = "Terraform default description"
}

variable "organization" {
  type    = string
  default = "DevOps-AnnaDluzhinskaya"
}
