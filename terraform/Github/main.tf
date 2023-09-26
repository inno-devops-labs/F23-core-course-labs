terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.token
}

resource "github_repository" "terraform" {
  name               = "core-course-labs"
  description        = "DevOps course labs"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
}

resource "github_branch_default" "main" {
  repository = github_repository.terraform.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.terraform.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}