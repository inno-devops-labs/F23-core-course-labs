# Terraform Best Practices

## Secrets
I created `.tfvars` files in order to store sensitive variables and access them in other files.
I also set flag `secrets` to tru to use this feature.

## Separate Files
All files are logically split and distributed across many folders for better readability and navigation.

## Clear Folders
I created a `.gitignore` file following standards in order to make my repository clean.

## Validation
I used `terraform validate` to make sure that infrastructure is clean.

## Formatting
Another thing is the usage of `terraform fmt` for files formatting.

# Outputs

## Docker

```
- terraform state show docker_container.app
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "0cd13dbac92f"
    id                                          = "0cd13dbac92f1ad7e0a8815edc066bb8036a79199309449045770d623bcd7d64"
    image                                       = "sha256:a37636aae2ef6c80f6bdd2f938550fba360dabcb9a4a064c3c2265ac1bbdff69"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "innopolis-devops-python-app"
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

- terraform state list
docker_container.app
docker_image.app

- terraform output
container_id = "0cd13dbac92f1ad7e0a8815edc066bb8036a79199309449045770d623bcd7d64"
image_id = "sha256:a37636aae2ef6c80f6bdd2f938550fba360dabcb9a4a064c3c2265ac1bbdff69vladimirka002/innopolis-devops-python-app:latest"
```

## VK Cloud

```
- terraform state show
# data.vkcs_compute_flavor.compute:
data "vkcs_compute_flavor" "compute" {
    disk         = 20
    extra_specs  = {
        "agg_common"     = "true"
        "hw:cpu_sockets" = "1"
        "mcs:cpu_type"   = "standard"
    }
    is_public    = true
    name         = "Basic-1-2-20"
    ram          = 2048
    rx_tx_factor = 1
    swap         = 0
    vcpus        = 1
}

# data.vkcs_images_image.compute:
data "vkcs_images_image" "compute" {
    container_format = "bare"
    created_at       = "2022-08-15T14:12:15Z"
    disk_format      = "raw"
    id               = "ibon18e0cmnzww3niy39fdu4x3yap7mj"
    metadata         = {}
    min_disk_gb      = 0
    min_ram_mb       = 0
    most_recent      = false
    name             = "Ubuntu-22.04-202208"
    owner            = "wd5b810hn78hoz0tecnsrv2g6pma094u"
    protected        = false
    region           = "RegionOne"
    schema           = "/v2/schemas/image"
    size_bytes       = 3758096384
    tags             = []
    updated_at       = "2022-08-16T06:01:24Z"
    visibility       = "public"
}

# data.vkcs_networking_network.extnet:
data "vkcs_networking_network" "extnet" {
    admin_state_up       = "true"
    external             = true
    id                   = "pwf43l0sanxyfda2zh31htprujpwk5rk"
    name                 = "ext-net"
    private_dns_domain   = "openstacklocal."
    region               = "RegionOne"
    sdn                  = "neutron"
    shared               = "true"
    tenant_id            = "09g6r3jvrr8o93fy1aw3i1ey2k31mi1n"
    vkcs_services_access = false
}

# vkcs_compute_floatingip_associate.fip:
resource "vkcs_compute_floatingip_associate" "fip" {
    floating_ip = "95.163.251.14"
    id          = "95.163.251.14/mp9cnwvm-34b3bn-v45bwv-34v34-erv356b7b7/"
    region      = "RegionOne"
}

# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.27"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
        "security_group",
    ]
    stop_before_destroy = false

    block_device {
        boot_index            = 0
        delete_on_termination = true
        destination_type      = "volume"
        source_type           = "image"
        uuid                  = "kgb8mau6z25drrvw9okjwtlkyxyowtay"
        volume_size           = 8
        volume_type           = "ceph-ssd"
    }

    network {
        access_network = false
        fixed_ip_v4    = "192.168.199.27"
        mac            = "fa:16:3e:bc:7c:54"
        name           = "net"
        uuid           = "c1gmbi7jm2qzkwqq43fgsgglimfyjnhd"
    }
}

# vkcs_networking_floatingip.fip:
resource "vkcs_networking_floatingip" "fip" {
    address = "95.163.251.14"
    pool    = "ext-net"
    region  = "RegionOne"
    sdn     = "neutron"
}

# vkcs_networking_network.network:
resource "vkcs_networking_network" "network" {
    admin_state_up        = true
    all_tags              = []
    id                    = "f9y3z6ey2q2epxsjqb9c697mw0lnxsvb"
    name                  = "net"
    port_security_enabled = true
    private_dns_domain    = "mcs.local."
    region                = "RegionOne"
    sdn                   = "neutron"
    tags                  = []
    vkcs_services_access  = false
}

# vkcs_networking_port.port:
resource "vkcs_networking_port" "port" {
    admin_state_up         = true
    all_fixed_ips          = [
        "192.168.199.23",
    ]
    all_tags               = []
    dns_assignment         = [
        {
            "hostname"   = "host-192-168-199-23"
            "ip_address" = "192.168.199.23"
        },
    ]
    mac_address            = "fa:16:3e:ae:0c:18"
    name                   = "port_1"
    port_security_enabled  = true
    region                 = "RegionOne"
    sdn                    = "neutron"
    tags                   = []

    fixed_ip {
        ip_address = "192.168.199.23"
    }
}

# vkcs_networking_port_secgroup_associate.port:
resource "vkcs_networking_port_secgroup_associate" "port" {
    enforce                = false
    region                 = "RegionOne"
    sdn                    = "neutron"
}

# vkcs_networking_router.router:
resource "vkcs_networking_router" "router" {
    admin_state_up      = true
    all_tags            = []
    name                = "router"
    region              = "RegionOne"
    sdn                 = "neutron"
    tags                = []
}

# vkcs_networking_router_interface.db:
resource "vkcs_networking_router_interface" "db" {
    id        = "2fw23523-1233-4536-6326-b24257b7468"
    port_id   = "2fw23523-1233-4536-6326-b24257b7468"
    region    = "RegionOne"
    router_id = "32v32e6232v-215c34-c245c-25c32-325c"
    sdn       = "neutron"
    subnet_id = "34c23-324c32-6bn64n-evwwev-325b453d"
}

- terraform state list
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
```

## Github

```
- terraform state show
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "devops-course-labs"
    rename     = false
    repository = "devops-course-labs"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    force_push_bypassers            = []
    lock_branch                     = false
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "devops-course-labs-infrastructure"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
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
    full_name                   = "vladimirKa002/devops-course-labs"
    git_clone_url               = "git://github.com/vladimirKa002/devops-course-labs.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/vladimirKa002/devops-course-labs"
    http_clone_url              = "https://github.com/vladimirKa002/devops-course-labs.git"
    id                          = "devops-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-course-labs"
    primary_language            = "Python"
    private                     = false
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:vladimirKa002/devops-course-labs.git"
    svn_url                     = "https://github.com/vladimirKa002/devops-course-labs
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

## Teams

```
- terraform state show
# github_team.team["Business"] will be created
  + resource "github_team" "team" {
      + create_default_maintainer = false
      + description               = "Business-people team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Business"
      + node_id                   = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team["Developers"] will be created
  + resource "github_team" "team" {
      + create_default_maintainer = false
      + description               = "Software Developers team"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Developers"
      + node_id                   = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team_membership.membership["Business"] will be created
  + resource "github_team_membership" "membership" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = (known after apply)
      + username = "vladimirKa002"
    }

  # github_team_membership.membership["Developers"] will be created
  + resource "github_team_membership" "membership" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = (known after apply)
      + username = "vladimirKa002"
    }
```