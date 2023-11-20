resource "github_repository" "repo" {
  name          = var.repo_name
  description   = "DevOps course labs at Innopolis University, Fall 2023"
  visibility    = "public"
  has_downloads = true
  has_projects  = true
  has_wiki      = true
  has_issues    = true
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

locals {
  github_teams = {
    "admins" = "admin",
    "devs"   = "push",
    "qa"     = "pull"
  }
}

resource "github_team" "team" {
  for_each = local.github_teams

  name        = each.key
  description = "Team of ${each.key}."
}

resource "github_team_repository" "team_repo" {
  for_each = local.github_teams

  team_id    = github_team.team[each.key].id
  repository = github_repository.repo.name
  permission = each.value
}

// Add owner to all teams
resource "github_team_membership" "team_membership" {
  for_each = local.github_teams

  team_id  = github_team.team[each.key].id
  username = var.owner
  role     = "maintainer"
}
