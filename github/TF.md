Result of ```terraform show```:

```
# github_branch_default.master:
resource "github_branch_default" "master" {
    branch     = "main"
    id         = "new-devops-repo"
    rename     = false
    repository = "new-devops-repo"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    force_push_bypassers            = []
    id                              = "BPR_kwDOKYpscM4CgU14"
    lock_branch                     = false
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "new-devops-repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# github_repository.new-devops-repo:
resource "github_repository" "new-devops-repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "My awesome homework"
    etag                        = "W/\"f11d45329af9c6e60e123b3f0bc0f74a494839a7df18c8531b579934dfb8f044\""
    full_name                   = "Wild-Queue/new-devops-repo"
    git_clone_url               = "git://github.com/Wild-Queue/new-devops-repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Wild-Queue/new-devops-repo"
    http_clone_url              = "https://github.com/Wild-Queue/new-devops-repo.git"
    id                          = "new-devops-repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "new-devops-repo"
    node_id                     = "R_kgDOKYpscA"
    private                     = false
    repo_id                     = 696937584
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Wild-Queue/new-devops-repo.git"
    svn_url                     = "https://github.com/Wild-Queue/new-devops-repo"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
```

Result of ```terraform state list```
```
github_branch_default.master
github_branch_protection.default
github_repository.new-devops-repo
```


### Best practices been used:

1. Using Variables: The usage of variables for configurable values allows for easy customization and separation of sensitive information from the code.

2. Visibility and Description: The visibility and description attributes are set in the github_repository resource block to specify the visibility and description of the GitHub repository being created. 

3. Code Organization: The code is well-organized with clear file splitting 

4. Documentation: The code includes helpful comments that explain the purpose and functionality of each resource block and configuration. 

5. Specify resource dependencies explicitly: In the code, the branch protection rule (github_branch_protection) depends on the default branch (github_branch_default). 

6. Use version control and code repositories: The code uses a public GitHub repository to store the Terraform configuration and version control. 

7. Use of Data Sources: Data sources are used to fetch information about compute flavors, images, and networks. 

8. Use of Authentication and Authorization: The provider configuration includes authentication details such as username, password, project ID, and auth URL.

9. Utilizing Version Constraints: In the terraform block, the required_providers attribute is used to specify the version and source of the required provider. 

10. Organized Provider Configuration: The provider block is used to configure the docker provider.The provider configuration is specified separately from the resource definitions. 

11. Resource Naming Convention: The resource names follow a naming convention that helps identify the type of resource and its purpose.