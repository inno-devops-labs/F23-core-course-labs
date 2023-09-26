terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.36.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
}


resource "github_repository" "example_repo" {
  name        = "ExampleRepository"
  description = "Example repo"
  visibility  = "public"
}

resource "github_team" "team_pull" {
  name = "team-pull"
}

resource "github_team" "team_push" {
  name = "team-push"
}

resource "github_team" "team_admin" {
  name = "team-admin"
}

resource "github_team_repository" "team_push_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_push.id
  permission = "push"
}

resource "github_team_repository" "team_pull_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_pull.id
  permission = "pull"
}

resource "github_team_repository" "team_admin_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_admin.id
  permission = "admin"
}