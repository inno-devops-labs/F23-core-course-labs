# Terraform

## Best Practises

- **Leverage _variables.tf_**:
Embrace the use of variables.tf to centralize and parameterize your configuration. This approach streamlines code modification, encourages flexibility, and supports scalability by allowing you to adjust settings without altering the underlying code.
- **Naming Conventions**:
Maintain a standardized naming convention across your Terraform codebase.
- **Secure Sensitive Data with _terraform.tfvars_**:
Safeguard sensitive information, such as passwords or API keys, by securely storing them in variables.tf or using Terraform-specific mechanisms like environment variables or secret management systems.
- **Utilize _output.tf_**:
Employ output.tf files to expose specific values or metadata from your infrastructure code after it has been applied.


## Docker

Check terraform state
```shell
terraform state list
```

Output:
```text
docker_container.app_python
docker_image.app_python
```

Check terraform show
```shell
terraform show
```

Output:
```text
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "-m",
        "uvicorn",
        "app_python.src.main:app",
        "--port",
        "8000",
    ]
    env                                         = []
    hostname                                    = "bab3ba3fabbd"
    id                                          = "bab3ba3fabbdcda7d1b12169819e7a088225e28f8b7900502087edf2d949d5b8"
    image                                       = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "default"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "0"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7yesliesnayder/app_python:1.0.3"
    image_id     = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7"
    keep_locally = false
    name         = "yesliesnayder/app_python:1.0.3"
    repo_digest  = "yesliesnayder/app_python@sha256:9c84ea15c98a163ee74f03fd1f586ecb1e746ce4653ac02a6eeae3f53d13d54c"
}
```

Check output:
```shell
terraform output
```

Output:
```text
container_id = "99ea9eb8ee2f7bcec45dc0665286b708d5e8f1eda6cb179d3a5297639851a2d0"
image_id = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7yesliesnayder/app_python:1.0.3"
```

## GitHub

```shell
terraform plan
```

Output:
```text
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "test-repo-yesliesnayder"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Test repository which was created on GitHub by Terraform"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "test-repo-yesliesnayder"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
    }

  # github_team.my_team_1 will be created
  + resource "github_team" "my_team_1" {
      + create_default_maintainer = false
      + description               = "Team 1"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "my_team_1"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.my_team_2 will be created
  + resource "github_team" "my_team_2" {
      + create_default_maintainer = false
      + description               = "Team 2"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "my_team_2"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team_repository.team_1_repo will be created
  + resource "github_team_repository" "team_1_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "test-repo-yesliesnayder"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_2_repo will be created
  + resource "github_team_repository" "team_2_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "test-repo-yesliesnayder"
      + team_id    = (known after apply)
    }
```

Check state list:
```shell
terraform state list
```

Output:
```text
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

## Yandex Cloud

```shell
terraform plan
```

Output:
```text
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.vm_1 will be created
  + resource "yandex_compute_instance" "vm_1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + name                      = "my-vm-1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd80bm0rh4rkepi5ksdi"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = "e9bdavfejkdr6h3r6ath"
        }

      + resources {
          + core_fraction = 5
          + cores         = 2
          + memory        = 1
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + default_instance_public_ip = (known after apply)
  + last_ubuntu                = "fd80bm0rh4rkepi5ksdi"
  + subnet_id                  = "e9bdavfejkdr6h3r6ath"
```