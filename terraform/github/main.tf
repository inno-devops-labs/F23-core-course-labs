resource "github_repository" "repo" {
  name               = "devops_course"
  description        = "Lab 4: Terraform and its things"
  visibility         = "public"
  has_issues         = false
  has_wiki           = true
  allow_rebase_merge = false
  allow_squash_merge = false
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true
}

resource "github_repository" "fpga_repository" {
  description = "Innopolis FPGA course repository"
  auto_init   = true
  name        = "FPGA"
  visibility  = "public"
}

resource "github_branch_default" "fpga_repository_master" {
  repository = github_repository.fpga_repository.name
  branch     = "master"
}