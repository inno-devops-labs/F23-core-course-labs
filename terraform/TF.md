## Docker

```sh
❯  terraform apply

docker_image.app_elixir: Refreshing state... [id=sha256:1912a20c8a03ebe45bb9de2f53b09dd754bd19cf131138868f38a30d515abdc9nikitosing/app_elixir:latest]
docker_container.nginx: Refreshing state... [id=60ac4c80e2877e890512b57f7eaa6cc4581966cc6ffcac09f1bf228ae34df5b3]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_elixir will be created
  + resource "docker_container" "app_elixir" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = [
          + "SECRET_KEY_BASE='WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O'",
        ]
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = "sha256:1912a20c8a03ebe45bb9de2f53b09dd754bd19cf131138868f38a30d515abdc9"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "elixir_time"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + ports {
          + external = 80
          + internal = 4000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_elixir: Creating...
docker_container.app_elixir: Creation complete after 1s [id=0be842272b26a3a2c3879f0a3a729078f9ff43e89be4f53ac0e91d2f8610eda9]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

```sh
❯ terraform state list
docker_container.app_elixir
docker_image.app_elixir
```

```sh
❯ terraform state show docker_container.app_elixir
# docker_container.app_elixir:
resource "docker_container" "app_elixir" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "bin/devops_web",
        "start",
    ]
    env                                         = [
        "SECRET_KEY_BASE='WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O'",
    ]
    hostname                                    = "0be842272b26"
    id                                          = "0be842272b26a3a2c3879f0a3a729078f9ff43e89be4f53ac0e91d2f8610eda9"
    image                                       = "sha256:1912a20c8a03ebe45bb9de2f53b09dd754bd19cf131138868f38a30d515abdc9"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "elixir_time"
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
    user                                        = "defaultuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 80
        internal = 4000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```sh
❯ terraform apply
docker_image.app_elixir: Refreshing state... [id=sha256:1912a20c8a03ebe45bb9de2f53b09dd754bd19cf131138868f38a30d515abdc9nikitosing/app_elixir:latest]
docker_container.app_elixir: Refreshing state... [id=0be842272b26a3a2c3879f0a3a729078f9ff43e89be4f53ac0e91d2f8610eda9]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_elixir must be replaced
-/+ resource "docker_container" "app_elixir" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "bin/devops_web",
          - "start",
        ] -> (known after apply)
      ~ env                                         = [ # forces replacement
          - "SECRET_KEY_BASE='WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O'",
          + "SECRET_KEY_BASE=WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O",
        ]
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "0be842272b26" -> (known after apply)
      ~ id                                          = "0be842272b26a3a2c3879f0a3a729078f9ff43e89be4f53ac0e91d2f8610eda9" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "elixir_time"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "defaultuser" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_elixir: Destroying... [id=0be842272b26a3a2c3879f0a3a729078f9ff43e89be4f53ac0e91d2f8610eda9]
docker_container.app_elixir: Destruction complete after 0s
docker_container.app_elixir: Creating...
docker_container.app_elixir: Creation complete after 0s [id=0e14e81990fe50caf59a055232713fa9e331c5823e1d18ac1fea355d0dc143f8]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

```sh
❯ terraform output
container_id = "0e14e81990fe50caf59a055232713fa9e331c5823e1d18ac1fea355d0dc143f8"
image_id = "sha256:1912a20c8a03ebe45bb9de2f53b09dd754bd19cf131138868f38a30d515abdc9nikitosing/app_elixir:latest"
```

## VK Cloud

```sh
❯ terraform init



Initializing the backend...

Initializing provider plugins...
- Finding vk-cs/vkcs versions matching "~> 0.1.12"...
- Installing vk-cs/vkcs v0.1.16...
- Installed vk-cs/vkcs v0.1.16 (unauthenticated)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Incomplete lock file information for providers
│
│ Due to your customized provider installation methods, Terraform was forced to calculate lock file checksums locally for the following providers:
│   - vk-cs/vkcs
│
│ The current .terraform.lock.hcl file only includes checksums for darwin_arm64, so Terraform running on another platform will fail to install these providers.
│
│ To calculate additional checksums for another platform, run:
│   terraform providers lock -platform=linux_amd64
│ (where linux_amd64 is the platform to generate)
╵

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```sh
❯ terraform apply


var.password
  Enter a value: ******

data.vkcs_compute_flavor.compute: Reading...
data.vkcs_networking_network.extnet: Reading...
data.vkcs_images_image.compute: Reading...
vkcs_networking_network.network: Refreshing state... [id=33931153-ef1b-4af6-8cc3-65cd82b331bb]
vkcs_networking_secgroup.secgroup: Refreshing state... [id=4ae2b4e0-e1a3-4acd-b297-3297d41bc665]
vkcs_networking_secgroup_rule.secgroup_rule_1: Refreshing state... [id=5313af3c-fdfb-4a86-b4a2-1dfc6ec6abce]
vkcs_networking_secgroup_rule.secgroup_rule_2: Refreshing state... [id=ac125f43-de8c-46bf-a9e7-2942bb25785a]
data.vkcs_images_image.compute: Read complete after 0s [id=b75595ca-4e1d-47e0-8e95-7a02edc0e242]
vkcs_networking_subnet.subnetwork: Refreshing state... [id=5403ec7a-740e-4c9f-97a9-907f1a57f0b1]
data.vkcs_compute_flavor.compute: Read complete after 0s [id=25ae869c-be29-4840-8e12-99e046d2dbd4]
vkcs_networking_port.port: Refreshing state... [id=8c10a39d-a009-4ca3-9a58-2a3e72328c7e]
data.vkcs_networking_network.extnet: Read complete after 0s [id=298117ae-3fa4-4109-9e08-8be5602be5a2]
vkcs_networking_floatingip.fip: Refreshing state... [id=68c0ec87-f33e-4cc7-a62b-cf5356fa2461]
vkcs_networking_router.router: Refreshing state... [id=890efe44-0158-4226-9201-5552e369e0a1]
vkcs_networking_port_secgroup_associate.port: Refreshing state... [id=8c10a39d-a009-4ca3-9a58-2a3e72328c7e]
vkcs_networking_router_interface.db: Refreshing state... [id=5e8e06bd-9e84-4f6b-be4e-5b1e14f3dff9]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # vkcs_compute_floatingip_associate.fip will be created
  + resource "vkcs_compute_floatingip_associate" "fip" {
      + floating_ip = "212.233.95.132"
      + id          = (known after apply)
      + instance_id = (known after apply)
      + region      = (known after apply)
    }

  # vkcs_compute_instance.compute will be created
  + resource "vkcs_compute_instance" "compute" {
      + access_ip_v4        = (known after apply)
      + all_metadata        = (known after apply)
      + all_tags            = (known after apply)
      + availability_zone   = "MS1"
      + flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
      + flavor_name         = (known after apply)
      + force_delete        = false
      + id                  = (known after apply)
      + image_id            = (known after apply)
      + image_name          = (known after apply)
      + key_pair            = "test"
      + name                = "compute-instance"
      + power_state         = "active"
      + region              = (known after apply)
      + security_groups     = [
          + "default",
          + "security_group",
        ]
      + stop_before_destroy = false

      + block_device {
          + boot_index            = 0
          + delete_on_termination = true
          + destination_type      = "volume"
          + source_type           = "image"
          + uuid                  = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
          + volume_size           = 8
          + volume_type           = "ceph-ssd"
        }

      + network {
          + access_network = false
          + fixed_ip_v4    = (known after apply)
          + mac            = (known after apply)
          + name           = (known after apply)
          + port           = (known after apply)
          + uuid           = "33931153-ef1b-4af6-8cc3-65cd82b331bb"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.
╷
│ Warning: Argument is deprecated
│
│   with vkcs_networking_secgroup_rule.secgroup_rule_1,
│   on network.tf line 34, in resource "vkcs_networking_secgroup_rule" "secgroup_rule_1":
│   34:    ethertype = "IPv4"
│
│ Only IPv4 can be used as ethertype. This argument is deprecated, please do not use it.
│
│ (and 3 more similar warnings elsewhere)
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

vkcs_compute_instance.compute: Creating...
vkcs_compute_instance.compute: Still creating... [10s elapsed]
vkcs_compute_instance.compute: Still creating... [20s elapsed]
vkcs_compute_instance.compute: Still creating... [30s elapsed]
vkcs_compute_instance.compute: Creation complete after 37s [id=472e9f1f-54d4-4ee4-a045-c030e8917e5c]
vkcs_compute_floatingip_associate.fip: Creating...
vkcs_compute_floatingip_associate.fip: Creation complete after 4s [id=212.233.95.132/472e9f1f-54d4-4ee4-a045-c030e8917e5c/]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

instance_fip = "212.233.95.132"
```

```sh
❯ terraform state list
data.vkcs_compute_flavor.compute
data.vkcs_images_image.compute
data.vkcs_networking_network.extnet
vkcs_compute_floatingip_associate.fip
vkcs_compute_instance.compute
vkcs_networking_floatingip.fip
vkcs_networking_network.network
vkcs_networking_port.port
vkcs_networking_port_secgroup_associate.port
vkcs_networking_router.router
vkcs_networking_router_interface.db
vkcs_networking_secgroup.secgroup
vkcs_networking_secgroup_rule.secgroup_rule_1
vkcs_networking_secgroup_rule.secgroup_rule_2
vkcs_networking_subnet.subnetwork
```

```sh
❯ terraform state show data.vkcs_compute_flavor.compute
# data.vkcs_compute_flavor.compute:
data "vkcs_compute_flavor" "compute" {
    disk         = 20
    extra_specs  = {
        "agg_common"     = "true"
        "hw:cpu_sockets" = "1"
        "mcs:cpu_type"   = "standard"
    }
    flavor_id    = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    is_public    = true
    name         = "Basic-1-2-20"
    ram          = 2048
    rx_tx_factor = 1
    swap         = 0
    vcpus        = 1
}
```

```sh
❯ terraform output
instance_fip = "212.233.95.132"
```

## GitHub

```sh
❯ terraform import "github_repository.repo" "core-course-labs"
var.GITHUB_TOKEN
  Github auth token

  Enter a value:

github_repository.repo: Importing from ID "core-course-labs"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

```

```sh
❯ terraform apply
var.GITHUB_TOKEN
  Github auth token

  Enter a value:

github_repository.repo: Refreshing state... [id=core-course-labs]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "core-course-labs"
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
      + repository_id                   = "core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "DevOps [F23]"
      - has_downloads               = true -> null
      ~ has_issues                  = false -> true
      - has_projects                = true -> null
        id                          = "core-course-labs"
        name                        = "core-course-labs"
        # (30 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

  # github_team.admins will be created
  + resource "github_team" "admins" {
      + create_default_maintainer = true
      + description               = "Admins Team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "admins"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.devs will be created
  + resource "github_team" "devs" {
      + create_default_maintainer = true
      + description               = "Developers Team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "devs"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team_repository.admins_repo will be created
  + resource "github_team_repository" "admins_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "core-course-labs"
      + team_id    = (known after apply)
    }

  # github_team_repository.devs_repo will be created
  + resource "github_team_repository" "devs_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "core-course-labs"
      + team_id    = (known after apply)
    }

Plan: 6 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.devs: Creating...
github_team.admins: Creating...
github_repository.repo: Modifying... [id=core-course-labs]
github_repository.repo: Modifications complete after 2s [id=core-course-labs]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOKPqOHs4CgWVb]
```

## Best practices

- Env variables for everything
- Format files
- Use git
- Env variable for all the secrets
- Use proper `.tf` files hierarchy
