terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.36.0"
    }
  }
  required_version = ">= 0.13"
}

provider "github" {
  token = var.github_token
  owner = var.github_owner
}

resource "github_repository" "devops" {
  name             = "devops"
  description      = "Lab work"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "main" {
  repository = github_repository.devops.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true
  allows_deletions                = false

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}