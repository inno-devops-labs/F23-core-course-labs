# Docker
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
    hostname                                    = "15e4d9a9d30b"
    id                                          = "15e4d9a9d30bf57069b631c15fe4ebb28f2f2ac518b0c4bd432b92d5bf734126"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "lab4"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}


Outputs:

container_id = "15e4d9a9d30bf57069b631c15fe4ebb28f2f2ac518b0c4bd432b92d5bf734126"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
```

docker_container.nginx
docker_image.nginx

# VK Cloud

```
# vkcs_networking_network.sfs:
resource "vkcs_networking_network" "sfs" {
    admin_state_up        = true
    all_tags              = []
    id                    = "f3fc195f-77e2-4c3e-b558-5e143c322d40"
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
    id          = "26989b8a-e5ba-466a-8173-ef37e99cc872"
    name        = "subnet"
    network_id  = "f3fc195f-77e2-4c3e-b558-5e143c322d40"
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
    export_location_path = "192.168.199.14:/shares/share-185bbc78-0ad0-46de-a036-48ecb8eb0e9a"
    id                   = "a659b29e-fa29-4797-8f33-6c2fa92f30ed"
    name                 = "nfs_share"
    project_id           = "72277e66c77e48119575839dcc4d5808"
    region               = "RegionOne"
    share_network_id     = "b604f769-57eb-47ee-bd21-2a88797c6047"
    share_proto          = "NFS"
    share_type           = "default_share_type"
    size                 = 1
}

# vkcs_sharedfilesystem_share_access.share_access_1:
resource "vkcs_sharedfilesystem_share_access" "share_access_1" {
    access_level = "rw"
    access_to    = "192.168.199.10"
    access_type  = "ip"
    id           = "4e75d96c-ad2e-4539-bd35-0e508d6984a3"
    region       = "RegionOne"
    share_id     = "a659b29e-fa29-4797-8f33-6c2fa92f30ed"
}

# vkcs_sharedfilesystem_share_access.share_access_2:
resource "vkcs_sharedfilesystem_share_access" "share_access_2" {
    access_level = "rw"
    access_to    = "192.168.199.11"
    access_type  = "ip"
    id           = "9b271ed4-19f5-40f1-b967-cc1ff501b1fb"
    region       = "RegionOne"
    share_id     = "a659b29e-fa29-4797-8f33-6c2fa92f30ed"
}

# vkcs_sharedfilesystem_sharenetwork.sharenetwork:
resource "vkcs_sharedfilesystem_sharenetwork" "sharenetwork" {
    id                = "b604f769-57eb-47ee-bd21-2a88797c6047"
    name              = "test_sharenetwork"
    neutron_net_id    = "f3fc195f-77e2-4c3e-b558-5e143c322d40"
    neutron_subnet_id = "26989b8a-e5ba-466a-8173-ef37e99cc872"
    project_id        = "72277e66c77e48119575839dcc4d5808"
    region            = "RegionOne"
}
```
# github_branch_default.main:
resource "github_branch_default" "main" {
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
    id                              = "BPR_kwDOKPhVk84CgSms"
    pattern                         = "main"
    repository_id                   = "core-course-labs"
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

# github_repository.terraform:
```
resource "github_repository" "terraform" {
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
            protected = false
        },
    ]
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "My awesome codebase"
    etag                        = "W/\"ace393e7020633b0284e24c09cd4012b77535fe478703983fe83c18d84aad180\""
    full_name                   = "IlyaMirzazhanov/core-course-labs"
    git_clone_url               = "git://github.com/IlyaMirzazhanov/core-course-labs.git"
    gitignore_template          = "VisualStudio"
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/IlyaMirzazhanov/core-course-labs"
    http_clone_url              = "https://github.com/IlyaMirzazhanov/core-course-labs.git"
    id                          = "core-course-labs"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "core-course-labs"
    node_id                     = "R_kgDOKPhVkw"
    private                     = false
    repo_id                     = 687363475
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:IlyaMirzazhanov/core-course-labs.git"
    svn_url                     = "https://github.com/IlyaMirzazhanov/core-course-labs"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
}
```
# Terraform best practices:

* small scope of each fileset (for VK cloud management, for Docker, for GitHub)
* separate terraform files into special folders, like variables, network, providers, etc.
* Variable name convention preserved (i.e. snake_case)
* terraform validate used to check if config is correct
* included descriptions for probably-unclear resources
