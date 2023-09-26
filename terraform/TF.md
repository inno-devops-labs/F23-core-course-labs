# Best practices
* Use `terraform fmt` to update configurations for readiability and consistency
* Use `terraform validate` to validate current configurations
* Use `terraform plan` before each apply
* Use terraform variables
* Do not put sensitive data into configuration

# Docker
## Command outputs
### 'terraform apply':
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform apply
docker_image.moscow_time_app: Refreshing state... [id=sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest]
docker_container.moscow_time_app: Refreshing state... [id=12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851]

No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are
needed.

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

container_id = "12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851"
image_id = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest"
```

#### `terraform state list`:
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform state list
docker_container.moscow_time_app
docker_image.moscow_time_app
```

#### `terraform state show` (image)
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform state show docker_image.moscow_time_app
# docker_image.moscow_time_app:
resource "docker_image" "moscow_time_app" {
    id           = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest"
    image_id     = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784"
    keep_locally = false
    name         = "edikgoose/moscow-time-app:latest"
    repo_digest  = "edikgoose/moscow-time-app@sha256:d102a3c2fbb0cbc9485790c55bbff31a7e8ddf82894dc555152e59eb673bf0ae"
}
```

#### `terraform state show` (container)
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform state show docker_container.moscow_time_app
# docker_container.moscow_time_app:
resource "docker_container" "moscow_time_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "uvicorn",
        "src.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "80",
    ]
    env                                         = []
    hostname                                    = "12cd47cdc1f3"
    id                                          = "12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851"
    image                                       = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-app"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

#### `terraform output`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform output
container_id = "12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851"
image_id = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest"
```





# Yandex Cloud
#### `terraform apply`
```
data.yandex_vpc_subnet.default_a: Reading...
data.yandex_compute_image.last_ubuntu: Reading...
data.yandex_compute_image.last_ubuntu: Read complete after 2s [id=fd80bm0rh4rkepi5ksdi]
data.yandex_vpc_subnet.default_a: Read complete after 2s [id=e9b72g6d4u511tmovhe2]
yandex_compute_instance.default: Refreshing state... [id=fhm2ap4ib1f29d1j06e0]

Changes to Outputs:
  + default_instance_public_ip = "158.160.33.18"
  + last_ubuntu                = "fd80bm0rh4rkepi5ksdi"
  + subnet_id                  = "e9b72g6d4u511tmovhe2"

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

default_instance_public_ip = "158.160.33.18"
last_ubuntu = "fd80bm0rh4rkepi5ksdi"
subnet_id = "e9b72g6d4u511tmovhe2"
```

#### `terraform state list`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state list
data.yandex_compute_image.last_ubuntu
data.yandex_vpc_subnet.default_a
yandex_compute_instance.default
```

#### `terraform state show data.yandex_compute_image.last_ubuntu`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state show data.yandex_compute_image.last_ubuntu
# data.yandex_compute_image.last_ubuntu:
data "yandex_compute_image" "last_ubuntu" {
    created_at    = "2023-09-25T10:53:45Z"
    description   = "ubuntu 22.04 lts"
    family        = "ubuntu-2204-lts"
    folder_id     = "standard-images"
    id            = "fd80bm0rh4rkepi5ksdi"
    image_id      = "fd80bm0rh4rkepi5ksdi"
    labels        = {}
    min_disk_size = 8
    name          = "ubuntu-22-04-lts-v20230925"
    os_type       = "linux"
    pooled        = true
    product_ids   = [
        "f2e3vsap4cmi4pqk05lg",
    ]
    size          = 7
    status        = "ready"
}
```

#### `terraform state show data.yandex_vpc_subnet.default_a`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state show data.yandex_vpc_subnet.default_a
# data.yandex_vpc_subnet.default_a:
data "yandex_vpc_subnet" "default_a" {
    created_at     = "2023-08-27T19:33:37Z"
    description    = "Auto-created default subnet for zone ru-central1-a in default"
    dhcp_options   = []
    folder_id      = "b1gm00gpfqn5aiom8dn1"
    id             = "e9b72g6d4u511tmovhe2"
    labels         = {}
    name           = "default-ru-central1-a"
    network_id     = "enp98kt2klp1tl362ntp"
    subnet_id      = "e9b72g6d4u511tmovhe2"
    v4_cidr_blocks = [
        "10.128.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

#### `terraform state show yandex_compute_instance.default`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state show yandex_compute_instance.default
# yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    created_at                = "2023-09-25T22:19:29Z"
    folder_id                 = "b1gm00gpfqn5aiom8dn1"
    fqdn                      = "fhm2ap4ib1f29d1j06e0.auto.internal"
    id                        = "fhm2ap4ib1f29d1j06e0"
    labels                    = {}
    metadata                  = {}
    name                      = "edikgoose-instance"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm9ff8onv3bhgc28hmq"
        disk_id     = "fhm9ff8onv3bhgc28hmq"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd80bm0rh4rkepi5ksdi"
            size       = 8
            type       = "network-hdd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "10.128.0.22"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:25:64:92:58"
        nat                = true
        nat_ip_address     = "158.160.33.18"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b72g6d4u511tmovhe2"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 5
        cores         = 2
        gpus          = 0
        memory        = 1
    }

    scheduling_policy {
        preemptible = false
    }
}
```

#### `terraform output`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform output
default_instance_public_ip = "158.160.33.18"
last_ubuntu = "fd80bm0rh4rkepi5ksdi"
subnet_id = "e9b72g6d4u511tmovhe2"
```


# GitHub 
#### `terraform state list`:
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github$ terraform state list
github_branch_default.imported_main
github_branch_default.main
github_branch_protection.default
github_repository.iu-devops-test-imported-repo
github_repository.repo
```


#### terraform state show github_repository.iu-devops-test-imported-repo
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github$ terraform state show github_repository.iu-devops-test-imported-repo
# github_repository.iu-devops-test-imported-repo:
resource "github_repository" "iu-devops-test-imported-repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Imported repo"
    etag                        = "W/\"1818683ee6ad7c98c7270648d99913434594a4cb7bcbcebfc75aa5de04759263\""
    full_name                   = "edikgoose/iu-devops-test-imported-repository"
    git_clone_url               = "git://github.com/edikgoose/iu-devops-test-imported-repository.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/edikgoose/iu-devops-test-imported-repository"
    http_clone_url              = "https://github.com/edikgoose/iu-devops-test-imported-repository.git"
    id                          = "iu-devops-test-imported-repository"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "iu-devops-test-imported-repository"
    node_id                     = "R_kgDOKYngEA"
    private                     = false
    repo_id                     = 696901648
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:edikgoose/iu-devops-test-imported-repository.git"
    svn_url                     = "https://github.com/edikgoose/iu-devops-test-imported-repository"
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


#### `terraform state show github_repository.repo`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github$ terraform state show github_repository.repo
# github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Test repository created by terraform"
    etag                        = "W/\"b91a35541abb5d2a6c40047f95100393df04d9793897c07eb049b178a379f3be\""
    full_name                   = "edikgoose/iu-devops-test"
    git_clone_url               = "git://github.com/edikgoose/iu-devops-test.git"
    gitignore_template          = "Terraform"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/edikgoose/iu-devops-test"
    http_clone_url              = "https://github.com/edikgoose/iu-devops-test.git"
    id                          = "iu-devops-test"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "iu-devops-test"
    node_id                     = "R_kgDOKYnT7A"
    private                     = false
    repo_id                     = 696898540
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:edikgoose/iu-devops-test.git"
    svn_url                     = "https://github.com/edikgoose/iu-devops-test"
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

#### `terraform output`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github$ terraform output
repository_default_branch_name = "main"
repository_full_name = "edikgoose/iu-devops-test"
```



# GitHub Teams

#### `terraform apply`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github_teams$ terraform apply
github_repository.example_repo: Refreshing state... [id=iu-devops-teams-test]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected
this plan:

  # github_repository.example_repo has been deleted
  - resource "github_repository" "example_repo" {
        id                          = "iu-devops-teams-test"
      - name                        = "iu-devops-teams-test" -> null
        # (32 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the
following plan may include actions to undo or respond to these changes.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # github_repository.example_repo will be created
  + resource "github_repository" "example_repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Test repository for teams created by terraform"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "iu-devops-teams-test"
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

  # github_team.team_admins will be created
  + resource "github_team" "team_admins" {
      + create_default_maintainer = false
      + description               = "Team with admin permissions"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-admins"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team_maintainers will be created
  + resource "github_team" "team_maintainers" {
      + create_default_maintainer = false
      + description               = "Team for maintaining"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-maintainers"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team_readers will be created
  + resource "github_team" "team_readers" {
      + create_default_maintainer = false
      + description               = "Team only for pushing"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-readers"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team_writers will be created
  + resource "github_team" "team_writers" {
      + create_default_maintainer = false
      + description               = "Team only for pushing/pulling"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-writers"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team_repository.team_admins_access will be created
  + resource "github_team_repository" "team_admins_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "iu-devops-teams-test"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_maintainers_access will be created
  + resource "github_team_repository" "team_maintainers_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "iu-devops-teams-test"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_readers_access will be created
  + resource "github_team_repository" "team_readers_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "pull"
      + repository = "iu-devops-teams-test"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_writers_access will be created
  + resource "github_team_repository" "team_writers_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "iu-devops-teams-test"
      + team_id    = (known after apply)
    }

Plan: 9 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.team_readers: Creating...
github_team.team_admins: Creating...
github_team.team_writers: Creating...
github_team.team_maintainers: Creating...
github_repository.example_repo: Creating...
github_team.team_readers: Still creating... [10s elapsed]
github_team.team_admins: Still creating... [10s elapsed]
github_team.team_writers: Still creating... [10s elapsed]
github_team.team_maintainers: Still creating... [10s elapsed]
github_repository.example_repo: Still creating... [10s elapsed]
github_team.team_readers: Creation complete after 18s [id=8645633]
github_team.team_writers: Still creating... [20s elapsed]
github_team.team_admins: Still creating... [20s elapsed]
github_team.team_maintainers: Still creating... [20s elapsed]
github_repository.example_repo: Still creating... [20s elapsed]
github_team.team_admins: Creation complete after 25s [id=8645635]
github_team.team_maintainers: Creation complete after 26s [id=8645636]
github_team.team_writers: Creation complete after 26s [id=8645638]
github_repository.example_repo: Creation complete after 27s [id=iu-devops-teams-test]
github_team_repository.team_writers_access: Creating...
github_team_repository.team_maintainers_access: Creating...
github_team_repository.team_readers_access: Creating...
github_team_repository.team_admins_access: Creating...
github_team_repository.team_writers_access: Creation complete after 6s [id=8645638:iu-devops-teams-test]
github_team_repository.team_admins_access: Creation complete after 7s [id=8645635:iu-devops-teams-test]
github_team_repository.team_maintainers_access: Creation complete after 7s [id=8645636:iu-devops-teams-test]
github_team_repository.team_readers_access: Creation complete after 8s [id=8645633:iu-devops-teams-test]

Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
```

#### `terraform state list`

```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github_teams$ terraform state list
github_repository.example_repo
github_team.team_admins
github_team.team_maintainers
github_team.team_readers
github_team.team_writers
github_team_repository.team_admins_access
github_team_repository.team_maintainers_access
github_team_repository.team_readers_access
github_team_repository.team_writers_access
```

#### `terraform state show github_team.team_admins`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github_teams$ terraform state show github_team.team_admins
# github_team.team_admins:
resource "github_team" "team_admins" {
    create_default_maintainer = false
    description               = "Team with admin permissions"
    etag                      = "W/\"4e46ac8c282722606239945460eb99726e16b4e5d3de277ec366bc0e76d704b1\""
    id                        = "8645635"
    members_count             = 0
    name                      = "team-admins"
    node_id                   = "T_kwDOCLWkT84Ag-wD"
    privacy                   = "secret"
    slug                      = "team-admins"
}
```

#### `terraform state show github_team.team_readers`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github_teams$ terraform state show github_team.team_readers
# github_team.team_readers:
resource "github_team" "team_readers" {
    create_default_maintainer = false
    description               = "Team only for pushing"
    etag                      = "W/\"cea20932faf1713d97b67163d07e76a3d3418940d0c6ae4bd3d8bbaa981851dc\""
    id                        = "8645633"
    members_count             = 0
    name                      = "team-readers"
    node_id                   = "T_kwDOCLWkT84Ag-wB"
    privacy                   = "secret"
    slug                      = "team-readers"
}
```

#### `terraform state show github_team.team_writers`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github_teams$ terraform state show github_team.team_writers
# github_team.team_writers:
resource "github_team" "team_writers" {
    create_default_maintainer = false
    description               = "Team only for pushing/pulling"
    etag                      = "W/\"bd4c8b2bf11658d19ce5ba74c676de5435851e6a60b17967097768b940fe8bf3\""
    id                        = "8645638"
    members_count             = 0
    name                      = "team-writers"
    node_id                   = "T_kwDOCLWkT84Ag-wG"
    privacy                   = "secret"
    slug                      = "team-writers"
}
```

#### `terraform state show github_team.team_maintainers`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/github_teams$ terraform state show github_team.team_maintainers
# github_team.team_maintainers:
resource "github_team" "team_maintainers" {
    create_default_maintainer = false
    description               = "Team for maintaining"
    etag                      = "W/\"279bf081efa93749e1c2398bb5fb922f117463ef285953477686099f0a7ccb0d\""
    id                        = "8645636"
    members_count             = 0
    name                      = "team-maintainers"
    node_id                   = "T_kwDOCLWkT84Ag-wE"
    privacy                   = "secret"
    slug                      = "team-maintainers"
}
```