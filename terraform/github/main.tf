resource "github_repository" "devops-course-test" {
  name             = "devops-course-test"
  description      = "This is cool experience at 5 am!"
  visibility       = "public"
  license_template = "mit"
}

resource "github_branch_default" "main" {
  repository = github_repository.devops-course-test.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops-course-test.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
