terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}


provider "github" {
} # This way terraform will look for GITHUB_TOKEN evironment variable.



resource "github_repository" "devops-labs" {
  name          = "devops-labs"
  visibility    = "public"
  has_downloads = true
  has_projects  = true
  has_wiki      = true
}


resource "github_branch_default" "devops-labs-default-branch" {
  repository = github_repository.devops-labs.name
  branch     = "main"
}


resource "github_branch_protection" "default_branch_protection" {
  repository_id  = github_repository.devops-labs.id
  enforce_admins = false
  pattern        = github_branch_default.devops-labs-default-branch.branch

  required_pull_request_reviews {
    dismiss_stale_reviews      = true
    require_code_owner_reviews = true
  }

  required_status_checks {
    strict   = true
    contexts = ["test-status-check"]
  }

}

resource "github_team" "team-1" {
  name        = "devops-team-1"
  description = "Best Devops Team"
  privacy     = "closed"
}

resource "github_team" "team-2" {
  name        = "devops-team-2"
  description = "Great Devops Team"
  privacy     = "closed"
}

resource "github_team_repository" "team-1-pull" {
  team_id    = github_team.team-1.id
  repository = github_repository.devops-labs.name
  permission = "pull" # Read access
}

resource "github_team_repository" "team-2-push" {
  team_id    = github_team.team-2.id
  repository = github_repository.devops-labs.name
  permission = "push" # Write access
}