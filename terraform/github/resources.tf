resource "github_repository" "repo" {
  name             = "devops-terraform-demo"
  description      = "Test repo to show terraform infra"
  visibility       = "public"
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "default_branch" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.default_branch.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
