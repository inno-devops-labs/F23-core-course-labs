# Terraform

## Best practices

- Maintain a consistent naming strategy throughout your code to improve readability and maintainability.
- output.tf files to reveal specific values.
- Directories unique to each app
- terraform variables

## Docker

### terraform show
```
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "uvicorn",
        "main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    env                                         = []
    hostname                                    = "09916de7d37c"
    id                                          = "09916de7d37c80ea95da0792343d9bbbcbbfdc14267544dbb9c1f2e4270a40b3"
    image                                       = "sha256:13a31ba39bc63109784df22fa4d497885353da4acec7ea9181ade6f923ac39ba"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "PythonApp"
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
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python/src"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:13a31ba39bc63109784df22fa4d497885353da4acec7ea9181ade6f923ac39bawareverdud/lab3:latest"
    image_id     = "sha256:13a31ba39bc63109784df22fa4d497885353da4acec7ea9181ade6f923ac39ba"
    keep_locally = false
    name         = "wareverdud/lab3:latest"
    repo_digest  = "wareverdud/lab3@sha256:a0b9aafef85c775dd9ee66148d6d8538912bb7e493651e329b6f8d7181dd86a1"
}


Outputs:

container_id = "09916de7d37c80ea95da0792343d9bbbcbbfdc14267544dbb9c1f2e4270a40b3"
image_id = "sha256:13a31ba39bc63109784df22fa4d497885353da4acec7ea9181ade6f923ac39bawareverdud/lab3:latest"
```

### terraform state list
```
docker_container.app_python
docker_image.app_python
```

### terraform output
```
container_id = "09916de7d37c80ea95da0792343d9bbbcbbfdc14267544dbb9c1f2e4270a40b3"
image_id = "sha256:13a31ba39bc63109784df22fa4d497885353da4acec7ea9181ade6f923ac39bawareverdud/lab3:latest"
```

## Yandex Cloud

### terraform state list
```
yandex_compute_image.ubuntu
yandex_compute_instance.vm
yandex_vpc_network.network
yandex_vpc_subnet.subnetwork
```

### terraform show
```
# yandex_compute_image.ubuntu:
resource "yandex_compute_image" "ubuntu" {
    created_at    = "2023-09-29T00:20:27Z"
    folder_id     = "b1gccr3oloqlg8l4ctie"
    id            = "fd860isb2aptsumi8rev"
    min_disk_size = 5
    pooled        = false
    product_ids   = [
        "f2ed6k5slaamr94lfdqu",
    ]
    size          = 4
    source_family = "ubuntu-2004-lts"
    status        = "ready"
}

# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2023-09-29T00:20:37Z"
    folder_id                 = "b1gccr3oloqlg8l4ctie"
    fqdn                      = "fhm28r0dsfr75n9uh63j.auto.internal"
    id                        = "fhm28r0dsfr75n9uh63j"
    name                      = "devops"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmkujpluveg9gmmrnvc"
        disk_id     = "fhmkujpluveg9gmmrnvc"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd860isb2aptsumi8rev"
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
        ip_address         = "10.128.0.17"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:24:6c:0d:e3"
        nat                = true
        nat_ip_address     = "51.250.78.172"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bh6pnvh0trcmn30ge4"
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

# yandex_vpc_network.network:
resource "yandex_vpc_network" "network" {
    created_at                = "2023-09-29T00:20:27Z"
    default_security_group_id = "enprsf1qg32s1eqs2kb4"
    folder_id                 = "b1gccr3oloqlg8l4ctie"
    id                        = "enp81envncca2rus71da"
    labels                    = {}
    name                      = "tf-network"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnetwork:
resource "yandex_vpc_subnet" "subnetwork" {
    created_at     = "2023-09-29T00:20:29Z"
    folder_id      = "b1gccr3oloqlg8l4ctie"
    id             = "e9bh6pnvh0trcmn30ge4"
    labels         = {}
    name           = "tf-network-ru-central1-a"
    network_id     = "enp81envncca2rus71da"
    v4_cidr_blocks = [
        "10.128.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

external_ip = "51.250.78.172"
instance_id = "fhm28r0dsfr75n9uh63j"
```

### terraform output
```
external_ip = "51.250.78.172"
instance_id = "fhm28r0dsfr75n9uh63j"
```

## Github

### terraform state list
```
github_branch_default.main
github_branch_protection.default
github_repository.repo
github_team.team_x
github_team.team_y
github_team_repository.x_repo
github_team_repository.y_repo
```

### terraform show
```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "inno-devops"
    rename     = false
    repository = "inno-devops"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKZ12A84Cgxa3"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "inno-devops"
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
    etag                        = "W/\"d3978ac381985795a5d80384e0e1ff912a9a4cb9cacf6439ed4a00df3fa34e99\""
    full_name                   = "wareverdudx/inno-devops"
    git_clone_url               = "git://github.com/wareverdudx/inno-devops.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/wareverdudx/inno-devops"
    http_clone_url              = "https://github.com/wareverdudx/inno-devops.git"
    id                          = "inno-devops"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "inno-devops"
    node_id                     = "R_kgDOKZ12Aw"
    private                     = false
    repo_id                     = 698185219
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:wareverdudx/inno-devops.git"
    svn_url                     = "https://github.com/wareverdudx/inno-devops"
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

# github_team.team_x:
resource "github_team" "team_x" {
    create_default_maintainer = false
    description               = "Team X"
    etag                      = "W/\"cd47149a6d6b565886748d9bb2e5c8871e6d2f6c5d7b8426b4df962edddb28c9\""
    id                        = "8664165"
    members_count             = 0
    name                      = "team_x"
    node_id                   = "T_kwDOCLp2KM4AhDRl"
    privacy                   = "secret"
    slug                      = "team_x"
}

# github_team.team_y:
resource "github_team" "team_y" {
    create_default_maintainer = false
    description               = "Team Y"
    etag                      = "W/\"ad4713add37fe2b9ad5c46dd8558edfa7d11bf4ca8c78392dbfb1cb942003784\""
    id                        = "8664164"
    members_count             = 0
    name                      = "team_y"
    node_id                   = "T_kwDOCLp2KM4AhDRk"
    privacy                   = "secret"
    slug                      = "team_y"
}

# github_team_repository.x_repo:
resource "github_team_repository" "x_repo" {
    etag       = "W/\"7f27fb707846e734fc05832c763607747eccc78b27a7b5e4f8261df61329be2f\""
    id         = "8664165:inno-devops"
    permission = "admin"
    repository = "inno-devops"
    team_id    = "8664165"
}

# github_team_repository.y_repo:
resource "github_team_repository" "y_repo" {
    etag       = "W/\"88d1e48950d0b3abdd36e52d7b0007cd35dbfc5c138f0107af44ba48f151243c\""
    id         = "8664164:inno-devops"
    permission = "push"
    repository = "inno-devops"
    team_id    = "8664164"
}
```