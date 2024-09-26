#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "new-devops-repo" {
  name               = "new-devops-repo"
  description        = "lab4"
  visibility         = "public"
  has_issues         = true
}

#Set default branch 'master'
resource "github_branch_default" "master" {
  repository = github_repository.new-devops-repo.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.new-devops-repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
