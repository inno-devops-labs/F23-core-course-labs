# Terraform
## Docker Infrastructure
### After first container created
```bash
[kinjalik@kinjalik-laptop terraform]$ terraform state list
docker_container.nginx
docker_image.nginx
[kinjalik@kinjalik-laptop terraform]$ terraform state show docker_container.nginx
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
    hostname                                    = "bd5e8971fe4c"
    id                                          = "bd5e8971fe4cc51cffc367cc38e9c583e58a113af50ae3c9a137e4036e4bac18"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
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

### Outputs of `terraform output`
```bash
[kinjalik@kinjalik-laptop docker-infra]$ terraform output 
container_id = "34603076bc82ea3cfe5fe322803e48885627ba5fea1a9c6a6a841429dedfefdc"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx"
[kinjalik@kinjalik-laptop docker-infra]$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                  NAMES
34603076bc82   61395b4c586d   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8000->80/tcp   ExampleNginxContainer
[kinjalik@kinjalik-laptop docker-infra]$ 
```

## ~~AWS~~ VK Cloud Infrastructure
**Important note**: I can not us AWS because they reject all russian cards. I don't have any foreign cards (I hope I'll be able to fix it). Tutorial by VK Cloud may be considered as a super-set over the tutoril on AWS, because this tutorials also covers network configuration and firewall configuration. But the result (state and output) also producible.
### Prerequisite
It's said to put password into the file. But I'm not enough stupid to do so, so I put it to env variable
```bash
export TF_VAR_vk_cloud_access_key=[DATA EXPLUNGED]
```

### After instance created
```bash
[kinjalik@kinjalik-laptop cloud-infra]$ terraform state list
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
[kinjalik@kinjalik-laptop cloud-infra]$ terraform state show vkcs_compute_instance.compute
# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.27"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "6346fd48-0f21-4851-9e82-b0e5d7e80445"
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
    tags                = []

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
        fixed_ip_v4    = "192.168.199.27"
        mac            = "fa:16:3e:0d:1e:04"
        name           = "net"
        uuid           = "1674a81f-fdd4-4c45-81de-5ab0b0b32f5d"
    }
}
```

Here you can see I created the EC2 instance according to VK Cloud tutorial. Moreover, I can even SSH inside (cuz security group declared in `network.tf` during the VK's tutorial opens 22 and another port on firewall)

### Terraform output
```bash
[kinjalik@kinjalik-laptop cloud-infra]$ terraform output 
instance_fip = "212.233.95.47"
```
We can see external IP of the instance

## GitHub
```bash
export TF_VAR_token=<PAT>
export GITHUB_USER=kinjalik-test-org
```
Without second it won't work.

**Note:** To accomplish the bonus task I had to use entirely new `kinjalik-test-org`. That means I was unable to perform `terraform init github_repository.repo core-course-labs` to track my actual course rep by Terraform.

```bash
[kinjalik@kinjalik-laptop github]$ terraform state list
github_branch_default.master
github_branch_protection.default
github_repository.repo
github_team.teamA
github_team.teamB
github_team_repository.team_a_to_repo
github_team_repository.team_b_to_repo
[kinjalik@kinjalik-laptop github]$ terraform state show github_repository.repo
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
    description                 = "Assigments for DevOps course"
    etag                        = "W/\"77601f0989713902a96453f223759d0532ff250a604e257dea28af1675dfa44d\""
    full_name                   = "kinjalik-test-org/devops"
    git_clone_url               = "git://github.com/kinjalik-test-org/devops.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/kinjalik-test-org/devops"
    http_clone_url              = "https://github.com/kinjalik-test-org/devops.git"
    id                          = "devops"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops"
    node_id                     = "R_kgDOKYuVbQ"
    private                     = false
    repo_id                     = 697013613
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:kinjalik-test-org/devops.git"
    svn_url                     = "https://github.com/kinjalik-test-org/devops"
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
````

## Terraform best practices
1. Separate terraform files into responsibility areas, like variables, network, providers, etc.
2. Small scope of each fileset (i.e. one for GitHub management, one for VK Cloud management, one for Docker)
3. Variable name convention preserved (i.e. `snake_case`)
4. `terraform fmt` used to keep style consistent
5. `terraform validate` used to check if config is correct
6. Added descriptions for probably-unclear resources