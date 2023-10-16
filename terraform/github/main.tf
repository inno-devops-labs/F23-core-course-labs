### Main.tf ###

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
}

#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "core-course-labs" {
  name               = "core-course-labs"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
}

#Set default branch 'master'
resource "github_branch_default" "main" {
  repository = github_repository.core-course-labs.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.core-course-labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "closed_privacy_team" {
  name        = "closed_privacy_team"
  description = "closed_privacy_team"
  privacy     = "closed"
}

resource "github_team" "secret_privacy_team" {
  name        = "secret_privacy_team"
  description = "secret_privacy_team"
  privacy     = "secret"
}