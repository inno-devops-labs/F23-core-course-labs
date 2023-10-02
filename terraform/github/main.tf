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

resource "github_team" "dev_team" {
  name        = "Developers"
  description = "Software Developers team"
}

resource "github_team" "bus_team" {
  name        = "Business"
  description = "Business-people team"
}

resource "github_team_repository" "dev_team_access" {
  repository = github_repository.repo.name
  team_id    = github_team.dev_team.id
  permission = "push"
}

resource "github_team_repository" "bus_team_access" {
  repository = github_repository.repo.name
  team_id    = github_team.bus_team.id
  permission = "admin"
}