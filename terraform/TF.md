# Terraform
I used yandex mirror for terraform providers to avoid using vpn. I put `terraform.rc` into `~/.terraformrc`. 

## Docker
Outputs of `terraform apply`
```
Outputs:

container_id = "a06d9cabc24a809cfd29e85d16c28e03365e92a094c34f83c5078c5fff21b725"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx"
```

After deploying using `terraform apply`
```
╰─➤  terraform state list
docker_container.nginx
docker_image.nginx

╰─➤  terraform state show docker_container.nginx
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "a06d9cabc24a"
    id                                          = "a06d9cabc24a809cfd29e85d16c28e03365e92a094c34f83c5078c5fff21b725"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devopse-course-nginx"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## Yandex cloud
Outputs of `terraform apply`
```
Outputs:

yandex-ip-address = "158.160.122.93"
```

After deploying using `terraform apply`
```
╰─➤  terraform state list                       
data.yandex_compute_image.my_image
yandex_compute_instance.terraform
yandex_vpc_address.addr
yandex_vpc_network.default
yandex_vpc_subnet.terraform

╰─➤  terraform state show yandex_compute_instance.terraform
# yandex_compute_instance.terraform:
resource "yandex_compute_instance" "terraform" {
    created_at                = "2023-09-27T05:06:12Z"
    folder_id                 = "b1gq1nfb08rgqmrqosie"
    fqdn                      = "fhmu13ojt0dcmkn2tu8n.auto.internal"
    id                        = "fhmu13ojt0dcmkn2tu8n"
    labels                    = {}
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQChf4aShIg4uY3NzfG7s+qMkDv04NmdDn4s9fC8i/HRgqWmFuS45fhfw2Vv/ZFPibC7raXCRu8po8tPfdjMF78sGYckEQCRBVLqDNooBKtJDlBaM5zzmIRoRGoSPJ2N0bC7o9cc52gjCcF3Ck1BLDtVkEcrMbaUoQNfoBLlJaw3z3d2JAfUO7s+7SbbNaI3umWNq7zMPl8+iNOPjdkYd2JKhUMCnzEBIKsqsMFECo0GsnzPcfS3R/iTVPFhRAcoFii6qqZRIzoW2YzVPOXAMVceusSGY9+1KBrxBL5n5SdtJlvEsa8ZuzcN5ZebM2n804Ttub1Mydin9a4OHPbTmcQB bizuki
        EOT
    }
    name                      = "devops-course-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm6hjns9p4vho54bje3"
        disk_id     = "fhm6hjns9p4vho54bje3"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8388svft7v8189tc5l"
            size       = 3
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
        ip_address         = "10.0.0.25"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1e:08:f1:3e"
        nat                = true
        nat_ip_address     = "158.160.122.93"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bon8s9omuqva1ah3e9"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }
}
```

## Github
Outputs of `terraform apply`
```
Outputs:

github_repo = "https://github.com/bizuki/devops-terraform-demo"
```

After deploying using `terraform apply`
```
╰─➤  terraform state list                                                                                                                                                                                   1 ↵
github_branch_default.default_branch
github_branch_protection.default
github_repository.repo

╰─➤  terraform state show github_repository.repo
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
    description                 = "Test repo to show terraform infra"
    etag                        = "W/\"52e91c8f14efa0058880e0e2e71419d3afd9f7a0d13ba7f156907c8465d382f2\""
    full_name                   = "bizuki/devops-terraform-demo"
    git_clone_url               = "git://github.com/bizuki/devops-terraform-demo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/bizuki/devops-terraform-demo"
    http_clone_url              = "https://github.com/bizuki/devops-terraform-demo.git"
    id                          = "devops-terraform-demo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-terraform-demo"
    node_id                     = "R_kgDOKY1PbA"
    private                     = false
    repo_id                     = 697126764
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:bizuki/devops-terraform-demo.git"
    svn_url                     = "https://github.com/bizuki/devops-terraform-demo"
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

## Best practices
1. Check code style and syntax using `terraform validate` and `terraform fmt` to make code look better.
2. Make tokens and other secrets as sensitive variables and do not specify them directly. You can use env vars for example (`TF_VAR_{varname}`)
3. Split your configurations by logic type. For example all resources go into `resources.tf`, variables into `variables.tf` and etc.