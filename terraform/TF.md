## Terraform practices used:

- **.tfvars file** - used to store the variables. In the repository, there is a `terraform.tfvars.example` file, with fake values. To use it, rename it to `terraform. tfvars` and fill with real values.
- **Documentation** - variables, outputs, and resources were documented.
- **Sensitive data** - used `sensitive = true` for variables, which should not be shown in the output.
- **Separate file structure** - used to separate the variables, outputs, and resources. Also, modules were used for folders.
- **for_each** - used to create docker containers for each app.
- **terraform fmt** - used to format the code. + (todo) - **pre-commit** - used to check the code before commiting.
- **.gitingore file** - used to ignore the tfvars and state files.

## Docker module
### Output of `terraform plan`
```
Terraform will perform the following actions:

  # module.docker_module["app_go"].docker_container.app_container will be created
  + resource "docker_container" "app_container" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "timeapp-go"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + ports {
          + external = 5002
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.docker_module["app_go"].docker_image.app_image will be created
  + resource "docker_image" "app_image" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "vladspigin/timeapp-go:latest"
      + repo_digest  = (known after apply)
    }

  # module.docker_module["app_python"].docker_container.app_container will be created
  + resource "docker_container" "app_container" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "timeapp"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + ports {
          + external = 5001
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.docker_module["app_python"].docker_image.app_image will be created
  + resource "docker_image" "app_image" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "vladspigin/timeapp:latest"
      + repo_digest  = (known after apply)
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = {
      + app_go     = (known after apply)
      + app_python = (known after apply)
    }
  + image_id     = {
      + app_go     = (known after apply)
      + app_python = (known after apply)
    }
```

### Output of `terraform apply`
```
module.docker_module["app_python"].docker_image.app_image: Creating...
module.docker_module["app_go"].docker_image.app_image: Creating...
module.docker_module["app_go"].docker_image.app_image: Still creating... [10s elapsed]
module.docker_module["app_python"].docker_image.app_image: Still creating... [10s elapsed]
module.docker_module["app_python"].docker_image.app_image: Still creating... [20s elapsed]
module.docker_module["app_go"].docker_image.app_image: Still creating... [20s elapsed]
module.docker_module["app_python"].docker_image.app_image: Still creating... [30s elapsed]
module.docker_module["app_go"].docker_image.app_image: Still creating... [30s elapsed]
module.docker_module["app_python"].docker_image.app_image: Creation complete after 31s [id=sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1vladspigin/timeapp:latest]
module.docker_module["app_python"].docker_container.app_container: Creating...
module.docker_module["app_python"].docker_container.app_container: Creation complete after 1s [id=4ebdf894f379856fa087141875c3e216967cb87e5cc03f9d9384073250ecc25a]
module.docker_module["app_go"].docker_image.app_image: Creation complete after 36s [id=sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7vladspigin/timeapp-go:latest]
module.docker_module["app_go"].docker_container.app_container: Creating...
module.docker_module["app_go"].docker_container.app_container: Creation complete after 1s [id=a523bf8f2b96b48444a7319f0398b2697a3e30bbcdde13be194cec14745f6b6b]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

container_id = {
  "app_go" = "a523bf8f2b96b48444a7319f0398b2697a3e30bbcdde13be194cec14745f6b6b"
  "app_python" = "4ebdf894f379856fa087141875c3e216967cb87e5cc03f9d9384073250ecc25a"
}
image_id = {
  "app_go" = "sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7"
  "app_python" = "sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1"
}
```

### Output of `terraform state list`
```
module.docker_module["app_go"].docker_container.app_container
module.docker_module["app_go"].docker_image.app_image
module.docker_module["app_python"].docker_container.app_container
module.docker_module["app_python"].docker_image.app_image
```

### Output of `terraform state show`
```
# module.docker_module["app_go"].docker_container.app_container:
resource "docker_container" "app_container" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "./timeapp",
    ]
    env                                         = []
    hostname                                    = "a523bf8f2b96"
    id                                          = "a523bf8f2b96b48444a7319f0398b2697a3e30bbcdde13be194cec14745f6b6b"
    image                                       = "sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "timeapp-go"
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
    user                                        = "timeapp"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5002
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
```
# module.docker_module["app_go"].docker_image.app_image:
resource "docker_image" "app_image" {
    id           = "sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7vladspigin/timeapp-go:latest"
    image_id     = "sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7"
    keep_locally = false
    name         = "vladspigin/timeapp-go:latest"
    repo_digest  = "vladspigin/timeapp-go@sha256:115de55d89f88a98ff5bc58f100621c2cf8f5c12b55ec982f0e71ec9ccf0b3ff"
}
```
```
# module.docker_module["app_python"].docker_container.app_container:
resource "docker_container" "app_container" {
    attach                                      = false
    command                                     = [
        "sh",
        "-c",
        "uvicorn --host $APP_HOST --port $APP_PORT app.main:app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "4ebdf894f379"
    id                                          = "4ebdf894f379856fa087141875c3e216967cb87e5cc03f9d9384073250ecc25a"
    image                                       = "sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "timeapp"
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
    user                                        = "timeapp"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    healthcheck {
        interval     = "10s"
        retries      = 0
        start_period = "0s"
        test         = [
            "CMD-SHELL",
            "wget --no-verbose --tries=1 --spider http://${APP_HOST}:${APP_PORT}/ || exit 1",
        ]
        timeout      = "3s"
    }

    ports {
        external = 5001
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
```
# module.docker_module["app_python"].docker_image.app_image:
resource "docker_image" "app_image" {
    id           = "sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1vladspigin/timeapp:latest"
    image_id     = "sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1"
    keep_locally = false
    name         = "vladspigin/timeapp:latest"
    repo_digest  = "vladspigin/timeapp@sha256:3b6276e55e8c2e43d02254349d9a7d0b89fb11e0074da3cf10b37e60cc883071"
}
```

### Output of `terraform output`
```
container_id = {
  "app_go" = "a523bf8f2b96b48444a7319f0398b2697a3e30bbcdde13be194cec14745f6b6b"
  "app_python" = "4ebdf894f379856fa087141875c3e216967cb87e5cc03f9d9384073250ecc25a"
}
image_id = {
  "app_go" = "sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7"
  "app_python" = "sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1"
}
```

### Output of `terrafom apply` after **changing Docker container name**.
```
Terraform will perform the following actions:

  # module.docker_module["app_python"].docker_container.app_container must be replaced
-/+ resource "docker_container" "app_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "sh",
          - "-c",
          - "uvicorn --host $APP_HOST --port $APP_PORT app.main:app",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "4ebdf894f379" -> (known after apply)
      ~ id                                          = "4ebdf894f379856fa087141875c3e216967cb87e5cc03f9d9384073250ecc25a" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "timeapp" -> "TIMEAPP-NEW" # forces replacement
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "timeapp" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

      - healthcheck {
          - interval     = "10s" -> null
          - retries      = 0 -> null
          - start_period = "0s" -> null
          - test         = [
              - "CMD-SHELL",
              - "wget --no-verbose --tries=1 --spider http://${APP_HOST}:${APP_PORT}/ || exit 1",
            ] -> null
          - timeout      = "3s" -> null
        }

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = {
      ~ app_python = "4ebdf894f379856fa087141875c3e216967cb87e5cc03f9d9384073250ecc25a" -> (known after apply)
        # (1 unchanged attribute hidden)
    }
```

### Output of `terraform output` after container name changed.
```
Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = {
  "app_go" = "a523bf8f2b96b48444a7319f0398b2697a3e30bbcdde13be194cec14745f6b6b"
  "app_python" = "2888c206746de62adfa857e878a06a7e2386ce29a829405c65dd2d39ed987dfa"
}
image_id = {
  "app_go" = "sha256:85f5244dc8706626c6d5317ea84c8d563e359af04136b93065713c1c53a9f1b7"
  "app_python" = "sha256:ed0bfbca73a0eacd10c7c5641d7e55df53ad84c91dbb0c367687a79bdbba99c1"
}
```

## Yandex cloud module

### Output of `terraform plan`
```
Terraform will perform the following actions:

  # yandex_compute_instance.this will be created
  + resource "yandex_compute_instance" "this" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "devopscourse"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8tf1sepeiku6d37l4l"
              + name        = (known after apply)
              + size        = 20
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }

      + scheduling_policy {
          + preemptible = false
        }
    }

  # yandex_vpc_network.this will be created
  + resource "yandex_vpc_network" "this" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-devopscourse"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.this will be created
  + resource "yandex_vpc_subnet" "this" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet-devopscourse"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "10.5.0.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip = (known after apply)
  + internal_ip = (known after apply)
```

### Output of `terraform apply` (partially)
```
yandex_vpc_network.this: Creating...
yandex_vpc_network.this: Creation complete after 6s [id=enpmv3ljosg3208seooq]
yandex_vpc_subnet.this: Creating...
yandex_vpc_subnet.this: Creation complete after 1s [id=e9bait49ocouql1o3d06]
yandex_compute_instance.this: Creating...
yandex_compute_instance.this: Still creating... [10s elapsed]
yandex_compute_instance.this: Still creating... [20s elapsed]
yandex_compute_instance.this: Still creating... [30s elapsed]
yandex_compute_instance.this: Still creating... [40s elapsed]
yandex_compute_instance.this: Still creating... [50s elapsed]
yandex_compute_instance.this: Still creating... [1m0s elapsed]
yandex_compute_instance.this: Still creating... [1m10s elapsed]
yandex_compute_instance.this: Creation complete after 1m11s [id=fhm9aa8jk664rpk65br5]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

### Output of `terraform output`
```
external_ip = "51.250.65.197"
internal_ip = "10.5.0.18"
```

### Output of `terraform state list`
```
yandex_compute_instance.this
yandex_vpc_network.this
yandex_vpc_subnet.this
```

### Output of `terraform state show`
```
# yandex_compute_instance.this:
resource "yandex_compute_instance" "this" {
    created_at                = "2023-09-24T20:09:33Z"
    folder_id                 = "b1g4ja9n51h5530r8a8b"
    fqdn                      = "fhm9aa8jk664rpk65br5.auto.internal"
    id                        = "fhm9aa8jk664rpk65br5"
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "devopscourse"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmp1r6tlqddbkfh27id"
        disk_id     = "fhmp1r6tlqddbkfh27id"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8tf1sepeiku6d37l4l"
            size       = 20
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
        ip_address         = "10.5.0.18"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:95:29:13:a1"
        nat                = true
        nat_ip_address     = "51.250.65.197"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bait49ocouql1o3d06"
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
```
```
# yandex_vpc_network.this:
resource "yandex_vpc_network" "this" {
    created_at                = "2023-09-24T20:09:28Z"
    default_security_group_id = "enp0ku13agel6ip17fh7"
    folder_id                 = "b1g4ja9n51h5530r8a8b"
    id                        = "enpmv3ljosg3208seooq"
    labels                    = {}
    name                      = "network-devopscourse"
    subnet_ids                = []
}
```
```
# yandex_vpc_subnet.this:
resource "yandex_vpc_subnet" "this" {
    created_at     = "2023-09-24T20:09:31Z"
    folder_id      = "b1g4ja9n51h5530r8a8b"
    id             = "e9bait49ocouql1o3d06"
    labels         = {}
    name           = "subnet-devopscourse"
    network_id     = "enpmv3ljosg3208seooq"
    v4_cidr_blocks = [
        "10.5.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

### Output of `terraform apply` after **changing memory size**.
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # yandex_compute_instance.this will be updated in-place
  ~ resource "yandex_compute_instance" "this" {
      + allow_stopping_for_update = true
        id                        = "fhm9aa8jk664rpk65br5"
        name                      = "devopscourse"
        # (9 unchanged attributes hidden)

      ~ resources {
          ~ memory        = 2 -> 4
            # (3 unchanged attributes hidden)
        }

        # (5 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.
```

### Output of `terraform output` after memory size changed.
```
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

external_ip = "51.250.65.197"
internal_ip = "10.5.0.18"
```

## Github module

### Output of `terraform plan`
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "DevOps course labs at Innopolis University, Fall 2023"
        id                          = "core-course-labs"
        name                        = "core-course-labs"
        # (33 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.
```

### Output of `terraform apply` (partially)
```
github_repository.repo: Modifying... [id=core-course-labs]
github_repository.repo: Modifications complete after 2s [id=core-course-labs]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=core-course-labs]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDOKOKzqM4CgDaR]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

Outputs:

repo_full_name = "vladislav5ik/core-course-labs"
```

## Github Teams module
To create teams, I first created an organization with repo:
https://github.com/vladislav5ik-test-org/core-course-labs.
Then I imported the organization's repo into terraform state.

### Output of `terraform plan`
```
Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "core-course-labs"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "core-course-labs"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      + description                 = "DevOps course labs at Innopolis University, Fall 2023"
        id                          = "core-course-labs"
        name                        = "core-course-labs"
        # (33 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

  # github_team.team["admins"] will be created
  + resource "github_team" "team" {
      + create_default_maintainer = false
      + description               = "Team of admins."
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "admins"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team["devs"] will be created
  + resource "github_team" "team" {
      + create_default_maintainer = false
      + description               = "Team of devs."
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "devs"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team["qa"] will be created
  + resource "github_team" "team" {
      + create_default_maintainer = false
      + description               = "Team of qa."
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "qa"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team_membership.team_membership["admins"] will be created
  + resource "github_team_membership" "team_membership" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = (known after apply)
      + username = "vladislav5ik"
    }

  # github_team_membership.team_membership["devs"] will be created
  + resource "github_team_membership" "team_membership" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = (known after apply)
      + username = "vladislav5ik"
    }

  # github_team_membership.team_membership["qa"] will be created
  + resource "github_team_membership" "team_membership" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "maintainer"
      + team_id  = (known after apply)
      + username = "vladislav5ik"
    }

  # github_team_repository.team_repo["admins"] will be created
  + resource "github_team_repository" "team_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "core-course-labs"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_repo["devs"] will be created
  + resource "github_team_repository" "team_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "core-course-labs"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_repo["qa"] will be created
  + resource "github_team_repository" "team_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "pull"
      + repository = "core-course-labs"
      + team_id    = (known after apply)
    }

Plan: 11 to add, 1 to change, 0 to destroy.
```

### Output of `terraform apply` (partially)
```
github_team.team["devs"]: Creating...
github_team.team["qa"]: Creating...
github_team.team["admins"]: Creating...
github_repository.repo: Modifying... [id=core-course-labs]
github_team.team["qa"]: Still creating... [10s elapsed]
github_team.team["devs"]: Still creating... [10s elapsed]
github_team.team["admins"]: Still creating... [10s elapsed]
github_repository.repo: Still modifying... [id=core-course-labs, 10s elapsed]
github_team.team["admins"]: Creation complete after 13s [id=8645684]
github_repository.repo: Modifications complete after 16s [id=core-course-labs]
github_branch_default.main: Creating...
github_team.team["devs"]: Creation complete after 16s [id=8645685]
github_team.team["qa"]: Creation complete after 16s [id=8645686]
github_team_membership.team_membership["devs"]: Creating...
github_team_membership.team_membership["admins"]: Creating...
github_team_repository.team_repo["qa"]: Creating...
github_team_repository.team_repo["devs"]: Creating...
github_team_membership.team_membership["qa"]: Creating...
github_team_repository.team_repo["admins"]: Creating...
github_team_repository.team_repo["devs"]: Creation complete after 8s [id=8645685:core-course-labs]
github_branch_default.main: Still creating... [10s elapsed]
github_team_membership.team_membership["devs"]: Still creating... [10s elapsed]
github_team_membership.team_membership["admins"]: Still creating... [10s elapsed]
github_team_repository.team_repo["admins"]: Still creating... [10s elapsed]
github_team_repository.team_repo["qa"]: Still creating... [10s elapsed]
github_team_membership.team_membership["qa"]: Still creating... [10s elapsed]
github_branch_default.main: Creation complete after 11s [id=core-course-labs]
github_branch_protection.default: Creating...
github_team_membership.team_membership["devs"]: Creation complete after 11s [id=8645685:vladislav5ik]
github_team_membership.team_membership["admins"]: Creation complete after 12s [id=8645684:vladislav5ik]
github_team_membership.team_membership["qa"]: Creation complete after 12s [id=8645686:vladislav5ik]
github_team_repository.team_repo["admins"]: Creation complete after 12s [id=8645684:core-course-labs]
github_team_repository.team_repo["qa"]: Creation complete after 13s [id=8645686:core-course-labs]
github_branch_protection.default: Creation complete after 6s [id=BPR_kwDOKYG6Ls4CgUKF]

Apply complete! Resources: 11 added, 1 changed, 0 destroyed.
```

### Output of `terraform output`
```
repo_full_name = "vladislav5ik-test-org/core-course-labs"
```

### Changes in Github
After applying terraform, I got the following teams in my organization:
![teams creation proof](github-teams/teams.png)
