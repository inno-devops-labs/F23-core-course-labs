resource "github_repository" "repo" {
  name          = "core-course-labs"
  description   = "DevOps course labs at Innopolis University, Fall 2023"
  visibility    = "public"
  has_downloads = true
  has_projects  = true
  has_wiki      = true
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
