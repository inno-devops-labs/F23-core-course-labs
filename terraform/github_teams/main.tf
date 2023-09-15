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
  name        = "example_repo"
  description = "Example repo"
  visibility  = "public"
}

resource "github_team" "team_a" {
  name = "team-a"
}

resource "github_team" "team_b" {
  name = "team-b"
}

resource "github_team" "team_c" {
  name = "team-c"
}

resource "github_team_repository" "team_a_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_a.id
  permission = "pull"
}

resource "github_team_repository" "team_b_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_b.id
  permission = "push"
}

resource "github_team_repository" "team_c_access" {
  repository = github_repository.example_repo.name
  team_id    = github_team.team_c.id
  permission = "admin"
}
