resource "github_team" "devops_team" {
  name        = "devops"
  description = "Do devops."
}

resource "github_team" "programmers_team" {
  name        = "programmers"
  description = "Do coding."
}

resource "github_team_repository" "add_devops" {
  team_id    = github_team.devops_team.id
  repository = github_repository.devops-course-test.name
  permission = "push"
}

resource "github_team_repository" "add_programmers" {
  team_id    = github_team.programmers_team.id
  repository = github_repository.devops-course-test.name
  permission = "admin"
}