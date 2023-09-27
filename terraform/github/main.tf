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

resource "github_repository" "repo" {
  name               = "inno-devops"
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

resource "github_team" "team_x" {
  name = "team_x"
  description = "Team X"
}

resource "github_team" "team_y" {
  name = "team_y"
  description = "Team Y"
}

resource "github_team_repository" "x_repo" {
  team_id = github_team.team_x.id
  repository = github_repository.repo.name
  permission = "admin"
}

resource "github_team_repository" "y_repo" {
  team_id = github_team.team_y.id
  repository = github_repository.repo.name
  permission = "push"
}