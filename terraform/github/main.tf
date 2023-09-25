
terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token 
}

resource "github_repository" "repo" {
  name               = "DevOps-lab4"
  description        = "This is a repository for Devops-lab4, classicClock"
  visibility         = "public"
  allow_rebase_merge = false
  allow_squash_merge = false
}

resource "github_branch_default" "repo" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
 repository_id = github_repository.repo.node_id

  pattern = github_repository.repo.default_branch

  allows_deletions                = false
  require_conversation_resolution = true
}