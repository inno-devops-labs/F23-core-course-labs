terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
}


resource "github_repository" "devops_course_labs" {
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
  repository = github_repository.devops_course_labs.name
  team_id    = github_team.team_pull.id
  permission = "pull"
}

resource "github_team_repository" "team_b_access" {
  repository = github_repository.devops_course_labs.name
  team_id    = github_team.team_maintain.id
  permission = "maintain"
}

resource "github_team_repository" "team_c_access" {
  repository = github_repository.devops_course_labs.name
  team_id    = github_team.team_admins.id
  permission = "admin"
}
