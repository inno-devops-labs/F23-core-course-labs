terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
  token = var.github_token
}


resource "github_repository" "gh_teams_terraform" {
  name = "gh-teams-terraform"
  description = "gh teams using terraform"
  visibility = "public"
}

resource "github_team" "team_pull" {
  name = "team-pull"
}

resource "github_team" "team_maintain" {
  name = "team-push"
}

resource "github_team" "team_admins" {
  name = "team-admins"
}

resource "github_team_repository" "team_a_access" {
  repository = github_repository.gh_teams_terraform.name
  team_id    = github_team.team_pull.id
  permission = "pull"
}

resource "github_team_repository" "team_b_access" {
  repository = github_repository.gh_teams_terraform.name
  team_id    = github_team.team_maintain.id
  permission = "maintain"
}

resource "github_team_repository" "team_c_access" {
  repository = github_repository.gh_teams_terraform.name
  team_id    = github_team.team_admins.id
  permission = "admin"
}
