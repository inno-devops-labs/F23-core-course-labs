terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.3"
    }
  }
}


provider "github" {
  owner = var.github_organization
  token = var.github_token
}


resource "github_team" "dev" {
  name        = "Development Team"
  description = "They never follow best practices"
  privacy     = "closed"
}

resource "github_team" "devops" {
  name        = "DevOps Team"
  description = "The DevOps team in the GitHub organization facilitates seamless collaboration and automation to optimize software development and deployment processes."
  privacy     = "closed"
}

#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "bphosting" {
  name               = "bphosting"
  description        = ""
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'main'
resource "github_branch_default" "bphosting_default" {
  repository = github_repository.bphosting.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "bphosting_main" {
  repository_id                   = github_repository.bphosting.id
  pattern                         = github_branch_default.bphosting_default.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}



resource "github_team_repository" "dev_bphosting" {
  team_id    = github_team.dev.id
  repository = github_repository.bphosting.name
  permission = "push"
}

resource "github_team_repository" "devops_bphosting" {
  team_id    = github_team.devops.id
  repository = github_repository.bphosting.name
  permission = "maintain"
}

