# Terraform 

## Best practices

- Decompose configuration file into `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`
- Use `terraform validate`
- Use `terraform fmt` 
- Using of .tfvars to keep secrets

## Outputs

__Outputs of command `terraform state list`:__

- docker:

```
docker_container.app_python
docker_image.app_python
```

- yandex.cloud:

```
yandex_compute_instance.my_vm
yandex_vpc_network.my_network
yandex_vpc_subnet.my_subnetwork
```

- github:

```
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

__Outputs of command `terraform show`:__

- docker:

```
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "c420f03c1581"
    id                                          = "c420f03c15819fa011d0300c02c47e48efae26377c7429a2e502ebad6bf06ee3"
    image                                       = "sha256:990bd7a3cf69714ed95832b30f32992d3c647e94f9643c78dc93b0feab1d02ae"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app-python"
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
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:990bd7a3cf69714ed95832b30f32992d3c647e94f9643c78dc93b0feab1d02aerakavaqaflow/app-python:v1"
    image_id     = "sha256:990bd7a3cf69714ed95832b30f32992d3c647e94f9643c78dc93b0feab1d02ae"
    keep_locally = false
    name         = "rakavaqaflow/app-python:v1"
    repo_digest  = "rakavaqaflow/app-python@sha256:cd298b6bcbcc531cb4f9d482074cf725eff7c34b4bacac8a25d2ee8e14d0b65e"
}


Outputs:

container_id = "c420f03c15819fa011d0300c02c47e48efae26377c7429a2e502ebad6bf06ee3"
image_id = "sha256:990bd7a3cf69714ed95832b30f32992d3c647e94f9643c78dc93b0feab1d02aerakavaqaflow/app-python:v1"

```


- yandex.cloud:

```
# yandex_compute_instance.my_vm:
resource "yandex_compute_instance" "my_vm" {
    created_at                = "2023-09-26T22:02:42Z"
    folder_id                 = "b1gcsukd39lji9up1ohe"
    fqdn                      = "epdi2ggisto571h7jm1o.auto.internal"
    id                        = "epdi2ggisto571h7jm1o"
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdf45mf4qtse1re776m"
        disk_id     = "epdf45mf4qtse1re776m"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8dfofgv8k45mqv25nq"
            name       = "ubuntu-20-04-lts-v20230918"
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
        ip_address         = "10.129.0.26"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:12:14:21:2e"
        nat                = false
        security_group_ids = []
        subnet_id          = "e2la6hksalj13g2vu6ma"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 20
        cores         = 2
        gpus          = 0
        memory        = 1
    }

    scheduling_policy {
        preemptible = false
    }
}

# yandex_vpc_network.my_network:
resource "yandex_vpc_network" "my_network" {
    created_at                = "2023-09-26T22:00:59Z"
    default_security_group_id = "enpus0o4b692jt8qft19"
    folder_id                 = "b1gcsukd39lji9up1ohe"
    id                        = "enpjvfav2l2pom29080g"
    labels                    = {}
    name                      = "terraform-network"
    subnet_ids                = [
        "e2la6hksalj13g2vu6ma",
    ]
}

# yandex_vpc_subnet.my_subnetwork:
resource "yandex_vpc_subnet" "my_subnetwork" {
    created_at     = "2023-09-26T22:01:02Z"
    folder_id      = "b1gcsukd39lji9up1ohe"
    id             = "e2la6hksalj13g2vu6ma"
    labels         = {}
    name           = "terraform-network-ru-central1-b"
    network_id     = "enpjvfav2l2pom29080g"
    v4_cidr_blocks = [
        "10.129.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}


Outputs:

instance_created_at = "2023-09-26T22:02:42Z"
instance_id = "epdi2ggisto571h7jm1o"

```


- github:

```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "lab-4-terraform"
    repository = "lab-4-terraform"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKYvFIs4CgW50"
    pattern                         = "main"
    repository_id                   = "lab-4-terraform"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        require_code_owner_reviews      = false
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
    archived                    = false
    auto_init                   = true
    branches                    = [
        {
            name      = "main"
            protected = false
        },
    ]
    default_branch              = "main"
    delete_branch_on_merge      = false
    etag                        = "W/\"9040b63642ca4050f924e2dcf80f3fe37b07d3e5b39d0b517bdc1877c9daa6bc\""
    full_name                   = "RakaVaqaFlow/lab-4-terraform"
    git_clone_url               = "git://github.com/RakaVaqaFlow/lab-4-terraform.git"
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/RakaVaqaFlow/lab-4-terraform"
    http_clone_url              = "https://github.com/RakaVaqaFlow/lab-4-terraform.git"
    id                          = "lab-4-terraform"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "lab-4-terraform"
    node_id                     = "R_kgDOKYvFIg"
    private                     = false
    repo_id                     = 697025826
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:RakaVaqaFlow/lab-4-terraform.git"
    svn_url                     = "https://github.com/RakaVaqaFlow/lab-4-terraform"
    visibility                  = "public"
    vulnerability_alerts        = false
}

```