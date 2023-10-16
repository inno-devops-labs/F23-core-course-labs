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

resource "github_repository" "repo" {
  name        = var.repo_name
  description = var.repo_description
  visibility  = "public"
}

resource "github_team" "first_team" {
  name = var.team_1
}

resource "github_team" "second_team" {
  name = var.team_2
}

resource "github_team" "third_team" {
  name = var.team_3
}

resource "github_team_repository" "team_1_access" {
  repository = github_repository.repo.name
  team_id    = github_team.first_team.id
  permission = "pull"
}

resource "github_team_repository" "team_2_access" {
  repository = github_repository.repo.name
  team_id    = github_team.second_team.id
  permission = "push"
}

resource "github_team_repository" "team_3_access" {
  repository = github_repository.repo.name
  team_id    = github_team.third_team.id
  permission = "admin"
}