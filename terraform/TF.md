# Terraform

## 0. Terraform Best Practices Used
- Split configuration into several files
- Organize files by workspaces in first-level directories and by projects in the second-level directories
- Use `variables.tf` for tokens' security
- Using `teraform fmt` to check if the files are correctly formated
- Using `terraform validate` to check the validity of the terraform code
- Don't push `.terraform` and `.tfstate` files to VCS
- The `.terraform` folder is created by terraform init which is executed by every user that wishes to use terraform configuration, so it's unique for each user.
- The `.tfstate` is a sensitive data and should not be shared publicly (or among the developers). It is much saver to use "remote" backend to store it on a server and to allow multiple developers to collaborate on the same state.
- Use `terraform.tfvars` file only in compositions
- Composition is the final infrastructure that is composed of many other terraform modules. It is what will be there and it is what should be configurated completely. Don't configurate using `terraform.tfvars` the modules themselves. Their variables are to be configured by the top-level user of the modules.

<br>

## 1. Docker steps and output

### 1.1 Installing Terraform and building infrastructure

<br>

From the directory where the `main.tf` is located, I used the command:

```
terraform apply
```

To view the built infrastructure, I used the commands below:

```
terraform show
```
Output: 

```sh
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach            = false
    command           = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    cpu_shares        = 0
    entrypoint        = [
        "/docker-entrypoint.sh",
    ]
    env               = []
    gateway           = "172.17.0.1"
    hostname          = "9fc236920c13"
    id                = "9fc236920c13bde042ce92a33e2bf2522c4285b3c778e270d8c20c70a2a6671a"
    image             = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init              = false
    ip_address        = "172.17.0.2"
    ip_prefix_length  = 16
    ipc_mode          = "private"
    log_driver        = "json-file"
    logs              = false
    max_retry_count   = 0
    memory            = 0
    memory_swap       = 0
    must_run          = true
    name              = "VariableNumberOne"
    network_data      = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            network_name              = "bridge"
        },
    ]
    network_mode      = "default"
    privileged        = false
    publish_all_ports = false
    read_only         = false
    remove_volumes    = true
    restart           = "no"
    rm                = false
    runtime           = "runc"
    security_opts     = []
    shm_size          = 64
    start             = true
    stdin_open        = false
    stop_signal       = "SIGQUIT"
    stop_timeout      = 0
    tty               = false

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    latest       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

```
 terraform state list
```
Output: 

```sh
docker_container.nginx
docker_image.nginx
```

### 1.2 Changing infrastructure (changed one variable)

<br>

Change log is displayed below:

```
terraform show
```
Output: 

```sh
docker_image.nginx: Refreshing state... [id=sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest]
docker_container.nginx: Refreshing state... [id=9fc236920c13bde042ce92a33e2bf2522c4285b3c778e270d8c20c70a2a6671a]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge            = (known after apply)
      ~ command           = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs    = (known after apply)
      - cpu_shares        = 0 -> null
      - dns               = [] -> null
      - dns_opts          = [] -> null
      - dns_search        = [] -> null
      ~ entrypoint        = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env               = [] -> (known after apply)
      + exit_code         = (known after apply)
      ~ gateway           = "172.17.0.1" -> (known after apply)
      - group_add         = [] -> null
      ~ hostname          = "9fc236920c13" -> (known after apply)
      ~ id                = "9fc236920c13bde042ce92a33e2bf2522c4285b3c778e270d8c20c70a2a6671a" -> (known after apply)
      ~ init              = false -> (known after apply)
      ~ ip_address        = "172.17.0.2" -> (known after apply)
      ~ ip_prefix_length  = 16 -> (known after apply)
      ~ ipc_mode          = "private" -> (known after apply)
      - links             = [] -> null
      ~ log_driver        = "json-file" -> (known after apply)
      - log_opts          = {} -> null
      - max_retry_count   = 0 -> null
      - memory            = 0 -> null
      - memory_swap       = 0 -> null
      ~ name              = "VariableNumberOne" -> "VariableNumberTwo" # forces replacement
      ~ network_data      = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode      = "default" -> null
      - privileged        = false -> null
      - publish_all_ports = false -> null
      ~ runtime           = "runc" -> (known after apply)
      ~ security_opts     = [] -> (known after apply)
      ~ shm_size          = 64 -> (known after apply)
      ~ stop_signal       = "SIGQUIT" -> (known after apply)
      ~ stop_timeout      = 0 -> (known after apply)
      - storage_opts      = {} -> null
      - sysctls           = {} -> null
      - tmpfs             = {} -> null
        # (11 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "9fc236920c13bde042ce92a33e2bf2522c4285b3c778e270d8c20c70a2a6671a" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=9fc236920c13bde042ce92a33e2bf2522c4285b3c778e270d8c20c70a2a6671a]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=dc9f9aeacabada45995be687e91c45043643abba54858ddfe11091373a347b91]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.        
```

### 1.3 Terraform output.

<br>

Command:
```
terraform output
```

output:
```sh
container_id = "dc9f9aeacabada45995be687e91c45043643abba54858ddfe11091373a347b91"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
```

<br>

## 2. Yandex Cloud

```
terraform show
```

```sh
# yandex_compute_instance.DevOps:
resource "yandex_compute_instance" "DevOps" {
    allow_stopping_for_update = true
    created_at                = "2023-09-27T01:30:38Z"
    folder_id                 = "b1gkp5mnhp65cbi1lti9"
    fqdn                      = "fhm7l8h5jfd0uc6ccueu.auto.internal"
    id                        = "fhm7l8h5jfd0uc6ccueu"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJns0Kh1zhy0vCcxD98WL63MEMhwRzKIFOHQEXoceW54Ey4sNIyL76gLFPkSIs/9gWFCulayFcOntOl3j4fzt8VtL8MJLy4kmp8QIXAUoT4HVV80JX5oGcqTHIGTKq5uZYp8A22Ui4LH5nE8DkS0FE47d8bFMuwg1Ple5fN2TxGXGQc49hHm8abJDkjk2YzxJRoAfD5CCcDkkPRdRCr8MfxkwD5Sehg5UCCBYrn6vT1AbIa3h3txrZMRNhnUYdbDoyWXnM4Qp/fLS/+dKwsivlEwrIBAkpN0BBq4DszfKbwPP/HbQaGYUfGlneex7Oo60BYIjqIvuMdDAMH1wJ2whBWWtAj5mzbKAK7LW9uE8CqjK9Mvm5IC1pJ54Ctq+ZogRTb2xBZYAAkUSzzw97Brkog8hA12VLFpAhakJZUm0QYPEGbdA/e5ronfBfnKukZmYphTR+PkLvvyYTH8shV8ImgTSI9lr6NL9rI8GdD2iOHsysYg/s7lquhWrLhBvfJNc= john@john
        EOT
    }
    name                      = "terraform-app"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhms2qtjp74i63jpemc0"
        disk_id     = "fhms2qtjp74i63jpemc0"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8clogg1kull9084s9o"
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
        mac_address        = "d0:0d:7a:a2:25:9b"
        nat                = true
        nat_ip_address     = "158.160.110.19"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bfqhar2lab13e0l11a"
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

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2023-09-27T01:30:31Z"
    default_security_group_id = "enp7h7b80ttp8deuvjce"
    folder_id                 = "b1gkp5mnhp65cbi1lti9"
    id                        = "enpsdfc80t2q3vkkfu8o"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-09-27T01:30:35Z"
    folder_id      = "b1gkp5mnhp65cbi1lti9"
    id             = "e9bfqhar2lab13e0l11a"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpsdfc80t2q3vkkfu8o"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

```
terraform output
```

```sh
external_ip_address_vm_1 = "158.160.110.19"
internal_ip_address_vm_1 = "192.168.10.14"
```

## 3. Github

### 3.1 Output of the `terraform apply -var "token=..."`

```sh
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "new-terraform-repository"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = false
      + allow_squash_merge          = false
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Terraform new repository"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + gitignore_template          = "VisualStudio"
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "new-terraform-repository"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Creating...
github_repository.repo: Creation complete after 6s [id=new-terraform-repository]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=new-terraform-repository]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOKYx9ds4CgYto]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

### 3.2 The output of `terraform import`

```sh
    github_repository.repo: Import prepared!
    Prepared github_repository for import
    github_repository.repo: Refreshing state... [id=new-terraform-repository]

    Import successful!

    The resources that were imported are shown above. These resources are now in
    your Terraform state and will henceforth be managed by Terraform.

```

### 3.3 Apply Terraform Changes (changed description of repo)
```sh
github_repository.repo: Refreshing state... [id=new-terraform-repository]
github_branch_default.main: Refreshing state... [id=new-terraform-repository]
github_branch_protection.default: Refreshing state... [id=BPR_kwDOKYx9ds4CgYto]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ description                 = "Terraform new repository" -> "New descriotion in Terraform new repository"
        id                          = "new-terraform-repository"
        name                        = "new-terraform-repository"
        # (32 unchanged attributes hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=new-terraform-repository]
github_repository.repo: Modifications complete after 2s [id=new-terraform-repository]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```
