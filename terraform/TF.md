# Best practices
* Use `terraform fmt` to update configurations for readiability and consistency
* Use `terraform validate` to validate current configurations
* Use `terraform plan` before each apply
* Use terraform variables

# Docker
## Command outputs
### 'terraform apply':
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform apply
docker_image.moscow_time_app: Refreshing state... [id=sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest]
docker_container.moscow_time_app: Refreshing state... [id=12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851]

No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are
needed.

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

container_id = "12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851"
image_id = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest"
```

#### `terraform state list`:
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform state list
docker_container.moscow_time_app
docker_image.moscow_time_app
```

#### `terraform state show` (image)
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform state show docker_image.moscow_time_app
# docker_image.moscow_time_app:
resource "docker_image" "moscow_time_app" {
    id           = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest"
    image_id     = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784"
    keep_locally = false
    name         = "edikgoose/moscow-time-app:latest"
    repo_digest  = "edikgoose/moscow-time-app@sha256:d102a3c2fbb0cbc9485790c55bbff31a7e8ddf82894dc555152e59eb673bf0ae"
}
```

#### `terraform state show` (container)
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform state show docker_container.moscow_time_app
# docker_container.moscow_time_app:
resource "docker_container" "moscow_time_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "uvicorn",
        "src.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "80",
    ]
    env                                         = []
    hostname                                    = "12cd47cdc1f3"
    id                                          = "12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851"
    image                                       = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-app"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

#### `terraform output`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform$ terraform output
container_id = "12cd47cdc1f344115b5e1095bbc974b97035012d690c09b78001db568f551851"
image_id = "sha256:2c78c87c1edd028f675e605b047dc607c44f8b1d14fe3e94f666c0dbbb1db784edikgoose/moscow-time-app:latest"
```





# Yandex Cloud
#### `terraform apply`
```
data.yandex_vpc_subnet.default_a: Reading...
data.yandex_compute_image.last_ubuntu: Reading...
data.yandex_compute_image.last_ubuntu: Read complete after 2s [id=fd80bm0rh4rkepi5ksdi]
data.yandex_vpc_subnet.default_a: Read complete after 2s [id=e9b72g6d4u511tmovhe2]
yandex_compute_instance.default: Refreshing state... [id=fhm2ap4ib1f29d1j06e0]

Changes to Outputs:
  + default_instance_public_ip = "158.160.33.18"
  + last_ubuntu                = "fd80bm0rh4rkepi5ksdi"
  + subnet_id                  = "e9b72g6d4u511tmovhe2"

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

default_instance_public_ip = "158.160.33.18"
last_ubuntu = "fd80bm0rh4rkepi5ksdi"
subnet_id = "e9b72g6d4u511tmovhe2"
```

#### `terraform state list`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state list
data.yandex_compute_image.last_ubuntu
data.yandex_vpc_subnet.default_a
yandex_compute_instance.default
```

#### `terraform state show data.yandex_compute_image.last_ubuntu`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state show data.yandex_compute_image.last_ubuntu
# data.yandex_compute_image.last_ubuntu:
data "yandex_compute_image" "last_ubuntu" {
    created_at    = "2023-09-25T10:53:45Z"
    description   = "ubuntu 22.04 lts"
    family        = "ubuntu-2204-lts"
    folder_id     = "standard-images"
    id            = "fd80bm0rh4rkepi5ksdi"
    image_id      = "fd80bm0rh4rkepi5ksdi"
    labels        = {}
    min_disk_size = 8
    name          = "ubuntu-22-04-lts-v20230925"
    os_type       = "linux"
    pooled        = true
    product_ids   = [
        "f2e3vsap4cmi4pqk05lg",
    ]
    size          = 7
    status        = "ready"
}
```

#### `terraform state show data.yandex_vpc_subnet.default_a`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state show data.yandex_vpc_subnet.default_a
# data.yandex_vpc_subnet.default_a:
data "yandex_vpc_subnet" "default_a" {
    created_at     = "2023-08-27T19:33:37Z"
    description    = "Auto-created default subnet for zone ru-central1-a in default"
    dhcp_options   = []
    folder_id      = "b1gm00gpfqn5aiom8dn1"
    id             = "e9b72g6d4u511tmovhe2"
    labels         = {}
    name           = "default-ru-central1-a"
    network_id     = "enp98kt2klp1tl362ntp"
    subnet_id      = "e9b72g6d4u511tmovhe2"
    v4_cidr_blocks = [
        "10.128.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

#### `terraform state show yandex_compute_instance.default`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform state show yandex_compute_instance.default
# yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    created_at                = "2023-09-25T22:19:29Z"
    folder_id                 = "b1gm00gpfqn5aiom8dn1"
    fqdn                      = "fhm2ap4ib1f29d1j06e0.auto.internal"
    id                        = "fhm2ap4ib1f29d1j06e0"
    labels                    = {}
    metadata                  = {}
    name                      = "edikgoose-instance"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm9ff8onv3bhgc28hmq"
        disk_id     = "fhm9ff8onv3bhgc28hmq"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd80bm0rh4rkepi5ksdi"
            size       = 8
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
        ip_address         = "10.128.0.22"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:25:64:92:58"
        nat                = true
        nat_ip_address     = "158.160.33.18"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b72g6d4u511tmovhe2"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 5
        cores         = 2
        gpus          = 0
        memory        = 1
    }

    scheduling_policy {
        preemptible = false
    }
}
```

#### `terraform output`
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/terraform/yandex_cloud$ terraform output
default_instance_public_ip = "158.160.33.18"
last_ubuntu = "fd80bm0rh4rkepi5ksdi"
subnet_id = "e9b72g6d4u511tmovhe2"
```