# Terraform configuration for managing GitHub repositories

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
  required_version = ">= 0.13"
}

provider "github" {
  owner = "iu-devops-test-org"
  token = var.github_access_token
}

# Organization teams setup
resource "github_team" "team-alpha" {
  name        = "team-alpha"
  description = "This is Team Alpha"
  privacy     = "closed"
}

resource "github_team" "team-bravo" {
  name        = "team-bravo"
  description = "This is Team Bravo"
  privacy     = "closed"
}

resource "github_team" "team-devops" {
  name        = "team-devops"
  description = "This is Team DevOps"
  privacy     = "closed"
}

###### Below, we setup new repo from the first half of Task 2 ###### 

# Create and initialize a public GitHub Repository with MIT license and a Python .gitignore file (incl. issues and wiki)
resource "github_repository" "tfrepo" {
  name               = "tfrepo"
  description        = "My Terraform Created repo"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}

# Set default branch 'master'
resource "github_branch_default" "main" {
  repository = github_repository.tfrepo.name
  branch     = "main"
}

# Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.tfrepo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

 ####### Below, we will configure a repo for the second half of Task 2 (that is, core-course-labs) #######

# Create a resource record for the my repository with labs. The repository will be updated according to this resource record
resource "github_repository" "core-course-labs" {
  name               = "core-course-labs"
  description        = "This repo description was updated by Terraform!"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
}

resource "github_branch_default" "main-core-course-labs" {
  repository = github_repository.core-course-labs.name
  branch     = "main"
}

# Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default-core-course-labs" {
  repository_id                   = github_repository.core-course-labs.id
  pattern                         = github_branch_default.main-core-course-labs.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

#### Bonus: set teams' permission on core-course-labs repo

resource "github_team_repository" "team-alpha-core-course-labs" {
  # team alpha is very cool and has write access to the repo
  team_id    = github_team.team-alpha.id
  repository = github_repository.core-course-labs.name
  permission = "push"
}

resource "github_team_repository" "team-bravo-core-course-labs" {
  # team bravo is not as cool and only has read access to the repo
  team_id    = github_team.team-bravo.id
  repository = github_repository.core-course-labs.name
  permission = "pull"
}

resource "github_team_repository" "team-devops-core-course-labs" {
  # team devops transcend every other team in coolness and has admin access to the repo
  team_id    = github_team.team-devops.id
  repository = github_repository.core-course-labs.name
  permission = "admin"
}