terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = var.GITHUB_TOKEN
}

resource "github_repository" "repo" {
  name        = "devops_tf_test"
  description = "DevOps [F23]"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
  auto_init   = true
  #  license_template   = "mit"
  #  gitignore_template = "VisualStudio"
}

#Set default branch 'main'
resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "devs" {
  name                      = "devs"
  description               = "Developers Team"
  create_default_maintainer = true
}

resource "github_team" "admins" {
  name                      = "admins"
  description               = "Admins Team"
  create_default_maintainer = true
}

resource "github_team_repository" "devs_repo" {
  team_id    = github_team.devs.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "admins_repo" {
  team_id    = github_team.admins.id
  repository = github_repository.repo.name
  permission = "admin"
}
