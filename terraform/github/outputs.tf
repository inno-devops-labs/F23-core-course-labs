#output "repository_name" {
#value = github_repository.repo.name
#}

#output "repository_description" {
#value = github_repository.repo.description
#}

#output "repository_visibility" {
#value = github_repository.repo.visibility
#}

#output "default_branch" {
#value = github_branch_default.default.branch
#}

#output "branch_protection_rule" {
#value = github_branch_protection.main.id
#}

#output "repositories" {
#value = {
#for repo_name, repo_config in github_repository.repos:
#repo_name => {
#name        = repo_config.name
#description = repo_config.description
#visibility  = repo_config.visibility
#default_branch = github_branch_default.default[repo_name].branch
#branch_protection_rule = github_branch_protection.main[repo_name].id
#}
#}
#}

#output "repositories" {
#value = {
#for repo_name, repo_config in data.terraform_remote_state.default_state.outputs.github_repositories :
#repo_name => {
#name               = repo_config.name
#description        = repo_config.description
#visibility         = repo_config.visibility
#default_branch     = repo_config.default_branch
#branch_protection_rule = repo_config.branch_protection_rule
#}
#}
#}


locals {
  github_repositories = [
    {
      name                   = github_repository.repo.name
      description            = github_repository.repo.description
      visibility             = github_repository.repo.visibility
      default_branch         = github_branch_default.repo_default.branch
      branch_protection_rule = github_branch_protection.repo_main.id
    },
    {
      name           = github_repository.course.name
      description    = github_repository.course.description
      visibility     = github_repository.course.visibility
      default_branch = github_branch_default.course_default.branch
    }
  ]
}

output "repositories" {
  value = local.github_repositories
}


