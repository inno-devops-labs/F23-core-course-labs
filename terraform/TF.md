# Terraform

## Best practices

- Use terraform modules to break down your code into smaller, reusable components.
- Declare variables in variables.tf
- Declare outputs in outputs.tf
- As for formatting, apply terraform fmt for each configuration

## Docker

`terraform apply`
Output:

```
docker_image.nginx: Refreshing state... [id=sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94nginx:latest]
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
      + attach           = false
      + bridge           = (known after apply)
      + command          = (known after apply)
      + container_logs   = (known after apply)
      + entrypoint       = (known after apply)
      + env              = (known after apply)
      + exit_code        = (known after apply)
      + gateway          = (known after apply)
      + hostname         = (known after apply)
      + id               = (known after apply)
      + image            = "sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94"
      + init             = (known after apply)
      + ip_address       = (known after apply)
      + ip_prefix_length = (known after apply)
      + ipc_mode         = (known after apply)
      + log_driver       = "json-file"
      + logs             = false
      + must_run         = true
      + name             = "tutorial"
      + network_data     = (known after apply)
      + read_only        = false
      + remove_volumes   = true
      + restart          = "no"
      + rm               = false
      + security_opts    = (known after apply)
      + shm_size         = (known after apply)
      + start            = true
      + stdin_open       = false
      + tty              = false
      + healthcheck {
          + interval     = (known after apply)
          + retries      = (known after apply)
          + start_period = (known after apply)
          + test         = (known after apply)
          + timeout      = (known after apply)
        }
      + labels {
          + label = (known after apply)
          + value = (known after apply)
        }
      + ports {
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }
Plan: 1 to add, 0 to change, 0 to destroy.
╷
│ Warning: Deprecated attribute
│
│   on main.tf line 18, in resource "docker_container" "nginx":
│   18:   image = docker_image.nginx.latest
│
│ The attribute "latest" is deprecated. Refer to the provider documentation for details.
│
│ (and one more similar warning elsewhere)
╵
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=f83b1c748668d635192c523dbdb2cd9fa61fcb3d9181e590dea69f0a8eb0a219]
╷
│ Warning: Deprecated attribute
│
│   on main.tf line 18, in resource "docker_container" "nginx":
│   18:   image = docker_image.nginx.latest
│
│ The attribute "latest" is deprecated. Refer to the provider documentation for details.
│
│ (and one more similar warning elsewhere)
╵
```

`terraform show`

Output:

```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach            = false
    command           = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    cpu_shares        = 0
    entrypoint        = [
        "/docker-entrypoint.sh",
    ]
    env               = []
    gateway           = "172.17.0.1"
    hostname          = "f83b1c748668"
    id                = "f83b1c748668d635192c523dbdb2cd9fa61fcb3d9181e590dea69f0a8eb0a219"
    image             = "sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94"
    init              = false
    ip_address        = "172.17.0.2"
    ip_prefix_length  = 16
    ipc_mode          = "private"
    log_driver        = "json-file"
    logs              = false
    max_retry_count   = 0
    memory            = 0
    memory_swap       = 0
    must_run          = true
    name              = "tutorial"
    network_data      = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            network_name              = "bridge"
        },
    ]
    network_mode      = "default"
    privileged        = false
    publish_all_ports = false
    read_only         = false
    remove_volumes    = true
    restart           = "no"
    rm                = false
    security_opts     = []
    shm_size          = 64
    start             = true
    stdin_open        = false
    tty               = false
    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94nginx:latest"
    keep_locally = false
    latest       = "sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94"
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:6650513efd1d27c1f8a5351cbd33edf85cc7e0d9d0fcb4ffb23d8fa89b601ba8"
}
```

---

`terraform state list`

Output:

```
docker_container.nginx
docker_image.nginx
```

I changed internal port from 8080 to 8088

`terraform show`

```
# docker_container.nginx:
resource "docker_container" "nginx" {
...
    ports {
        external = 8088
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94nginx:latest"
    keep_locally = false
    latest       = "sha256:3f8a00f137a0d2c8a2163a09901e28e2471999fde4efc2f9570b91f1c30acf94"
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:6650513efd1d27c1f8a5351cbd33edf85cc7e0d9d0fcb4ffb23d8fa89b601ba8"
}
```

## Yandex Cloud

Took the configuration from Yandex Cloud official [guide](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart).

`terraform show`

Output:

```
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2023-22-09T19:11:34Z"
    folder_id                 = "b1gepv1qst16sijtnhp7"
    fqdn                      = "fhm320h129cjct4hqm90.auto.internal"
    id                        = "fhm320h129cjct4hqm90"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJmrN4mPXFazoSL2n3WSvjJjLyyG9iodFbyTWI/6kC16 sokratmillman@sokratmillman
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"
    boot_disk {
        auto_delete = true
        device_name = "fhm50g92sejc3sjd7aag"
        disk_id     = "fhm50g92sejc3sjd7aag"
        mode        = "READ_WRITE"
        initialize_params {
            block_size = 4096
            image_id   = "fd8irfoscugmpsoanefh"
            size       = 3
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
        ip_address         = "192.168.10.11"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:31:02:21:12"
        nat                = true
        nat_ip_address     = "51.250.80.86"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bips5c8n4dd0allhu2"
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
    created_at = "2023-02-12T22:11:31Z"
    folder_id  = "b1gepv1qst16sijtnhp7"
    id         = "enpsrfgjuo25u57gkl6g"
    labels     = {}
    name       = "network1"
    subnet_ids = []
}
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-02-12T22:11:32Z"
    folder_id      = "b1gepv1qst16sijtnhp7"
    id             = "e9bips5c8n4dd0allhu2"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpsrfgjuo25u57gkl6g"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

Manually changed service name:

```
yandex_vpc_network.network-1: Refreshing state... [id=enpli1aaifsckp4j3u4o]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9b904eljqnc5cma4amu]
yandex_compute_instance.vm: Refreshing state... [id=fhmm98cicod8c5gablg5]
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place
Terraform will perform the following actions:
  # yandex_compute_instance.vm will be updated in-place
  ~ resource "yandex_compute_instance" "vm" {
        id                        = "fhmm98cicod8c5gablg5"
      ~ name                      = "terraform1" -> "terraform2"
        # (9 unchanged attributes hidden)
        # (6 unchanged blocks hidden)
    }
Plan: 0 to add, 1 to change, 0 to destroy.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
yandex_compute_instance.vm: Modifying... [id=fhmm98cicod8c5gablg5]
yandex_compute_instance.vm: Modifications complete after 5s [id=fhmm98cicod8c5gablg5]
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```
