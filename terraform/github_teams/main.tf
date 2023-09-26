terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.36.0"
    }
  }
}

provider "github" {
  owner = var.organization
}

resource "github_repository" "github_repo" {
  name        = var.name
  description = var.description
  visibility  = "public"
}

resource "github_team" "team_1" {
  name = var.team_name_1
}

resource "github_team" "team_2" {
  name = var.team_name_2
}

resource "github_team" "team_3" {
  name = var.team_name_3
}

resource "github_team_repository" "access_1" {
  repository = github_repository.github_repo.name
  team_id    = github_team.team_1.id
  permission = "pull"
}

resource "github_team_repository" "access_2" {
  repository = github_repository.github_repo.name
  team_id    = github_team.team_2.id
  permission = "push"
}

resource "github_team_repository" "access_3" {
  repository = github_repository.github_repo.name
  team_id    = github_team.team_3.id
  permission = "admin"
}
