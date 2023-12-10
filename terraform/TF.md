# Terraform Best Practices

- Prioritize Terraform Plan - before making any changes, it's essential to run terraform plan. This step ensures you comprehend Terraform's intended actions and mitigates unintended consequences.
- Consistent Naming Conventions - maintain a uniform naming convention throughout your code to enhance clarity and maintainability.
- Utilize variables.tf - to facilitate easy code modification, promoting flexibility and scalability.
- Secure Sensitive Data Handling - handle sensitive information, such as passwords or API keys, securely by storing them in variables.tf rather than hardcoding them in your Terraform code.
- Utilize Output.tf - to expose specific values or information from your infrastructure code after it has been applied, aiding in monitoring and external access.

# Docker
List states
```
terraform state list
```
Output:
```
docker_container.app
docker_image.app
```

Terraform show
```bash
terraform show
```
<details>
  <summary>COMMAND OUTPUT</summary>
  
  ```bash
  [arodef@fedora terraform]$ terraform show
  # docker_container.app:
  resource "docker_container" "app" {
      attach                                      = false
      command                                     = []
      container_read_refresh_timeout_milliseconds = 15000
      cpu_shares                                  = 0
      entrypoint                                  = [
          "python3",
          "-m",
          "uvicorn",
          "main:app",
          "--port",
          "8000",
          "--host",
          "0.0.0.0",
      ]
      env                                         = []
      hostname                                    = "67218ff3ed56"
      id                                          = "67218ff3ed56c9410eec380390c0ae5869fd4862cddd6ddf9834539c1d2f344f"
      image                                       = "sha256:bcc1c0d9c1b72f5c412f8c56a7f304c1fb488a4df77a8c16df8f46d129c7871d"
      init                                        = false
      ipc_mode                                    = "private"
      log_driver                                  = "json-file"
      logs                                        = false
      max_retry_count                             = 0
      memory                                      = 0
      memory_swap                                 = 0
      must_run                                    = true
      name                                        = "python_webserv"
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
      user                                        = "myuser"
      wait                                        = false
      wait_timeout                                = 60
      working_dir                                 = "/code"

      ports {
          external = 8000
          internal = 8000
          ip       = "0.0.0.0"
          protocol = "tcp"
      }
  }

  # docker_image.app:
  resource "docker_image" "app" {
      id           = "sha256:bcc1c0d9c1b72f5c412f8c56a7f304c1fb488a4df77a8c16df8f46d129c7871dseakysneka1/webserv_python:latest"
      image_id     = "sha256:bcc1c0d9c1b72f5c412f8c56a7f304c1fb488a4df77a8c16df8f46d129c7871d"
      keep_locally = false
      name         = "seakysneka1/webserv_python:latest"
      repo_digest  = "seakysneka1/webserv_python@sha256:1aa9e7f729b79e53176997aa52cd055fcf645f269a024ecb2c6f6bf53543c954"
  }


  Outputs:

  container_id = "67218ff3ed56c9410eec380390c0ae5869fd4862cddd6ddf9834539c1d2f344f"
  image_id = "sha256:bcc1c0d9c1b72f5c412f8c56a7f304c1fb488a4df77a8c16df8f46d129c7871dseakysneka1/webserv_python:latest"
  ```
</details>


Terraform outputs

``` bash
terraform output
```
Output:
```
container_id = "67218ff3ed56c9410eec380390c0ae5869fd4862cddd6ddf9834539c1d2f344f"
image_id = "sha256:bcc1c0d9c1b72f5c412f8c56a7f304c1fb488a4df77a8c16df8f46d129c7871dseakysneka1/webserv_python:latest"
```

# Yandex cloud
I used yandex cloud infrastructure with terraform:
I followed this [Yandex cloud guide](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-state-storage#configure-terraform)


```bash
terraform init -backend-config="access_key=$ACCESS_KEY" -backend-config="secret_key=$SECRET_KEY"
```

```bash
terraform plan
```

<details>
  <summary>COMMAND OUTPUT</summary>  

  ```bash
  [arodef@fedora yandex]$ terraform plan
  yandex_vpc_network.network_1: Refreshing state... [id=enpeuh5j59pitqm07lce]
  yandex_compute_image.ubuntu_2004: Refreshing state... [id=fd8rgb0p4q707v53p9he]
  yandex_vpc_subnet.subnet_1: Refreshing state... [id=e9b7m26mr49fhc438dg0]
  yandex_compute_instance.vm_1: Refreshing state... [id=fhmuorsqp1k6j37r06u3]

  Note: Objects have changed outside of Terraform

  Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

    # yandex_compute_instance.vm_1 has been deleted
    - resource "yandex_compute_instance" "vm_1" {
          id                        = "fhmuorsqp1k6j37r06u3"
          name                      = "terraform-vm-1"
          # (7 unchanged attributes hidden)

        - network_interface {
            - ip_address         = "10.130.0.7" -> null
              # (9 unchanged attributes hidden)
          }

          # (5 unchanged blocks hidden)
      }


  Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following
  plan may include actions to undo or respond to these changes.

  ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
  symbols:
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
        + name                      = "terraform-vm-1"
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
                + image_id    = "fd8rgb0p4q707v53p9he"
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
            + subnet_id          = "e9b7m26mr49fhc438dg0"
          }

        + resources {
            + core_fraction = 100
            + cores         = 2
            + memory        = 2
          }
      }

  Plan: 1 to add, 0 to change, 0 to destroy.

  Changes to Outputs:
    ~ internal_ip_address_vm_1 = "10.130.0.7" -> (known after apply)

  ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

  Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run
  "terraform apply" now.

  ```

</details>



```bash
terraform apply
```
<details>
  <summary>COMMAND OUTPUT</summary>  

  ```bash
  [arodef@fedora yandex]$ terraform apply
  yandex_vpc_network.network_1: Refreshing state... [id=enpeuh5j59pitqm07lce]
  yandex_compute_image.ubuntu_2004: Refreshing state... [id=fd8rgb0p4q707v53p9he]
  yandex_vpc_subnet.subnet_1: Refreshing state... [id=e9b7m26mr49fhc438dg0]
  yandex_compute_instance.vm_1: Refreshing state... [id=fhmuorsqp1k6j37r06u3]

  Note: Objects have changed outside of Terraform

  Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

    # yandex_compute_instance.vm_1 has been deleted
    - resource "yandex_compute_instance" "vm_1" {
          id                        = "fhmuorsqp1k6j37r06u3"
          name                      = "terraform-vm-1"
          # (7 unchanged attributes hidden)

        - network_interface {
            - ip_address         = "10.130.0.7" -> null
              # (9 unchanged attributes hidden)
          }

          # (5 unchanged blocks hidden)
      }


  Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following
  plan may include actions to undo or respond to these changes.

  ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
  symbols:
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
        + name                      = "terraform-vm-1"
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
                + image_id    = "fd8rgb0p4q707v53p9he"
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
            + subnet_id          = "e9b7m26mr49fhc438dg0"
          }

        + resources {
            + core_fraction = 100
            + cores         = 2
            + memory        = 2
          }
      }

  Plan: 1 to add, 0 to change, 0 to destroy.

  Changes to Outputs:
    ~ internal_ip_address_vm_1 = "10.130.0.7" -> (known after apply)

  Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

  yandex_compute_instance.vm_1: Creating...
  yandex_compute_instance.vm_1: Still creating... [10s elapsed]
  yandex_compute_instance.vm_1: Still creating... [20s elapsed]
  yandex_compute_instance.vm_1: Still creating... [30s elapsed]
  yandex_compute_instance.vm_1: Still creating... [40s elapsed]
  yandex_compute_instance.vm_1: Still creating... [50s elapsed]
  yandex_compute_instance.vm_1: Still creating... [1m0s elapsed]
  yandex_compute_instance.vm_1: Still creating... [1m10s elapsed]
  yandex_compute_instance.vm_1: Still creating... [1m20s elapsed]
  yandex_compute_instance.vm_1: Creation complete after 1m29s [id=fhmj9jqpgpebgpjta4u4]

  Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

  Outputs:

  internal_ip_address_vm_1 = "10.130.0.31"

  ```

</details>

```bash
  terraform state list
```

<details>
  <summary>COMMAND OUTPUT</summary>  
  
  ```bash
  [arodef@fedora yandex]$ terraform state list
  yandex_compute_image.ubuntu_2004
  yandex_compute_instance.vm_1
  yandex_vpc_network.network_1
  yandex_vpc_subnet.subnet_1

  ```
</details>

```bash
terraform show
```

<details>
  <summary>COMMAND OUTPUT</summary>  
  
  ```bash
  [arodef@fedora yandex]$ terraform show
  # yandex_compute_image.ubuntu_2004:
  resource "yandex_compute_image" "ubuntu_2004" {
      created_at    = "2023-09-26T12:56:52Z"
      folder_id     = "b1g7r0hqh6a654to932a"
      id            = "fd8rgb0p4q707v53p9he"
      labels        = {}
      min_disk_size = 5
      pooled        = false
      product_ids   = [
          "f2ed6k5slaamr94lfdqu",
      ]
      size          = 4
      source_family = "ubuntu-2004-lts"
      status        = "ready"
  }

  # yandex_compute_instance.vm_1:
  resource "yandex_compute_instance" "vm_1" {
      created_at                = "2023-09-26T15:17:34Z"
      folder_id                 = "b1g7r0hqh6a654to932a"
      fqdn                      = "fhmj9jqpgpebgpjta4u4.auto.internal"
      id                        = "fhmj9jqpgpebgpjta4u4"
      name                      = "terraform-vm-1"
      network_acceleration_type = "standard"
      platform_id               = "standard-v1"
      status                    = "running"
      zone                      = "ru-central1-a"

      boot_disk {
          auto_delete = true
          device_name = "fhmdfda6kra768a3gmia"
          disk_id     = "fhmdfda6kra768a3gmia"
          mode        = "READ_WRITE"

          initialize_params {
              block_size = 4096
              image_id   = "fd8rgb0p4q707v53p9he"
              size       = 5
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
          ip_address         = "10.130.0.31"
          ipv4               = true
          ipv6               = false
          mac_address        = "d0:0d:13:4c:f5:98"
          nat                = true
          nat_ip_address     = "51.250.64.80"
          nat_ip_version     = "IPV4"
          security_group_ids = []
          subnet_id          = "e9b7m26mr49fhc438dg0"
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

  # yandex_vpc_network.network_1:
  resource "yandex_vpc_network" "network_1" {
      created_at                = "2023-09-26T12:56:51Z"
      default_security_group_id = "enp75135jse6rgejm2ip"
      folder_id                 = "b1g7r0hqh6a654to932a"
      id                        = "enpeuh5j59pitqm07lce"
      labels                    = {}
      name                      = "chiplinka-vpc-network-default"
      subnet_ids                = [
          "e9b7m26mr49fhc438dg0",
      ]
  }

  # yandex_vpc_subnet.subnet_1:
  resource "yandex_vpc_subnet" "subnet_1" {
      created_at     = "2023-09-26T12:56:55Z"
      folder_id      = "b1g7r0hqh6a654to932a"
      id             = "e9b7m26mr49fhc438dg0"
      labels         = {}
      name           = "chiplinka-subnet-default-ru-central1-a"
      network_id     = "enpeuh5j59pitqm07lce"
      v4_cidr_blocks = [
          "10.130.0.0/24",
      ]
      v6_cidr_blocks = []
      zone           = "ru-central1-a"
  }


  Outputs:

  internal_ip_address_vm_1 = "10.130.0.31"

  ```
</details>



# Github
```bash
terraform plan -var="token=123" 
```

<details>
  <summary>COMMAND OUTPUT</summary>  
  
  ```bash
  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

  Terraform will perform the following actions:

    # github_branch_default.main will be created
    + resource "github_branch_default" "main" {
        + branch     = "main"
        + id         = (known after apply)
        + rename     = false
        + repository = "devops-assignment-chiplinka"
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
        + name                        = "devops-assignment-chiplinka"
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

    # github_team.team_silly will be created
    + resource "github_team" "team_silly" {
        + create_default_maintainer = false
        + description               = "Team 2"
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "team_silly_2"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "secret"
        + slug                      = (known after apply)
      }

    # github_team.team_smart will be created
    + resource "github_team" "team_smart" {
        + create_default_maintainer = false
        + description               = "Team 1"
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "team_smart_1"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "secret"
        + slug                      = (known after apply)
      }

    # github_team_repository.team_silly_repo will be created
    + resource "github_team_repository" "team_silly_repo" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "admin"
        + repository = "devops-assignment-chiplinka"
        + team_id    = (known after apply)
      }

    # github_team_repository.team_smart_repo will be created
    + resource "github_team_repository" "team_smart_repo" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "push"
        + repository = "devops-assignment-chiplinka"
        + team_id    = (known after apply)
      }

  Plan: 7 to add, 0 to change, 0 to destroy.

  ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

  Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
  ```

</details>

```bash
terraform apply -var="token=123"
```

<details>
  <summary>COMMAND OUTPUT</summary>  
  
  ```bash
  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

  Terraform will perform the following actions:

    # github_branch_default.main will be created
    + resource "github_branch_default" "main" {
        + branch     = "main"
        + id         = (known after apply)
        + rename     = false
        + repository = "devops-assignment-chiplinka"
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
        + name                        = "devops-assignment-chiplinka"
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

    # github_team.team_silly will be created
    + resource "github_team" "team_silly" {
        + create_default_maintainer = false
        + description               = "Team 2"
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "team_silly_2"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "secret"
        + slug                      = (known after apply)
      }

    # github_team.team_smart will be created
    + resource "github_team" "team_smart" {
        + create_default_maintainer = false
        + description               = "Team 1"
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "team_smart_1"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "secret"
        + slug                      = (known after apply)
      }

    # github_team_repository.team_silly_repo will be created
    + resource "github_team_repository" "team_silly_repo" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "admin"
        + repository = "devops-assignment-chiplinka"
        + team_id    = (known after apply)
      }

    # github_team_repository.team_smart_repo will be created
    + resource "github_team_repository" "team_smart_repo" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "push"
        + repository = "devops-assignment-chiplinka"
        + team_id    = (known after apply)
      }

  Plan: 7 to add, 0 to change, 0 to destroy.

  Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

  github_team.team_silly: Creating...
  github_team.team_smart: Creating...
  github_repository.repo: Creating...
  github_team.team_smart: Still creating... [10s elapsed]
  github_team.team_silly: Still creating... [10s elapsed]
  github_repository.repo: Still creating... [10s elapsed]
  github_team.team_silly: Creation complete after 12s [id=8644619]
  github_team.team_smart: Creation complete after 16s [id=8644620]
  github_repository.repo: Creation complete after 16s [id=devops-assignment-chiplinka]
  github_team_repository.team_silly_repo: Creating...
  github_team_repository.team_smart_repo: Creating...
  github_branch_default.main: Creating...
  github_team_repository.team_smart_repo: Creation complete after 4s [id=8644620:devops-assignment-chiplinka]
  github_branch_default.main: Creation complete after 6s [id=devops-assignment-chiplinka]
  github_branch_protection.default: Creating...
  github_team_repository.team_silly_repo: Creation complete after 6s [id=8644619:devops-assignment-chiplinka]
  github_branch_protection.default: Creation complete after 5s [id=BPR_kwDOKYj25c4CgSn8]

  Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
  ```
</details>

```bash
terraform show
```

<details>
  <summary>COMMAND OUTPUT</summary>  
  
  ```bash
  [arodef@fedora github]$ terraform show
  # github_branch_default.main:
  resource "github_branch_default" "main" {
      branch     = "main"
      id         = "devops-assignment-chiplinka"
      rename     = false
      repository = "devops-assignment-chiplinka"
  }

  # github_branch_protection.default:
  resource "github_branch_protection" "default" {
      allows_deletions                = false
      allows_force_pushes             = false
      blocks_creations                = false
      enforce_admins                  = true
      id                              = "BPR_kwDOKYj25c4CgSn8"
      lock_branch                     = false
      pattern                         = "main"
      repository_id                   = "devops-assignment-chiplinka"
      require_conversation_resolution = true
      require_signed_commits          = false
      required_linear_history         = false

      required_pull_request_reviews {
          dismiss_stale_reviews           = false
          require_code_owner_reviews      = false
          require_last_push_approval      = false
          required_approving_review_count = 1
          restrict_dismissals             = false
      }
  }

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
      etag                        = "W/\"6a3216b7e16964e1008a84b095d7439082781f840980a07c45a21b273699bfa1\""
      full_name                   = "DevopsAssignment-chiplinka/devops-assignment-chiplinka"
      git_clone_url               = "git://github.com/DevopsAssignment-chiplinka/devops-assignment-chiplinka.git"
      has_discussions             = false
      has_downloads               = false
      has_issues                  = true
      has_projects                = false
      has_wiki                    = true
      html_url                    = "https://github.com/DevopsAssignment-chiplinka/devops-assignment-chiplinka"
      http_clone_url              = "https://github.com/DevopsAssignment-chiplinka/devops-assignment-chiplinka.git"
      id                          = "devops-assignment-chiplinka"
      is_template                 = false
      merge_commit_message        = "PR_TITLE"
      merge_commit_title          = "MERGE_MESSAGE"
      name                        = "devops-assignment-chiplinka"
      node_id                     = "R_kgDOKYj25Q"
      private                     = false
      repo_id                     = 696841957
      squash_merge_commit_message = "COMMIT_MESSAGES"
      squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      ssh_clone_url               = "git@github.com:DevopsAssignment-chiplinka/devops-assignment-chiplinka.git"
      svn_url                     = "https://github.com/DevopsAssignment-chiplinka/devops-assignment-chiplinka"
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

  # github_team.team_silly:
  resource "github_team" "team_silly" {
      create_default_maintainer = false
      description               = "Team 2"
      etag                      = "W/\"ab1e53cb02129981c1d497f11dbb166570ddfc752127b6d5f9edacf11fdcd08f\""
      id                        = "8644619"
      members_count             = 0
      name                      = "team_silly_2"
      node_id                   = "T_kwDOCLVdss4Ag-gL"
      privacy                   = "secret"
      slug                      = "team_silly_2"
  }

  # github_team.team_smart:
  resource "github_team" "team_smart" {
      create_default_maintainer = false
      description               = "Team 1"
      etag                      = "W/\"454aa73876b82bbe30ef1340930e66af70129cd47282cd55ffd5385e04d47a4c\""
      id                        = "8644620"
      members_count             = 0
      name                      = "team_smart_1"
      node_id                   = "T_kwDOCLVdss4Ag-gM"
      privacy                   = "secret"
      slug                      = "team_smart_1"
  }

  # github_team_repository.team_silly_repo:
  resource "github_team_repository" "team_silly_repo" {
      etag       = "W/\"54d58677f65d752a6288ec95fbfe64c20883e83ebe366a07bf2979729f5f6633\""
      id         = "8644619:devops-assignment-chiplinka"
      permission = "admin"
      repository = "devops-assignment-chiplinka"
      team_id    = "8644619"
  }

  # github_team_repository.team_smart_repo:
  resource "github_team_repository" "team_smart_repo" {
      etag       = "W/\"6ea2816688cb06a06ff485b6090cce659c0327060000f197a95f42e3f6c7fd64\""
      id         = "8644620:devops-assignment-chiplinka"
      permission = "push"
      repository = "devops-assignment-chiplinka"
      team_id    = "8644620"
  }
  ```
</details>

```bash
terraform state list
```

<details>
  <summary>COMMAND OUTPUT</summary>  
  
  ```bash
  [arodef@fedora github]$ terraform state list
  github_branch_default.main
  github_branch_protection.default
  github_repository.repo
  github_team.team_silly
  github_team.team_smart
  github_team_repository.team_silly_repo
  github_team_repository.team_smart_repo
  ```
</details>
