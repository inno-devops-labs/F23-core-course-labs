## Docker infra

### `terraform state list`

```
docker_container.python_app_container
docker_image.python_app_image
```

### `terraform state show docker_container.python_app_container`

```
# docker_container.python_app_container:
resource "docker_container" "python_app_container" {
    attach                                      = false
    command                                     = [
        "/bin/sh",
        "-c",
        "uvicorn app:app --host 0.0.0.0 --port 8000 --reload",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "841167891b59"
    id                                          = "841167891b594082d45233d8546c25e98432676146c3b55c1b54052506dc451c"
    image                                       = "sha256:56f509fc4e099818b53e04a05546304b7a4311758045777d8b5d67a2100e3586"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_container"
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
    user                                        = "core_lab_user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### `terraform state show docker_image.python_app_image`

```
# docker_image.python_app_image:
resource "docker_image" "python_app_image" {
    id           = "sha256:56f509fc4e099818b53e04a05546304b7a4311758045777d8b5d67a2100e3586dmitriypru/core_course_labs_python:latest"
    image_id     = "sha256:56f509fc4e099818b53e04a05546304b7a4311758045777d8b5d67a2100e3586"
    keep_locally = false
    name         = "dmitriypru/core_course_labs_python:latest"
    repo_digest  = "dmitriypru/core_course_labs_python@sha256:edacbec6c41c27be5c34a0936e743a0e6e327b7643aaadf67d16e5086c987544"
}
```

### `terraform output`

```
container_id = "841167891b594082d45233d8546c25e98432676146c3b55c1b54052506dc451c"
image_id = "sha256:56f509fc4e099818b53e04a05546304b7a4311758045777d8b5d67a2100e3586dmitriypru/core_course_labs_python:latest"
```

## VK Cloud infra

### `terraform state list`

```
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

### `terraform state show vkcs_compute_instance.compute`

```
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.5"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "ca13f9c4-0ca2-4559-80c7-c9c43376e8b0"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "a7541ad6-80a3-49ad-9710-deacbd93f2be",
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
        mac            = "fa:16:3e:c5:98:ec"
        name           = "net"
        uuid           = "b5ed2a65-8fd5-4da4-afa3-b59d780715cc"
    }
}
```

### `terraform state show data.vkcs_images_image.compute`

```
# data.vkcs_images_image.compute:
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

### `terraform output`

```
instance_fip = "185.130.115.101"
```