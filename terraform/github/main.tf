resource "github_repository" "repo" {
  name          = "devops-course-labs-infrastructure"
  description   = "Solutions for DevOps course labs"
  visibility    = "public"
  has_downloads = true
  has_projects  = true
  has_wiki      = true
  license_template   = "mit"
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
  teams = {
    "Developers" = "Software Developers team",
    "Business"   = "Business-people team"
  }
}

resource "github_team" "team" {
  for_each = local.teams

  name        = each.key
  description = each.value
}

resource "github_team_repository" "team_repo" {
  for_each = local.teams

  team_id    = github_team.team[each.key].id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_membership" "membership" {
  for_each = local.teams

  team_id  = github_team.team[each.key].id
  username = "vladimirKa002"
  role     = "maintainer"
}