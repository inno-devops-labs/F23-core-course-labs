# Docker
## List states
```
terraform state list
```
Output:
```
docker_container.app
docker_image.app
```
## Show states
```
terraform show
```
Output:
```
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
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
    group_add                                   = []
    hostname                                    = "b4a7d27508d2"
    id                                          = "b4a7d27508d2405e0f9fd565802ed7904bc0ba7e5e1de6fcab5beb7125a2eeb6"
    image                                       = "sha256:dc1eeb85be48ec8a00299957bb5ce46777b6564886b05b430e239770ef57793e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
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
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    user                                        = "2000"
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:dc1eeb85be48ec8a00299957bb5ce46777b6564886b05b430e239770ef57793ezrrrget/app_python"
    image_id     = "sha256:dc1eeb85be48ec8a00299957bb5ce46777b6564886b05b430e239770ef57793e"
    keep_locally = false
    name         = "zrrrget/app_python"
    repo_digest  = "zrrrget/app_python@sha256:c7820e23bc709b7b21083b53cc454782b813a0b8cd7e7f16475f6cc538c08a40"
}
```
## Terraform outputs:
```
terraform output
```
Output:
```
container_id = "b4a7d27508d2405e0f9fd565802ed7904bc0ba7e5e1de6fcab5beb7125a2eeb6"
image_id = "sha256:dc1eeb85be48ec8a00299957bb5ce46777b6564886b05b430e239770ef57793ezrrrget/app_python"
```
# Yandex
Creates vm resource.
Following guidelines were used:

https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart
https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-state-storage

```
terraform init -backend-config="access_key=$ACCESS_KEY"-backend-config="secret_key=$SECRET_KEY"

terraform apply -var="cloud_id=1234" -var="folder_id=5678" -var="service_account_key_file=.../authorized_key.json"
```

```
terraform state list
yandex_compute_image.ubuntu_2004
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```
terraform show
# yandex_compute_image.ubuntu_2004:
resource "yandex_compute_image" "ubuntu_2004" {
    created_at    = "2023-09-23T11:54:11Z"
    folder_id     = "b1gvv93ogsnc6djj51qr"
    id            = "fd8k9tg169k1tjectipg"
    min_disk_size = 5
    pooled        = false
    product_ids   = [
        "f2enn1chbcbvfegk0qgf",
    ]
    size          = 4
    source_family = "ubuntu-2004-lts"
    status        = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-09-23T11:54:23Z"
    folder_id                 = "b1gvv93ogsnc6djj51qr"
    fqdn                      = "fhmkhbvc8vc12cp91v23.auto.internal"
    id                        = "fhmkhbvc8vc12cp91v23"
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmio3cpul31fp2idjk8"
        disk_id     = "fhmio3cpul31fp2idjk8"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8k9tg169k1tjectipg"
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
        ip_address         = "10.130.0.9"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:14:8a:fe:c4"
        nat                = true
        nat_ip_address     = "158.160.115.53"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b67sur2dlad5v0ggb1"
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
    created_at                = "2023-09-23T11:54:11Z"
    default_security_group_id = "enp65jmelhhbs86373bq"
    folder_id                 = "b1gvv93ogsnc6djj51qr"
    id                        = "enpbhiqsumuqr7172e0j"
    labels                    = {}
    name                      = "default2"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-09-23T11:54:14Z"
    folder_id      = "b1gvv93ogsnc6djj51qr"
    id             = "e9b67sur2dlad5v0ggb1"
    labels         = {}
    name           = "default-ru-central1-a2"
    network_id     = "enpbhiqsumuqr7172e0j"
    v4_cidr_blocks = [
        "10.130.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```
# Github
```
terraform show
# github_branch_default.master:
resource "github_branch_default" "master" {
    branch     = "main"
    id         = "core-course-labs"
    repository = "core-course-labs"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKOllVM4Cf9Z4"
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "core-course-labs_generated"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# github_repository.core-course-labs:
resource "github_repository" "core-course-labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    archived                    = false
    auto_init                   = true
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
            name      = "main"
            protected = true
        },
    ]
    default_branch              = "main"
    delete_branch_on_merge      = false
    etag                        = "W/\"b04914aa73c58b56523610d964ac585d797e282333bb1e1a4ae71f1860a4cbe0\""
    full_name                   = "zRrrGet/core-course-labs"
    git_clone_url               = "git://github.com/zRrrGet/core-course-labs.git"
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/zRrrGet/core-course-labs"
    http_clone_url              = "https://github.com/zRrrGet/core-course-labs.git"
    id                          = "core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "core-course-labs"
    node_id                     = "R_kgDOKOllVA"
    private                     = false
    repo_id                     = 686384468
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:zRrrGet/core-course-labs.git"
    svn_url                     = "https://github.com/zRrrGet/core-course-labs"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
}
```

# Best practices
- Same name convention(underscores are used)
- Variables are stored in variables.tf
- Outputs are stored in outputs.tf
- Proper variable/output names