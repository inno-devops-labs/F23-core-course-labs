terraform {
  required_providers { 
    github = {
      source  = "integrations/github"
      version = "~> 5.3"
    }
  }
}


provider "github" {
  token = var.github_token
}


#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {
  name               = "DevOps-Demo-Repo-2023"
  description        = "Automatically provisioned codebase"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'main'
resource "github_branch_default" "repo_default" {
  repository = github_repository.repo.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "repo_main" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.repo_default.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_repository" "course" {
	name = "core-course-labs"
	auto_init = true
	#allow_update_branch = true
}

resource "github_branch_default" "course_default" {
  repository = github_repository.course.name
  branch     = "main"
}


# Retrieve information about the currently authenticated user.
data "github_user" "current" {
  username = ""
}

