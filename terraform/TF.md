
---
## Navigation

- [Docker](#docker)
  - [terraform show](#terraform-show)
  - [terraform state list](#terraform-state-list)
  - [apply changes](#apply-changes)
  - [terraform output](#terraform-output)
- [Yandex](#Yandex)
  - [terraform show](#terraform-show)
  - [terraform state list](#terraform-state-list)
  - [apply changes](#apply-changes)
  - [terraform output](#terraform-output)

---

## Docker

---
### terraform show
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
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "5ed970512676"
    id                                          = "5ed9705126764cadbe44b39a016edffd47225e4bf66482b19fdbe428c70df0a8"
    image                                       = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
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
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
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
    id           = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647nginx:latest"
    image_id     = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6"
}
```


--- 

### terraform state list
```
docker_container.nginx
docker_image.nginx
```

---
### apply changes

Changed port number from 8000 to 8080

Log of applying changes

```
docker_image.nginx: Refreshing state... [id=sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647nginx:latest]
docker_container.nginx: Refreshing state... [id=5ed9705126764cadbe44b39a016edffd47225e4bf66482b19fdbe428c70df0a8]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "5ed970512676" -> (known after apply)
      ~ id                                          = "5ed9705126764cadbe44b39a016edffd47225e4bf66482b19fdbe428c70df0a8" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=5ed9705126764cadbe44b39a016edffd47225e4bf66482b19fdbe428c70df0a8]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=781cb629e08fd2b1a31f3ee51c282304fee8ca8af6e5dda6857cb95c6ea96f9a]
```
--- 
### terraform output

```
container_id = "08fdf2c5a040719655da7fe473aa15cc274bade374783f562928ea336be6cd90"
image_id = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647nginx:latest"
```

---

## Yandex

---
### terraform show
```
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-11-21T23:06:38Z"
    folder_id                 = "b1g7f8fjspnqh0o2na1m"
    fqdn                      = "epdttcfsudbas2bk1u8c.auto.internal"
    id                        = "epdttcfsudbas2bk1u8c"
    metadata                  = {
        "serial-port-enable" = "1"
        "user-data"          = <<-EOT
            users:
              - name: devopsubuntu
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh-authorized-keys:
                  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHqurjNO7H/KjYqQrED4nn8mQoPXCmgXDypKSNNbvCrC aibek@ideapad
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdfbgp3v3sstsllqd2q"
        disk_id     = "epdfbgp3v3sstsllqd2q"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8clogg1kull9084s9o"
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
        ip_address         = "192.168.10.16"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1d:eb:1f:cf"
        nat                = true
        nat_ip_address     = "51.250.111.19"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2lpgqupdtua22kq4ci6"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2023-11-21T23:06:34Z"
    default_security_group_id = "enpmpc8k4ia5rqv5fl4i"
    folder_id                 = "b1g7f8fjspnqh0o2na1m"
    id                        = "enpqb0ptlees07q9qias"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-11-21T23:06:36Z"
    folder_id      = "b1g7f8fjspnqh0o2na1m"
    id             = "e2lpgqupdtua22kq4ci6"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpqb0ptlees07q9qias"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}


Outputs:

external_ip_address_vm_1 = "51.250.111.19"
internal_ip_address_vm_1 = "192.168.10.16"
```


--- 

### terraform state list
```
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

---
### apply changes

Changed virtual machine's name

Log of applying changes

```
yandex_vpc_network.network-1: Refreshing state... [id=enpqb0ptlees07q9qias]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e2lpgqupdtua22kq4ci6]
yandex_compute_instance.vm-1: Refreshing state... [id=epdttcfsudbas2bk1u8c]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # yandex_compute_instance.vm-1 will be updated in-place
  ~ resource "yandex_compute_instance" "vm-1" {
        id                        = "epdttcfsudbas2bk1u8c"
      ~ name                      = "terraform1" -> "devops-vm"
        # (9 unchanged attributes hidden)

        # (6 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_instance.vm-1: Modifying... [id=epdttcfsudbas2bk1u8c]
yandex_compute_instance.vm-1: Modifications complete after 7s [id=epdttcfsudbas2bk1u8c]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "51.250.111.19"
internal_ip_address_vm_1 = "192.168.10.16"
```
--- 
### terraform output

```
external_ip_address_vm_1 = "51.250.111.19"
internal_ip_address_vm_1 = "192.168.10.16"
```