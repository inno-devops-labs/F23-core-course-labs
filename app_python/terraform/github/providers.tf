terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  owner = "Arseniy172-test-org"
  token = var.token # or `GITHUB_TOKEN`
}
