terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  owner = "lnsfna-organization"
  token = var.token
}

resource "github_repository" "terraform" {
  name             = "DevOpsCourse"
  description      = "DevOps course labs"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
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

resource "github_team" "team1" {
  name        = "team1"
  description = "test team 1"
}

resource "github_team" "team2" {
  name        = "team2"
  description = "test team 2"
}

resource "github_team_repository" "team_1_to_repo" {
    team_id = github_team.team1.id
    repository = github_repository.terraform.name
    permission = "pull"
}

resource "github_team_repository" "team_2_to_repo" {
    team_id = github_team.team2.id
    repository = github_repository.terraform.name
    permission = "admin"
}