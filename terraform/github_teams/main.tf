terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.36.0"
    }
  }
}

provider "github" {
  owner = var.owner
  token = var.token
}


resource "github_repository" "example_repo" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.repository_visibility
}

resource "github_team" "team_readers" {
  name = "team-readers"
  description = "Team only for pushing"
}

resource "github_team" "team_writers" {
  name = "team-writers"
  description = "Team only for pushing/pulling"
}

resource "github_team" "team_maintainers" {
  name = "team-maintainers"
  description = "Team for maintaining"
}

resource "github_team" "team_admins" {
  name = "team-admins"
  description = "Team with admin permissions"
}

resource "github_team_repository" "team_readers_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_readers.id
  permission = "pull"
}

resource "github_team_repository" "team_writers_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_writers.id
  permission = "push"
}

resource "github_team_repository" "team_admins_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_admins.id
  permission = "admin"
}

resource "github_team_repository" "team_maintainers_access" {
  repository = github_repository.example_repo.name
  team_id = github_team.team_maintainers.id
  permission = "maintain"
}