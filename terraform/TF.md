# Docker

```
(venv) purfreak@Tashas-MBP terraform % terraform state list
docker_container.my_python_app
docker_image.image_python_app
```

## docker_container.my_python_app:
```
resource "docker_container" "my_python_app" {
    attach                                      = false
    command                                     = [
        "uvicorn",
        "app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "8a7ee502d65a"
    id                                          = "8a7ee502d65a15b5ee1ea87d164bd36774855deadf2d5ec138abde1f57231bf0"
    image                                       = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my_python_app"
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
    working_dir                                 = "/home/myuser/app"

    ports {
        external = 5555
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## docker_image.image_python_app:
```
resource "docker_image" "image_python_app" {
    id           = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412epurfreak/lab2_devops:latest"
    image_id     = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412e"
    keep_locally = false
    name         = "purfreak/lab2_devops:latest"
}
```

## output:
```
container_id = "d05856b8bbd0ecd92dfe444a9bc980f73b468e8b7ddb4c45ff3b4e4e7a87bc1d"
image_id = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412epurfreak/lab2_devops:latest"
```

# Cloud


```
PS C:\Users\tyref\PycharmProjects\core-course-labs\terraform\vk-cloud> terraform state list
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

## vkcs_compute_instance.compute:

```
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.5"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "15106b50-cc6b-4896-8d8f-2d304f02cca8"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
    ]
    stop_before_destroy = false

    block_device {
        boot_index            = 0
        delete_on_termination = true
        destination_type      = "volume"
        source_type           = "image"
        uuid                  = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
        volume_size           = 8
        volume_type           = "ceph-ssd"
    }

    network {
        access_network = false
        fixed_ip_v4    = "192.168.199.5"
        mac            = "fa:16:3e:12:9f:ee"
        name           = "net"
        uuid           = "9e842fa4-b81c-4af0-92f0-181c6e95613c"
    }
}
```

## data.vkcs_images_image.compute:

```
data "vkcs_images_image" "compute" {
    checksum         = "6d4ade04c95ed136e8c0f2832ee31cd2"
    container_format = "bare"
    created_at       = "2022-08-15T14:12:15Z"
    disk_format      = "raw"
    file             = "/v2/images/b75595ca-4e1d-47e0-8e95-7a02edc0e242/file"
    id               = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
    metadata         = {}
    min_disk_gb      = 0
    min_ram_mb       = 0
    most_recent      = false
    name             = "Ubuntu-22.04-202208"
    owner            = "9d013ed7c41e4bf38dd91f899e40185a"
    protected        = false
    region           = "RegionOne"
    schema           = "/v2/schemas/image"
    size_bytes       = 3758096384
    tags             = []
    updated_at       = "2022-08-16T06:01:24Z"
    visibility       = "public"
}
```

## output:
```
instance_fip = "212.233.95.67"
```

# GitHub

```
PS C:\Users\tyref\PycharmProjects\core-course-labs\terraform\github> terraform state list
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

## github_repository.repo:
```
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
    description                 = "DevOps course lab 4"
    etag                        = "W/\"e8344e71129ac2979ac87a6de826038657900f3e274f1f30ca43d87c21cae3b5\""
    full_name                   = "purfreak/lab4_devops"
    git_clone_url               = "git://github.com/purfreak/lab4_devops.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/purfreak/lab4_devops"
    http_clone_url              = "https://github.com/purfreak/lab4_devops.git"
    id                          = "lab4_devops"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "lab4_devops"
    node_id                     = "R_kgDOKY1RnQ"
    private                     = false
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:purfreak/lab4_devops.git"
    svn_url                     = "https://github.com/purfreak/lab4_devops"
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

# Terraform best practices:

* run `terraform plan` before `terraform apply` to review changes and avoid surprises.
* organise configuration in separate files: `variables.tf` for vars, `outputs.tf` for outputs, `network.tf` for network
* different projects in different folders