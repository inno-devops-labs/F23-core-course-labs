resource "github_repository" "repo" {
  name               = "IU-Devops-demo-repo"
  description        = "demo repo"
  visibility         = "public"
  auto_init          = true
  has_issues         = true
  has_wiki           = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_branch_default" "repo_default" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.repo_default.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
