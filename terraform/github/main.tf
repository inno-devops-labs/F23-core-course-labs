terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "devops_course_labs" {
  name = "my-core-course-labs"
  description = "Solutions for the DevOps course"
  visibility = "public"
}

# make the default branch main 
resource "github_branch_default" "main" {
  repository = github_repository.devops_course_labs.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops_course_labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}