## Important: learn-terraform-aws-instance folder was removed as it was larger than 100MB^ which is not possible to push to Github.

## Output of `terraform state show 'docker_container.nginx'`

    #docker_container.nginx:
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
        hostname                                    = "19b7b77e2d15"
        id                                          = "19b7b77e2d15206e497fa166b37b50d881b39f2b4c9915b49a7962362c81c83e"
        image                                       = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
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

## Output of `terraform state show 'docker_image.nginx'`

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
        hostname                                    = "19b7b77e2d15"
        id                                          = "19b7b77e2d15206e497fa166b37b50d881b39f2b4c9915b49a7962362c81c83e"
        image                                       = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
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
    ganslev@MacBook-Pro-5 learn-terraform-docker-container % terraform state show 'docker_image.nginx'
    # docker_image.nginx:
    resource "docker_image" "nginx" {
        id           = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73nginx:latest"
        image_id     = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
        keep_locally = false
        name         = "nginx:latest"
        repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
    }

## Output of `terraform state list`

`docker_container.nginx
docker_image.nginx`


## VK Cloud

`
[ganslev@MacBook-Pro-5 cloud-infra]$ terraform state list
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
[ganslev@MacBook-Pro-5 cloud-infra]$ terraform state show vkcs_compute_instance.compute
# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "194.71.220.204"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "84ce6b10-9443-11ee-b9d1-0242ac120002"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "8a27f374-9443-11ee-b9d1-0242ac120002"
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
        uuid                  = "93db6be4-9443-11ee-b9d1-0242ac120002"
        volume_size           = 8
        volume_type           = "ceph-ssd"
    }

    network {
        access_network = false
        fixed_ip_v4    = "194.71.220.204"
        mac            = "ad:0c:fd:ee:45:97"
        name           = "net"
        uuid           = "971d1f82-9443-11ee-b9d1-0242ac120002"
    }
}
`

## Terraform output 

`
[ganslev@MacBook-Pro-5 cloud-infra]$ terraform output 
instance_fip = "194.244.121.189"
`

## Github

`
[Arseniy172@Arseniy172-laptop github]$ terraform state list
github_branch_default.master
github_branch_protection.default
github_repository.repo
github_team.teamA
github_team.teamB
github_team_repository.team_a_to_repo
github_team_repository.team_b_to_repo
[Arseniy172@Arseniy172-laptop github]$ terraform state show github_repository.repo
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
    etag                        = "W/\"6b2a2e798b111103f9bef3ef9096ebdc7fa0f8c752327f452fa449fa82677468\""
    full_name                   = "Arseniy172-test-org/devops"
    git_clone_url               = "git://github.com/Arseniy172-test-org/devops.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Arseniy172-test-org/devops"
    http_clone_url              = "https://github.com/Arseniy172-test-org/devops.git"
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
    ssh_clone_url               = "git@github.com:Arseniy172-test-org/devops.git"
    svn_url                     = "https://github.com/Arseniy172-test-org/devops"
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
`


## Terraform best practices

To ensure efficient management of terraform files, it is recommended to organize them into different responsibility areas such as variables, network, and providers. Each fileset should have a small scope, for example, one for managing GitHub, VK Cloud, and Docker respectively. It is important to maintain a consistent variable name convention, using snake_case. Consistency in style can be maintained by using terraform fmt. Additionally, terraform validate can be used to ensure that the configuration is correct. To avoid confusion, descriptions should be added for resources that may be unclear.

