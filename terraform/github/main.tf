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
  owner = "DevopsAssignment-chiplinka"
}

resource "github_repository" "repo" {
  name               = "devops-assignment-chiplinka"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "team_smart" {
  name        = "team_smart_1"
  description = "Team 1"
}

resource "github_team" "team_silly" {
  name        = "team_silly_2"
  description = "Team 2"
}

resource "github_team_repository" "team_smart_repo" {
  team_id = github_team.team_smart.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "team_silly_repo" {
  team_id = github_team.team_silly.id
  repository = github_repository.repo.name
  permission = "admin"
}