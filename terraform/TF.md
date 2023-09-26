### Docker
terraform show
```
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
    hostname                                    = "d4ad6e505d6b"
    id                                          = "d4ad6e505d6b25e7715ae387d831640d0040344ccc261dc560727b6034463e6d"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "BMW-m5"
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
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

terraform state list
```
docker_container.nginx
docker_image.nginx
```

terraform output
```
container_id = "328c3c851e0b76868c442459cf3fecca3dfc81db11b1cb27d9067f13083803c4"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
```

### VK Cloud
terraform show
```
# vkcs_networking_network.sfs:
resource "vkcs_networking_network" "sfs" {
    admin_state_up        = true
    all_tags              = []
    id                    = "1183312b-1126-4809-ad18-9bcac87cd2b4"
    name                  = "network"
    port_security_enabled = true
    private_dns_domain    = "mcs.local."
    region                = "RegionOne"
    sdn                   = "neutron"
    vkcs_services_access  = false
}

# vkcs_networking_subnet.sfs:
resource "vkcs_networking_subnet" "sfs" {
    all_tags    = []
    cidr        = "192.168.199.0/24"
    enable_dhcp = true
    gateway_ip  = "192.168.199.1"
    id          = "a77a050b-1247-4490-87a2-92b8e295cdaa"
    name        = "subnet"
    network_id  = "1183312b-1126-4809-ad18-9bcac87cd2b4"
    no_gateway  = false
    region      = "RegionOne"
    sdn         = "neutron"

    allocation_pool {
        end   = "192.168.199.254"
        start = "192.168.199.2"
    }
}

# vkcs_sharedfilesystem_share.share:
resource "vkcs_sharedfilesystem_share" "share" {
    all_metadata         = {}
    availability_zone    = "GZ1"
    description          = "test share description"
    export_location_path = "192.168.199.5:/shares/share-e2258885-f691-4804-b020-300aba951a09"
    id                   = "9d388c8c-7597-4807-b1d4-dc83baf42a7b"
    name                 = "nfs_share"
    project_id           = "f67d34fb24434924a4d606a2eb5e1f46"
    region               = "RegionOne"
    share_network_id     = "b9e805ee-2561-4da3-88a9-872f27063d1d"
    share_proto          = "NFS"
    share_type           = "default_share_type"
    size                 = 1
}

# vkcs_sharedfilesystem_share_access.share_access_1:
resource "vkcs_sharedfilesystem_share_access" "share_access_1" {
    access_level = "rw"
    access_to    = "192.168.199.10"
    access_type  = "ip"
    id           = "42edd896-7f12-4b57-b37f-c34b590decd5"
    region       = "RegionOne"
    share_id     = "9d388c8c-7597-4807-b1d4-dc83baf42a7b"
}

# vkcs_sharedfilesystem_share_access.share_access_2:
resource "vkcs_sharedfilesystem_share_access" "share_access_2" {
    access_level = "rw"
    access_to    = "192.168.199.11"
    access_type  = "ip"
    id           = "0e091818-c70b-4daf-aa86-d0b3916f74c8"
    region       = "RegionOne"
    share_id     = "9d388c8c-7597-4807-b1d4-dc83baf42a7b"
}

# vkcs_sharedfilesystem_sharenetwork.sharenetwork:
resource "vkcs_sharedfilesystem_sharenetwork" "sharenetwork" {
    id                = "b9e805ee-2561-4da3-88a9-872f27063d1d"
    name              = "test_sharenetwork"
    neutron_net_id    = "1183312b-1126-4809-ad18-9bcac87cd2b4"
    neutron_subnet_id = "a77a050b-1247-4490-87a2-92b8e295cdaa"
    project_id        = "f67d34fb24434924a4d606a2eb5e1f46"
    region            = "RegionOne"
}
```

terraform state list
```
vkcs_networking_network.sfs
vkcs_networking_subnet.sfs
vkcs_sharedfilesystem_share.share
vkcs_sharedfilesystem_share_access.share_access_1
vkcs_sharedfilesystem_share_access.share_access_2
vkcs_sharedfilesystem_sharenetwork.sharenetwork
```

### GitHub
terraform show
```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "Pwd9000-Demo-Repo-2022"
    repository = "Pwd9000-Demo-Repo-2022"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKYfKJc4CgRU4"
    pattern                         = "main"
    repository_id                   = "Pwd9000-Demo-Repo-2022"
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
    description                 = "My awesome codebase"
    etag                        = "W/\"b6a10db85b2ceaa02a5f29be42f5765f1452b7ed71a96f41b37197ee728e6c5d\""
    full_name                   = "kolbasaegor/Pwd9000-Demo-Repo-2022"
    git_clone_url               = "git://github.com/kolbasaegor/Pwd9000-Demo-Repo-2022.git"
    gitignore_template          = "VisualStudio"
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/kolbasaegor/Pwd9000-Demo-Repo-2022"
    http_clone_url              = "https://github.com/kolbasaegor/Pwd9000-Demo-Repo-2022.git"
    id                          = "Pwd9000-Demo-Repo-2022"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "Pwd9000-Demo-Repo-2022"
    node_id                     = "R_kgDOKYfKJQ"
    private                     = false
    repo_id                     = 696764965
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:kolbasaegor/Pwd9000-Demo-Repo-2022.git"
    svn_url                     = "https://github.com/kolbasaegor/Pwd9000-Demo-Repo-2022"
    visibility                  = "public"
    vulnerability_alerts        = false
}
```

terraform state list
```
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

## Best practices
1. Infrastructure is provisioned through a UI or CLI
2. Source files are stored in version control to record editing history
3. Some Terraform code is split out into modules
