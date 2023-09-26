# Terraform

## Terraform best practices
- Use outputs to highlight important information.
- Use modules to organize the code and enable the use of concise commands.
- Specify versions of all providers to ensure reliability.
- Keep state files out of version control.
- The use of variables to increase flexibility.
- Sensitive information as environment variables.
- `.gitignore` for terraform-specific files.
- `import` blocks to automate imports.

## list
    terraform state list

Output:

    module.app-python.docker_image.app_python_image
    module.github.github_branch_default.main
    module.github.github_repository.devops_course_labs
    module.github-teams.github_repository.gh_teams_terraform
    module.github-teams.github_team.team_admins
    module.github-teams.github_team.team_maintain
    module.github-teams.github_team.team_pull
    module.github-teams.github_team_repository.team_a_access
    module.github-teams.github_team_repository.team_b_access
    module.github-teams.github_team_repository.team_c_access
    module.yandex-cloud.yandex_compute_instance.vm-1
    module.yandex-cloud.yandex_compute_instance.vm-2
    module.yandex-cloud.yandex_vpc_network.network-1
    module.yandex-cloud.yandex_vpc_subnet.subnet-1



## show
    terraform show

Output:

    # module.app-python.docker_image.app_python_image:
    resource "docker_image" "app_python_image" {
        id           = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1ekurohata7/devops_msk_time"
        image_id     = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1e"
        keep_locally = false
        name         = "kurohata7/devops_msk_time"
        repo_digest  = "kurohata7/devops_msk_time@sha256:48cb36f3e629274d373801220166f4382848272e7b69d1d6e3e49384ffb51681"
    }
    # module.github.github_branch_default.main:
    resource "github_branch_default" "main" {
        branch     = "main"
        id         = "devops-course-labs"
        repository = "devops-course-labs"
    }

    # module.github.github_repository.devops_course_labs:
    resource "github_repository" "devops_course_labs" {
        allow_auto_merge            = false
        allow_merge_commit          = true
        allow_rebase_merge          = true
        allow_squash_merge          = true
        archived                    = false
        auto_init                   = false
        branches                    = [
            {
                name      = "lab1"
                protected = false
            },
            {
                name      = "lab2"
                protected = false
            },
            {
                name      = "lab3"
                protected = false
            },
            {
                name      = "lab4"
                protected = false
            },
            {
                name      = "main"
                protected = true
            },
        ]
        default_branch              = "main"
        delete_branch_on_merge      = false
        description                 = "Lab solutions for DevOps course at IU"
        etag                        = "W/\"0b3a3eefbe3efbacd3e1bb9e53ea35ba0d4504cb0ae08c48f904574f7d2ed1bc\""
        full_name                   = "KuronoSangatsu7/devops-course-labs"
        git_clone_url               = "git://github.com/KuronoSangatsu7/devops-course-labs.git"
        has_downloads               = false
        has_issues                  = false
        has_projects                = false
        has_wiki                    = false
        html_url                    = "https://github.com/KuronoSangatsu7/devops-course-labs"
        http_clone_url              = "https://github.com/KuronoSangatsu7/devops-course-labs.git"
        id                          = "devops-course-labs"
        is_template                 = false
        merge_commit_message        = "PR_TITLE"
        merge_commit_title          = "MERGE_MESSAGE"
        name                        = "devops-course-labs"
        node_id                     = "R_kgDOKORFSQ"
        private                     = false
        repo_id                     = 686048585
        squash_merge_commit_message = "COMMIT_MESSAGES"
        squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
        ssh_clone_url               = "git@github.com:KuronoSangatsu7/devops-course-labs.git"
        svn_url                     = "https://github.com/KuronoSangatsu7/devops-course-labs"
        topics                      = []
        visibility                  = "public"
        vulnerability_alerts        = false
    }
    # module.github-teams.github_repository.gh_teams_terraform:
    resource "github_repository" "gh_teams_terraform" {
        allow_auto_merge            = false
        allow_merge_commit          = true
        allow_rebase_merge          = true
        allow_squash_merge          = true
        archived                    = false
        branches                    = []
        default_branch              = "main"
        delete_branch_on_merge      = false
        description                 = "gh teams using terraform"
        etag                        = "W/\"f453df947905aca7ff43927897c156f3b9052d1a8e7c60ccacc269788e35c177\""
        full_name                   = "FirstRaccoonInaTrenchCoat/gh-teams-terraform"
        git_clone_url               = "git://github.com/FirstRaccoonInaTrenchCoat/gh-teams-terraform.git"
        has_downloads               = false
        has_issues                  = false
        has_projects                = false
        has_wiki                    = false
        html_url                    = "https://github.com/FirstRaccoonInaTrenchCoat/gh-teams-terraform"
        http_clone_url              = "https://github.com/FirstRaccoonInaTrenchCoat/gh-teams-terraform.git"
        id                          = "gh-teams-terraform"
        is_template                 = false
        merge_commit_message        = "PR_TITLE"
        merge_commit_title          = "MERGE_MESSAGE"
        name                        = "gh-teams-terraform"
        node_id                     = "R_kgDOKYvReA"
        private                     = false
        repo_id                     = 697028984
        squash_merge_commit_message = "COMMIT_MESSAGES"
        squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
        ssh_clone_url               = "git@github.com:FirstRaccoonInaTrenchCoat/gh-teams-terraform.git"
        svn_url                     = "https://github.com/FirstRaccoonInaTrenchCoat/gh-teams-terraform"
        visibility                  = "public"
        vulnerability_alerts        = false
    }

    # module.github-teams.github_team.team_admins:
    resource "github_team" "team_admins" {
        create_default_maintainer = false
        etag                      = "W/\"71f79b17a6e64a745cd1d36993772a3c85d7b9c47941d01bca058e1c939204ab\""
        id                        = "8647215"
        members_count             = 0
        name                      = "team-admins"
        node_id                   = "T_kwDOCLXSC84Ag_Iv"
        privacy                   = "secret"
        slug                      = "team-admins"
    }

    # module.github-teams.github_team.team_maintain:
    resource "github_team" "team_maintain" {
        create_default_maintainer = false
        etag                      = "W/\"31c6fcb86cdbfb02e69cff0a0b01e4570169d5a94598ccb8b5b8c93dfbcdf358\""
        id                        = "8647213"
        members_count             = 0
        name                      = "team-push"
        node_id                   = "T_kwDOCLXSC84Ag_It"
        privacy                   = "secret"
        slug                      = "team-push"
    }

    # module.github-teams.github_team.team_pull:
    resource "github_team" "team_pull" {
        create_default_maintainer = false
        etag                      = "W/\"2ff57f583b14aba6d86ea7f7801646c10174bea8ac728c5123540927daf9df20\""
        id                        = "8647214"
        members_count             = 0
        name                      = "team-pull"
        node_id                   = "T_kwDOCLXSC84Ag_Iu"
        privacy                   = "secret"
        slug                      = "team-pull"
    }

    # module.github-teams.github_team_repository.team_a_access:
    resource "github_team_repository" "team_a_access" {
        etag       = "W/\"b07bc9756acbc9f179c02d531b4b24c666d1ed55fed6183ba5f9bf53b0c19401\""
        id         = "8647214:gh-teams-terraform"
        permission = "pull"
        repository = "gh-teams-terraform"
        team_id    = "8647214"
    }

    # module.github-teams.github_team_repository.team_b_access:
    resource "github_team_repository" "team_b_access" {
        etag       = "W/\"a85cc262825a2ad0bdae7ec494d5415153bb11b23301cbf47355455ff9ee9373\""
        id         = "8647213:gh-teams-terraform"
        permission = "maintain"
        repository = "gh-teams-terraform"
        team_id    = "8647213"
    }

    # module.github-teams.github_team_repository.team_c_access:
    resource "github_team_repository" "team_c_access" {
        etag       = "W/\"382b721771c2aefc1421c947a0401cf66daa0778763140ad2328336ceb99963f\""
        id         = "8647215:gh-teams-terraform"
        permission = "admin"
        repository = "gh-teams-terraform"
        team_id    = "8647215"
    }
    # module.yandex-cloud.yandex_compute_instance.vm-1:
    resource "yandex_compute_instance" "vm-1" {
        created_at                = "2023-09-26T23:27:01Z"
        folder_id                 = "b1g1aqrohbot4fl3e1vb"
        fqdn                      = "fhmhr8utke1pq532ljid.auto.internal"
        id                        = "fhmhr8utke1pq532ljid"
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILhfsZIYeXjHbVnzBrSptYAKkhqLisjuA8daEBQgyBjx jacepac264@gmail.com
            EOT
        }
        name                      = "terraform1"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        status                    = "running"
        zone                      = "ru-central1-a"

        boot_disk {
            auto_delete = true
            device_name = "fhmj382ct5d2t58vc1p7"
            disk_id     = "fhmj382ct5d2t58vc1p7"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd82sqrj4uk9j7vlki3q"
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
            ip_address         = "192.168.10.14"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:11:da:3d:da"
            nat                = true
            nat_ip_address     = "51.250.2.20"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e9b8ti7c0faeeqdne0h9"
        }

        placement_policy {
            host_affinity_rules = []
        }

        resources {
            core_fraction = 100
            cores         = 2
            gpus          = 0
            memory        = 2
        }

        scheduling_policy {
            preemptible = false
        }
    }

    # module.yandex-cloud.yandex_compute_instance.vm-2:
    resource "yandex_compute_instance" "vm-2" {
        created_at                = "2023-09-26T23:27:01Z"
        folder_id                 = "b1g1aqrohbot4fl3e1vb"
        fqdn                      = "fhmviuovi1fus7abe342.auto.internal"
        id                        = "fhmviuovi1fus7abe342"
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILhfsZIYeXjHbVnzBrSptYAKkhqLisjuA8daEBQgyBjx jacepac264@gmail.com
            EOT
        }
        name                      = "terraform2"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        status                    = "running"
        zone                      = "ru-central1-a"

        boot_disk {
            auto_delete = true
            device_name = "fhm4t53js6roi8e2t21q"
            disk_id     = "fhm4t53js6roi8e2t21q"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd82sqrj4uk9j7vlki3q"
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
            ip_address         = "192.168.10.16"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:1f:97:b1:f9"
            nat                = true
            nat_ip_address     = "51.250.83.140"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e9b8ti7c0faeeqdne0h9"
        }

        placement_policy {
            host_affinity_rules = []
        }

        resources {
            core_fraction = 100
            cores         = 4
            gpus          = 0
            memory        = 4
        }

        scheduling_policy {
            preemptible = false
        }
    }

    # module.yandex-cloud.yandex_vpc_network.network-1:
    resource "yandex_vpc_network" "network-1" {
        created_at                = "2023-09-26T23:26:57Z"
        default_security_group_id = "enp7idu0lc81u43ltc7c"
        folder_id                 = "b1g1aqrohbot4fl3e1vb"
        id                        = "enpfjc3s1acs93k8kvcg"
        labels                    = {}
        name                      = "network1"
        subnet_ids                = []
    }

    # module.yandex-cloud.yandex_vpc_subnet.subnet-1:
    resource "yandex_vpc_subnet" "subnet-1" {
        created_at     = "2023-09-26T23:26:59Z"
        folder_id      = "b1g1aqrohbot4fl3e1vb"
        id             = "e9b8ti7c0faeeqdne0h9"
        labels         = {}
        name           = "subnet1"
        network_id     = "enpfjc3s1acs93k8kvcg"
        v4_cidr_blocks = [
            "192.168.10.0/24",
        ]
        v6_cidr_blocks = []
        zone           = "ru-central1-a"
    }


## outputs

    terraform outputs

Output:

    container_id = "a6973460a287574461b480097acfb151a34589c7fd5f3b5573e74ebc6dde109c"
    image_id = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1ekurohata7/devops_msk_time"
