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
  name               = "test-repo-yesliesnayder"
  description        = "Test repository which was created on GitHub by Terraform"
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

resource "github_team" "my_team_1" {
  name        = "my_team_1"
  description = "Team 1"
}

resource "github_team" "my_team_2" {
  name        = "my_team_2"
  description = "Team 2"
}

resource "github_team_repository" "team_1_repo" {
  team_id = github_team.my_team_1.id
  repository = github_repository.repo.name
  permission = "admin"
}

resource "github_team_repository" "team_2_repo" {
  team_id = github_team.my_team_2.id
  repository = github_repository.repo.name
  permission = "push"
}