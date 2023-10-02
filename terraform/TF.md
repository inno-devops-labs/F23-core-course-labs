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
- terraform state show vkcs_compute_instance.compute
# data.vkcs_compute_flavor.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.10"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "b5f998e9-aea0-4b78-9efd-7613ea8da8b0"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
        "ssh",
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
        fixed_ip_v4    = "192.168.199.10"
        mac            = "fa:16:3e:98:55:55"
        name           = "net"
        uuid           = "bd4070de-541b-4e06-8557-8acbc1c55270"
    }
}

- terraform state list
data.vkcs_compute_flavor.compute
data.vkcs_images_image.compute
data.vkcs_networking_network.extnet
vkcs_compute_floatingip_associate.fip
vkcs_compute_instance.compute
vkcs_networking_floatingip.fip
vkcs_networking_network.network
vkcs_networking_router.router
vkcs_networking_router_interface.db
vkcs_networking_secgroup.ssh_secgroup
vkcs_networking_secgroup_rule.ssh_secgroup_rule_1
vkcs_networking_secgroup_rule.ssh_secgroup_rule_2
vkcs_networking_subnet.subnetwork

- terraform output
instance_fip = "84.23.55.246"
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

To create teams in Github one has to use organization. For this, I created a 'inno-devops-vladimirKa002-org' organization.
 Then, using Terraform I created multiple teams with different access levels:
 ![teams](github/assets/Teams.png)