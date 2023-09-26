# Results

## Docker results

`terraform state list`

```docker_container.python-app
docker_image.python-app
```

`terraform state show docker_contaoner.python-app`

```
 terraform state show docker_container.python-app
# docker_container.python-app:
resource "docker_container" "python-app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "3982f3e6e64f"
    id                                          = "3982f3e6e64f21a15a3f987e8add5a3e99a541dd4ee14f8c2a54fe58817ce430"
    image                                       = "sha256:fce3be07aedb51b7da21937a7403fd4eaca8f55fe533cebbb894b1d3beb68eb3"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-app"
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
    user                                        = "relisqu"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/python-app"

    ports {
        external = 8080  
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

`terraform state show docker_image.python-app`

``` 
# docker_image.python-app:

resource "docker_image" "python-app" {
    id           = "sha256:fce3be07aedb51b7da21937a7403fd4eaca8f55fe533cebbb894b1d3beb68eb3relisqu/python-app:latest"
    image_id     = "sha256:fce3be07aedb51b7da21937a7403fd4eaca8f55fe533cebbb894b1d3beb68eb3"
    keep_locally = false
    name         = "relisqu/python-app:latest"
    repo_digest  = "relisqu/python-app@sha256:9bbc4554e63f21cc397a34468a3979e9b5c8dd25396d8a1a65e96f64af8ccde6"
}
```

`terraform output`

```container_id = "3982f3e6e64f21a15a3f987e8add5a3e99a541dd4ee14f8c2a54fe58817ce430"
image_id = "sha256:fce3be07aedb51b7da21937a7403fd4eaca8f55fe533cebbb894b1d3beb68eb3relisqu/python-app:latest"
```

## VK Cloud results

`terraform state list`

```data.vkcs_compute_flavor.compute
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
vkcs_networking_secgroup_rule.secgroup_rule
vkcs_networking_subnet.subnetwork
```

`terraform state show`

```vkcs_compute_instance.compute
# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.10.4"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"     
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "f834243a-7278-41a9-ab0f-eed6d3934c10"     
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "admin",
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
        fixed_ip_v4    = "192.168.10.4"
        mac            = "fa:16:3e:35:7a:62"
        name           = "net"
        uuid           = "f7265ae5-3669-4c76-b9db-056592151015"      
    }
}
```

`terraform output`

```
instance_fip = "84.23.53.144"
```

## Github results

For github-org I used this envieroment variable in windows:
`GITHUB_OWNER=relisqu-org`


`terraform apply`

```
github_repository.repo: Creating...
github_repository.repo: Creation complete after 5s [id=devops-terraform-labs]
github_team_repository.team_a_to_repo: Creating...
github_branch_default.main: Creating...
github_team_repository.team_b_to_repo: Creating...
github_team_repository.team_a_to_repo: Creation complete after 5s [id=8646745:devops-terraform-labs]
github_branch_default.main: Creation complete after 5s [id=devops-terraform-labs]
github_branch_protection.default: Creating...
github_team_repository.team_b_to_repo: Creation complete after 6s [id=8646744:devops-terraform-labs]
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDOKYtacM4CgWLx]
```

`terraform state list`

```
github_branch_default.main
github_branch_protection.default
github_repository.repo
github_team.team-a
github_team.team-b
github_team_repository.team_a_to_repo
github_team_repository.team_b_to_repo
```


## Best practices for Terraform

1. Small scope of each fileset- one for each task: GitHub, VK Cloud management, Docker
2. Used `terraform fmt` and `terraform validate` to keep style consistent and to check if config is correct.
3. `snake_case` name convention preserved
4. I separated terraform files into responsibility areas, like variables, network, providers, outputs.
