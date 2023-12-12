resource "github_repository" "repo" {
  name        = "devops"
  description = "Assigments for DevOps course"
  visibility  = "public"
  has_issues  = false
  has_wiki    = true
  auto_init   = true
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "teamA" {
  name        = "some-team-a"
  description = "Some cool team A"
}

resource "github_team" "teamB" {
  name        = "some-team-b"
  description = "Some cool team B"
}

resource "github_team_repository" "team_a_to_repo" {
    team_id = github_team.teamA.id
    repository = github_repository.repo.name
    permission = "pull"
}

resource "github_team_repository" "team_b_to_repo" {
    team_id = github_team.teamB.id
    repository = github_repository.repo.name
    permission = "admin"
}