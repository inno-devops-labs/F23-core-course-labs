
locals {
  github_repositories = [
    {
      name               = github_repository.bphosting.name
      description        = github_repository.bphosting.description
      visibility         = github_repository.bphosting.visibility
      default_branch     = github_branch_default.bphosting_default.branch
      branch_protection_rule = github_branch_protection.bphosting_main.id
    },
  ]
}

output "repositories" {
  value = local.github_repositories
}


