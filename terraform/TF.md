# First run of terraform 

## Terraform apply
```
ruslan@Elestrias:~/Downloads/devops/core-course-labs/terraform$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.app_python.docker_container.app will be created
  + resource "docker_container" "app" {
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
      + name                                        = "python_app"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = true
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.app_python.docker_image.gilvanov_image will be created
  + resource "docker_image" "gilvanov_image" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "dashvayet/python_app"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + python_container_id = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
```

## Terraform show
```
# module.app_python.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python3",
        "src/web/__main__.py",
    ]
    env                                         = []
    hostname                                    = "1ea74375cafb"
    id                                          = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e"
    image                                       = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
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
    rm                                          = true
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
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app"
    image_id     = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    keep_locally = false
    name         = "dashvayet/python_app"
    repo_digest  = "dashvayet/python_app@sha256:08179edca5cf76d7211fe165d2e4f374f4c9c03b2a0dff7dc79d81a17ae42eee"
}


Outputs:

python_container_id = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e"
```

## Terraform state list
```
module.app_python.docker_container.app
module.app_python.docker_image.gilvanov_image
```

# Add new container + rename it to distinguish
## terraform apply
```
terraform apply
module.app_python.docker_image.gilvanov_image: Refreshing state... [id=sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app]
module.app_python.docker_container.app: Refreshing state... [id=1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.app_cpp.docker_container.app will be created
  + resource "docker_container" "app" {
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
      + name                                        = "app_cplusplus"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = true
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
          + external = 10000
          + internal = 10000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.app_cpp.docker_image.gilvanov_image will be created
  + resource "docker_image" "gilvanov_image" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "dashvayet/app_cplusplus"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + cplusplus_container_id = (known after apply)
```

## terraform show
```
# module.app_cpp.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "./startServer",
        "10000",
    ]
    env                                         = []
    hostname                                    = "8565371ab5c9"
    id                                          = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
    image                                       = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_cplusplus"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/startServer"

    ports {
        external = 10000
        internal = 10000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_cpp.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus"
    image_id     = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    keep_locally = false
    name         = "dashvayet/app_cplusplus"
    repo_digest  = "dashvayet/app_cplusplus@sha256:e87bc1f6118617cbe110b9b9a38e97d9cfa9251c08f9a4ce64b29af52011853d"
}
# module.app_python.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "python3",
        "src/web/__main__.py",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "1ea74375cafb"
    id                                          = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e"
    image                                       = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app"
    image_id     = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    keep_locally = false
    name         = "dashvayet/python_app"
    repo_digest  = "dashvayet/python_app@sha256:08179edca5cf76d7211fe165d2e4f374f4c9c03b2a0dff7dc79d81a17ae42eee"
}


Outputs:

cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
python_container_id = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e"
```

## terraform output
```
ruslan@Elestrias:~/Downloads/devops/core-course-labs/terraform$ terraform output
cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
python_container_id = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e"
```

# Rename container
## terraform apply
```
 terraform apply
module.app_cpp.docker_image.gilvanov_image: Refreshing state... [id=sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus]
module.app_python.docker_image.gilvanov_image: Refreshing state... [id=sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app]
module.app_cpp.docker_container.app: Refreshing state... [id=8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a]
module.app_python.docker_container.app: Refreshing state... [id=1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # module.app_python.docker_container.app must be replaced
-/+ resource "docker_container" "app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python3",
          - "src/web/__main__.py",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "1ea74375cafb" -> (known after apply)
      ~ id                                          = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "python_app" -> "python_app_new" # forces replacement
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
      - user                                        = "app" -> null
      - working_dir                                 = "/usr/src/app" -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ python_container_id    = "1ea74375cafb5a38ee327ab5216284bc7a5df8d7ccaf0f866ae7dfd77e21546e" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
```

## terraform output
```
cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
python_container_id = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
```
## terraform state show
I forgot to do it at this step, but I dont think it is crucial, so states will be after cloud establish step

# Yandex cloud establish
## terraform apply
```
terraform apply
module.app_python.docker_image.gilvanov_image: Refreshing state... [id=sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app]
module.app_cpp.docker_image.gilvanov_image: Refreshing state... [id=sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus]
module.app_cpp.docker_container.app: Refreshing state... [id=8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a]
module.app_python.docker_container.app: Refreshing state... [id=52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Reading...
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Read complete after 1s [id=fd80bm0rh4rkepi5ksdi]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.yandex_cloud.yandex_compute_instance.default will be created
  + resource "yandex_compute_instance" "default" {
      + allow_stopping_for_update = true
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = "test-hostname"
      + id                        = (known after apply)
      + metadata                  = {
          + "serial-port-enable" = "1"
          + "ssh-keys"           = "ubuntu:"
        }
      + name                      = "test-name"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd80bm0rh4rkepi5ksdi"
              + name        = (known after apply)
              + size        = (known after apply)
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
          + memory        = 4
        }
    }

  # module.yandex_cloud.yandex_vpc_address.vm1 will be created
  + resource "yandex_vpc_address" "vm1" {
      + created_at          = (known after apply)
      + deletion_protection = (known after apply)
      + folder_id           = (known after apply)
      + id                  = (known after apply)
      + labels              = (known after apply)
      + name                = "vm1-devops"
      + reserved            = (known after apply)
      + used                = (known after apply)

      + external_ipv4_address {
          + address                  = (known after apply)
          + ddos_protection_provider = (known after apply)
          + outgoing_smtp_capability = (known after apply)
          + zone_id                  = "ru-central1-a"
        }
    }

  # module.yandex_cloud.yandex_vpc_network.networkabobus will be created
  + resource "yandex_vpc_network" "networkabobus" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = (known after apply)
      + subnet_ids                = (known after apply)
    }

  # module.yandex_cloud.yandex_vpc_subnet.networkabobus will be created
  + resource "yandex_vpc_subnet" "networkabobus" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "10.228.0.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.
```
## terraform show
```
# module.app_cpp.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "./startServer",
        "10000",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "8565371ab5c9"
    id                                          = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
    image                                       = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_cplusplus"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/startServer"

    ports {
        external = 10000
        internal = 10000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_cpp.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus"
    image_id     = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    keep_locally = false
    name         = "dashvayet/app_cplusplus"
    repo_digest  = "dashvayet/app_cplusplus@sha256:e87bc1f6118617cbe110b9b9a38e97d9cfa9251c08f9a4ce64b29af52011853d"
}
# module.app_python.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "python3",
        "src/web/__main__.py",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "52e2799b3094"
    id                                          = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
    image                                       = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_new"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app"
    image_id     = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    keep_locally = false
    name         = "dashvayet/python_app"
    repo_digest  = "dashvayet/python_app@sha256:08179edca5cf76d7211fe165d2e4f374f4c9c03b2a0dff7dc79d81a17ae42eee"
}
# module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts:
data "yandex_compute_image" "ubuntu-2204-lts" {
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

# module.yandex_cloud.yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2023-09-26T18:53:26Z"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    fqdn                      = "test-hostname.ru-central1.internal"
    hostname                  = "test-hostname"
    id                        = "fhmlcl03cikb1pukln4l"
    metadata                  = {
        "serial-port-enable" = "1"
        "ssh-keys"           = "ubuntu:"
    }
    name                      = "test-name"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm85ikvvhghi9jk5llr"
        disk_id     = "fhm85ikvvhghi9jk5llr"
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
        ip_address         = "10.228.0.13"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:15:65:40:36"
        nat                = true
        nat_ip_address     = "51.250.74.138"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bp8vmvjliadgj9aejf"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }
}

# module.yandex_cloud.yandex_vpc_address.vm1:
resource "yandex_vpc_address" "vm1" {
    created_at          = "2023-09-26T18:53:24Z"
    deletion_protection = false
    folder_id           = "b1gkr31c0tt9f3k2cm7b"
    id                  = "e9b3c9n91nonlm4lvrf2"
    labels              = {}
    name                = "vm1-devops"
    reserved            = true
    used                = false

    external_ipv4_address {
        address = "51.250.74.138"
        zone_id = "ru-central1-a"
    }
}

# module.yandex_cloud.yandex_vpc_network.networkabobus:
resource "yandex_vpc_network" "networkabobus" {
    created_at                = "2023-09-26T18:53:23Z"
    default_security_group_id = "enp9rl6mte2q3d7c04m7"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    id                        = "enpua36rqgpijoah84qb"
    labels                    = {}
    subnet_ids                = []
}

# module.yandex_cloud.yandex_vpc_subnet.networkabobus:
resource "yandex_vpc_subnet" "networkabobus" {
    created_at     = "2023-09-26T18:53:25Z"
    folder_id      = "b1gkr31c0tt9f3k2cm7b"
    id             = "e9bp8vmvjliadgj9aejf"
    labels         = {}
    network_id     = "enpua36rqgpijoah84qb"
    v4_cidr_blocks = [
        "10.228.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
python_container_id = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
```
# Update and change values for vm
## terraform apply
```
module.app_cpp.docker_image.gilvanov_image: Refreshing state... [id=sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus]
module.app_python.docker_image.gilvanov_image: Refreshing state... [id=sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app]
module.app_cpp.docker_container.app: Refreshing state... [id=8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a]
module.app_python.docker_container.app: Refreshing state... [id=52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988]
module.yandex_cloud.yandex_vpc_network.networkabobus: Refreshing state... [id=enpua36rqgpijoah84qb]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Reading...
module.yandex_cloud.yandex_vpc_address.vm1: Refreshing state... [id=e9b3c9n91nonlm4lvrf2]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Read complete after 1s [id=fd80bm0rh4rkepi5ksdi]
module.yandex_cloud.yandex_vpc_subnet.networkabobus: Refreshing state... [id=e9bp8vmvjliadgj9aejf]
module.yandex_cloud.yandex_compute_instance.default: Refreshing state... [id=fhmlcl03cikb1pukln4l]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # module.yandex_cloud.yandex_compute_instance.default will be updated in-place
  ~ resource "yandex_compute_instance" "default" {
        id                        = "fhmlcl03cikb1pukln4l"
      ~ name                      = "test-name" -> "test-name-updated"
        # (11 unchanged attributes hidden)

        # (6 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + vm_external_ip         = "51.250.74.138"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: 
```

## terraform show
```
# module.app_cpp.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "./startServer",
        "10000",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "8565371ab5c9"
    id                                          = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
    image                                       = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_cplusplus"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/startServer"

    ports {
        external = 10000
        internal = 10000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_cpp.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus"
    image_id     = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    keep_locally = false
    name         = "dashvayet/app_cplusplus"
    repo_digest  = "dashvayet/app_cplusplus@sha256:e87bc1f6118617cbe110b9b9a38e97d9cfa9251c08f9a4ce64b29af52011853d"
}
# module.app_python.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "python3",
        "src/web/__main__.py",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "52e2799b3094"
    id                                          = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
    image                                       = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_new"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app"
    image_id     = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    keep_locally = false
    name         = "dashvayet/python_app"
    repo_digest  = "dashvayet/python_app@sha256:08179edca5cf76d7211fe165d2e4f374f4c9c03b2a0dff7dc79d81a17ae42eee"
}
# module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts:
data "yandex_compute_image" "ubuntu-2204-lts" {
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

# module.yandex_cloud.yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2023-09-26T18:53:26Z"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    fqdn                      = "test-hostname.ru-central1.internal"
    hostname                  = "test-hostname"
    id                        = "fhmlcl03cikb1pukln4l"
    labels                    = {}
    metadata                  = {
        "serial-port-enable" = "1"
        "ssh-keys"           = "ubuntu:"
    }
    name                      = "test-name-updated"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm85ikvvhghi9jk5llr"
        disk_id     = "fhm85ikvvhghi9jk5llr"
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
        ip_address         = "10.228.0.13"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:15:65:40:36"
        nat                = true
        nat_ip_address     = "51.250.74.138"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bp8vmvjliadgj9aejf"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }
}

# module.yandex_cloud.yandex_vpc_address.vm1:
resource "yandex_vpc_address" "vm1" {
    created_at          = "2023-09-26T18:53:24Z"
    deletion_protection = false
    folder_id           = "b1gkr31c0tt9f3k2cm7b"
    id                  = "e9b3c9n91nonlm4lvrf2"
    labels              = {}
    name                = "vm1-devops"
    reserved            = true
    used                = true

    external_ipv4_address {
        address = "51.250.74.138"
        zone_id = "ru-central1-a"
    }
}

# module.yandex_cloud.yandex_vpc_network.networkabobus:
resource "yandex_vpc_network" "networkabobus" {
    created_at                = "2023-09-26T18:53:23Z"
    default_security_group_id = "enp9rl6mte2q3d7c04m7"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    id                        = "enpua36rqgpijoah84qb"
    labels                    = {}
    subnet_ids                = [
        "e9bp8vmvjliadgj9aejf",
    ]
}

# module.yandex_cloud.yandex_vpc_subnet.networkabobus:
resource "yandex_vpc_subnet" "networkabobus" {
    created_at     = "2023-09-26T18:53:25Z"
    folder_id      = "b1gkr31c0tt9f3k2cm7b"
    id             = "e9bp8vmvjliadgj9aejf"
    labels         = {}
    network_id     = "enpua36rqgpijoah84qb"
    v4_cidr_blocks = [
        "10.228.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
python_container_id = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
vm_external_ip = "51.250.74.138"
```

## terraform output
```
cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
python_container_id = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
vm_external_ip = "51.250.74.138"
```

# Final results of 10 points task
## terraform state list
```
module.app_cpp.docker_container.app
module.app_cpp.docker_image.gilvanov_image
module.app_python.docker_container.app
module.app_python.docker_image.gilvanov_image
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
module.yandex_cloud.yandex_compute_instance.default
module.yandex_cloud.yandex_vpc_address.vm1
module.yandex_cloud.yandex_vpc_network.networkabobus
module.yandex_cloud.yandex_vpc_subnet.networkabobus
```

## terraform state show
Resource: module.app_cpp.docker_container.app
```
# module.app_cpp.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "./startServer",
        "10000",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "8565371ab5c9"
    id                                          = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
    image                                       = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_cplusplus"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/startServer"

    ports {
        external = 10000
        internal = 10000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```
------------------------------------------------------------
Resource: module.app_cpp.docker_image.gilvanov_image
```
# module.app_cpp.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus"
    image_id     = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    keep_locally = false
    name         = "dashvayet/app_cplusplus"
    repo_digest  = "dashvayet/app_cplusplus@sha256:e87bc1f6118617cbe110b9b9a38e97d9cfa9251c08f9a4ce64b29af52011853d"
}

```
------------------------------------------------------------
Resource: module.app_python.docker_container.app
```
# module.app_python.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "python3",
        "src/web/__main__.py",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "52e2799b3094"
    id                                          = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
    image                                       = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app_new"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```
------------------------------------------------------------
Resource: module.app_python.docker_image.gilvanov_image
```
# module.app_python.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app"
    image_id     = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    keep_locally = false
    name         = "dashvayet/python_app"
    repo_digest  = "dashvayet/python_app@sha256:08179edca5cf76d7211fe165d2e4f374f4c9c03b2a0dff7dc79d81a17ae42eee"
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
```
# module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts:
data "yandex_compute_image" "ubuntu-2204-lts" {
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
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_compute_instance.default
```
# module.yandex_cloud.yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2023-09-26T18:53:26Z"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    fqdn                      = "test-hostname.ru-central1.internal"
    hostname                  = "test-hostname"
    id                        = "fhmlcl03cikb1pukln4l"
    metadata                  = {
        "serial-port-enable" = "1"
        "ssh-keys"           = "ubuntu:"
    }
    name                      = "test-name"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm85ikvvhghi9jk5llr"
        disk_id     = "fhm85ikvvhghi9jk5llr"
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
        ip_address         = "10.228.0.13"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:15:65:40:36"
        nat                = true
        nat_ip_address     = "51.250.74.138"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bp8vmvjliadgj9aejf"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_vpc_address.vm1
```
# module.yandex_cloud.yandex_vpc_address.vm1:
resource "yandex_vpc_address" "vm1" {
    created_at          = "2023-09-26T18:53:24Z"
    deletion_protection = false
    folder_id           = "b1gkr31c0tt9f3k2cm7b"
    id                  = "e9b3c9n91nonlm4lvrf2"
    labels              = {}
    name                = "vm1-devops"
    reserved            = true
    used                = false

    external_ipv4_address {
        address = "51.250.74.138"
        zone_id = "ru-central1-a"
    }
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_vpc_network.networkabobus
```
# module.yandex_cloud.yandex_vpc_network.networkabobus:
resource "yandex_vpc_network" "networkabobus" {
    created_at                = "2023-09-26T18:53:23Z"
    default_security_group_id = "enp9rl6mte2q3d7c04m7"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    id                        = "enpua36rqgpijoah84qb"
    labels                    = {}
    subnet_ids                = []
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_vpc_subnet.networkabobus
```
# module.yandex_cloud.yandex_vpc_subnet.networkabobus:
resource "yandex_vpc_subnet" "networkabobus" {
    created_at     = "2023-09-26T18:53:25Z"
    folder_id      = "b1gkr31c0tt9f3k2cm7b"
    id             = "e9bp8vmvjliadgj9aejf"
    labels         = {}
    network_id     = "enpua36rqgpijoah84qb"
    v4_cidr_blocks = [
        "10.228.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}

```
------------------------------------------------------------
# Github integration
## terraform apply
```
module.app_python.docker_image.gilvanov_image: Refreshing state... [id=sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app]
module.app_cpp.docker_image.gilvanov_image: Refreshing state... [id=sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus]
module.app_cpp.docker_container.app: Refreshing state... [id=8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a]
module.app_python.docker_container.app: Refreshing state... [id=52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Reading...
module.yandex_cloud.yandex_vpc_network.networkabobus: Refreshing state... [id=enpua36rqgpijoah84qb]
module.yandex_cloud.yandex_vpc_address.vm1: Refreshing state... [id=e9b3c9n91nonlm4lvrf2]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Read complete after 0s [id=fd80bm0rh4rkepi5ksdi]
module.yandex_cloud.yandex_vpc_subnet.networkabobus: Refreshing state... [id=e9bp8vmvjliadgj9aejf]
module.yandex_cloud.yandex_compute_instance.default: Refreshing state... [id=fhmlcl03cikb1pukln4l]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.github.github_branch_default.core_main will be created
  + resource "github_branch_default" "core_main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "devopsTest"
    }

  # module.github.github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "Devops_repo"
    }

  # module.github.github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false
    }

  # module.github.github_repository.core will be created
  + resource "github_repository" "core" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Innopolis DevOps 2023 core repository"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devopsTest"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
    }

  # module.github.github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = false
      + allow_squash_merge          = false
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Devops_repo"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "Devops_repo"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
    }

Plan: 5 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + github_repo_name       = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

```

## terraform output
```
cplusplus_container_id = "8565371ab5c9806c382de29293d883690c7a476c9f1554a6cc22944d6a55503a"
github_repo_name = "Elestrias/Devops_repo"
python_container_id = "52e2799b3094d955a084b72ba375c0cfe6828a6fd8b09936246495d710f6f988"
vm_external_ip = "51.250.74.138"
```

# Making import repo
```
github_repository.core: Refreshing state... [id=test-import]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.core_main will be created
  + resource "github_branch_default" "core_main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "devopsTest"
    }

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + rename     = false
      + repository = "Devops_repo"
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
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false
    }

  # github_repository.core will be updated in-place
  ~ resource "github_repository" "core" {
      ~ auto_init                   = false -> true
      + description                 = "Innopolis DevOps 2023 core repository"
      ~ full_name                   = "Elestrias/test-import" -> (known after apply)
      - has_downloads               = true -> null
      - has_issues                  = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "test-import"
      ~ name                        = "test-import" -> "devopsTest"
        # (26 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = false
      + allow_squash_merge          = false
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Devops_repo"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "Devops_repo"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
    }

Plan: 4 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + repo_name = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
```

## terraform show

```
# github_branch_default.core_main:
resource "github_branch_default" "core_main" {
    branch     = "main"
    id         = "devopsTest"
    rename     = false
    repository = "devopsTest"
}

# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "Devops_repo"
    rename     = false
    repository = "Devops_repo"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKYtqL84CgWT1"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "Devops_repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false
}

# github_repository.core:
resource "github_repository" "core" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Innopolis DevOps 2023 core repository"
    etag                        = "W/\"374e2515d4b35540362537cbe6b332ec5ba08493f822ed933b53c9b9bbdbc60b\""
    full_name                   = "Elestrias/devopsTest"
    git_clone_url               = "git://github.com/Elestrias/devopsTest.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Elestrias/devopsTest"
    http_clone_url              = "https://github.com/Elestrias/devopsTest.git"
    id                          = "devopsTest"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devopsTest"
    node_id                     = "R_kgDOKYtnhQ"
    private                     = false
    repo_id                     = 697001861
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Elestrias/devopsTest.git"
    svn_url                     = "https://github.com/Elestrias/devopsTest"
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

# github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = false
    allow_squash_merge          = false
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Devops_repo"
    etag                        = "W/\"fcee9573eb0a529b353c8431f1a8fa12eac608c149de6867f6da04046c9d8be4\""
    full_name                   = "Elestrias/Devops_repo"
    git_clone_url               = "git://github.com/Elestrias/Devops_repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Elestrias/Devops_repo"
    http_clone_url              = "https://github.com/Elestrias/Devops_repo.git"
    id                          = "Devops_repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "Devops_repo"
    node_id                     = "R_kgDOKYtqLw"
    private                     = false
    repo_id                     = 697002543
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Elestrias/Devops_repo.git"
    svn_url                     = "https://github.com/Elestrias/Devops_repo"
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


Outputs:

repo_name = "Elestrias/Devops_repo"
```

## terraform state list
```
github_branch_default.core_main
github_branch_default.main
github_branch_protection.default
github_repository.core
github_repository.repo
```

## terraform state show 
Resource: github_branch_default.core_main
```
# github_branch_default.core_main:
resource "github_branch_default" "core_main" {
    branch     = "main"
    id         = "devopsTest"
    rename     = false
    repository = "devopsTest"
}

```
------------------------------------------------------------
Resource: github_branch_default.main
```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "Devops_repo"
    rename     = false
    repository = "Devops_repo"
}

```
------------------------------------------------------------
Resource: github_branch_protection.default
```
# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKYuiKc4CgWts"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "Devops_repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false
}

```
------------------------------------------------------------
Resource: github_repository.core
```
# github_repository.core:
resource "github_repository" "core" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Innopolis DevOps 2023 core repository"
    etag                        = "W/\"2fc008142f4618fce692083f2b58c0692cc7bbdf3d54f6f7984aa045a1e86281\""
    full_name                   = "Elestrias/devopsTest"
    git_clone_url               = "git://github.com/Elestrias/devopsTest.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Elestrias/devopsTest"
    http_clone_url              = "https://github.com/Elestrias/devopsTest.git"
    id                          = "devopsTest"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devopsTest"
    node_id                     = "R_kgDOKYuhcg"
    private                     = false
    repo_id                     = 697016690
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Elestrias/devopsTest.git"
    svn_url                     = "https://github.com/Elestrias/devopsTest"
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
------------------------------------------------------------
Resource: github_repository.repo
```
# github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = false
    allow_squash_merge          = false
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Devops_repo"
    etag                        = "W/\"a73c19bbc5b230e72a1f836a2c1ba03d6ba1f690e391dd2e061ce08a5a00f967\""
    full_name                   = "Elestrias/Devops_repo"
    git_clone_url               = "git://github.com/Elestrias/Devops_repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Elestrias/Devops_repo"
    http_clone_url              = "https://github.com/Elestrias/Devops_repo.git"
    id                          = "Devops_repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "Devops_repo"
    node_id                     = "R_kgDOKYuiKQ"
    private                     = false
    repo_id                     = 697016873
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Elestrias/Devops_repo.git"
    svn_url                     = "https://github.com/Elestrias/Devops_repo"
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
------------------------------------------------------------



# Best practices
1. Use reusable modules to not duplicate code
2. Separate terraform project on different levels - directories for each module to keep all structure clear
3. Use ```terraform plan``` and ```terraform validate``` to check your work before applying
4. Use  ```terraform fmt``` for formatting your declarations
5. Use variables to parametrize your solution
6. Use outputs to keep significant values in easy access
7. Do not put validation tokens or other sensitive data inside your declarations
8. Take as less resources as you your solution allows you to reduces cloud spending (cloud could be really expensive for companies)
9. Use only reliable providers and always update the version of modules and machines you are going to use

# Github teams
## terraform apply
```
var.github_organization
  Enter a value: ElestriasOrg 


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_repository.example_repo will be created
  + resource "github_repository" "example_repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Example repo"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "ExampleRepository"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
    }

  # github_team.team_admin will be created
  + resource "github_team" "team_admin" {
      + create_default_maintainer = false
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-admin"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team_pull will be created
  + resource "github_team" "team_pull" {
      + create_default_maintainer = false
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-pull"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team.team_push will be created
  + resource "github_team" "team_push" {
      + create_default_maintainer = false
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "team-push"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "secret"
      + slug                      = (known after apply)
    }

  # github_team_repository.team_admin_access will be created
  + resource "github_team_repository" "team_admin_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = "ExampleRepository"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_pull_access will be created
  + resource "github_team_repository" "team_pull_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "pull"
      + repository = "ExampleRepository"
      + team_id    = (known after apply)
    }

  # github_team_repository.team_push_access will be created
  + resource "github_team_repository" "team_push_access" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "ExampleRepository"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

github_team.team_push: Creation complete after 19s [id=8646899]
github_repository.example_repo: Creation complete after 19s [id=ExampleRepository]
github_team_repository.team_push_access: Creating...
github_team_repository.team_pull_access: Creating...
github_team_repository.team_admin_access: Creating...
github_team_repository.team_push_access: Creation complete after 5s [id=8646899:ExampleRepository]
github_team_repository.team_admin_access: Creation complete after 5s [id=8646898:ExampleRepository]
github_team_repository.team_pull_access: Creation complete after 6s [id=8646897:ExampleRepository]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
```

## terraform show
```
# github_repository.example_repo:
resource "github_repository" "example_repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Example repo"
    etag                        = "W/\"b8235088d439063ecd8912c5daeeac9bda241627c3c45fc6f35617e736b27851\""
    full_name                   = "ElestriasOrg/ExampleRepository"
    git_clone_url               = "git://github.com/ElestriasOrg/ExampleRepository.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/ElestriasOrg/ExampleRepository"
    http_clone_url              = "https://github.com/ElestriasOrg/ExampleRepository.git"
    id                          = "ExampleRepository"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "ExampleRepository"
    node_id                     = "R_kgDOKYt6dg"
    private                     = false
    repo_id                     = 697006710
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:ElestriasOrg/ExampleRepository.git"
    svn_url                     = "https://github.com/ElestriasOrg/ExampleRepository"
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

# github_team.team_admin:
resource "github_team" "team_admin" {
    create_default_maintainer = false
    etag                      = "W/\"35ed1135618f892395a34893b438906611ed14cd211a5dd496677cc8d8a3b38f\""
    id                        = "8646898"
    members_count             = 0
    name                      = "team-admin"
    node_id                   = "T_kwDOCLK5Bc4Ag_Dy"
    privacy                   = "secret"
    slug                      = "team-admin"
}

# github_team.team_pull:
resource "github_team" "team_pull" {
    create_default_maintainer = false
    etag                      = "W/\"ca581fabefeeb73294381dd4f297460f7e0ae45c799f57eb759c388c35cf49f4\""
    id                        = "8646897"
    members_count             = 0
    name                      = "team-pull"
    node_id                   = "T_kwDOCLK5Bc4Ag_Dx"
    privacy                   = "secret"
    slug                      = "team-pull"
}

# github_team.team_push:
resource "github_team" "team_push" {
    create_default_maintainer = false
    etag                      = "W/\"99cdbe20f5aa367bd91f00e64df18959b36b0409bd94b86c1b7adbc1d02d699b\""
    id                        = "8646899"
    members_count             = 0
    name                      = "team-push"
    node_id                   = "T_kwDOCLK5Bc4Ag_Dz"
    privacy                   = "secret"
    slug                      = "team-push"
}

# github_team_repository.team_admin_access:
resource "github_team_repository" "team_admin_access" {
    etag       = "W/\"0e378cfb5f82d67062298fea4b0bb3a193e0f96c869743b3012e47dd30569ba5\""
    id         = "8646898:ExampleRepository"
    permission = "admin"
    repository = "ExampleRepository"
    team_id    = "8646898"
}

# github_team_repository.team_pull_access:
resource "github_team_repository" "team_pull_access" {
    etag       = "W/\"0127b1acac7c69ea77a6c9231f9a3a0c2be7728a08ec09a43c1bdd1d02b71d0a\""
    id         = "8646897:ExampleRepository"
    permission = "pull"
    repository = "ExampleRepository"
    team_id    = "8646897"
}

# github_team_repository.team_push_access:
resource "github_team_repository" "team_push_access" {
    etag       = "W/\"12587599a8eb6918d8d547a1dcf49993b57ba363c2b6573c07de557b53625d7f\""
    id         = "8646899:ExampleRepository"
    permission = "push"
    repository = "ExampleRepository"
    team_id    = "8646899"
}
```

## terraform state list
```
github_repository.example_repo
github_team.team_admin
github_team.team_pull
github_team.team_push
github_team_repository.team_admin_access
github_team_repository.team_pull_access
github_team_repository.team_push_access
```

## terraform state show for each 
Resource: github_repository.example_repo
```
# github_repository.example_repo:
resource "github_repository" "example_repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Example repo"
    etag                        = "W/\"b8235088d439063ecd8912c5daeeac9bda241627c3c45fc6f35617e736b27851\""
    full_name                   = "ElestriasOrg/ExampleRepository"
    git_clone_url               = "git://github.com/ElestriasOrg/ExampleRepository.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/ElestriasOrg/ExampleRepository"
    http_clone_url              = "https://github.com/ElestriasOrg/ExampleRepository.git"
    id                          = "ExampleRepository"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "ExampleRepository"
    node_id                     = "R_kgDOKYt6dg"
    private                     = false
    repo_id                     = 697006710
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:ElestriasOrg/ExampleRepository.git"
    svn_url                     = "https://github.com/ElestriasOrg/ExampleRepository"
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
------------------------------------------------------------
Resource: github_team.team_admin
```
# github_team.team_admin:
resource "github_team" "team_admin" {
    create_default_maintainer = false
    etag                      = "W/\"35ed1135618f892395a34893b438906611ed14cd211a5dd496677cc8d8a3b38f\""
    id                        = "8646898"
    members_count             = 0
    name                      = "team-admin"
    node_id                   = "T_kwDOCLK5Bc4Ag_Dy"
    privacy                   = "secret"
    slug                      = "team-admin"
}

```
------------------------------------------------------------
Resource: github_team.team_pull
```
# github_team.team_pull:
resource "github_team" "team_pull" {
    create_default_maintainer = false
    etag                      = "W/\"ca581fabefeeb73294381dd4f297460f7e0ae45c799f57eb759c388c35cf49f4\""
    id                        = "8646897"
    members_count             = 0
    name                      = "team-pull"
    node_id                   = "T_kwDOCLK5Bc4Ag_Dx"
    privacy                   = "secret"
    slug                      = "team-pull"
}

```
------------------------------------------------------------
Resource: github_team.team_push
```
# github_team.team_push:
resource "github_team" "team_push" {
    create_default_maintainer = false
    etag                      = "W/\"99cdbe20f5aa367bd91f00e64df18959b36b0409bd94b86c1b7adbc1d02d699b\""
    id                        = "8646899"
    members_count             = 0
    name                      = "team-push"
    node_id                   = "T_kwDOCLK5Bc4Ag_Dz"
    privacy                   = "secret"
    slug                      = "team-push"
}

```
------------------------------------------------------------
Resource: github_team_repository.team_admin_access
```
# github_team_repository.team_admin_access:
resource "github_team_repository" "team_admin_access" {
    etag       = "W/\"0e378cfb5f82d67062298fea4b0bb3a193e0f96c869743b3012e47dd30569ba5\""
    id         = "8646898:ExampleRepository"
    permission = "admin"
    repository = "ExampleRepository"
    team_id    = "8646898"
}

```
------------------------------------------------------------
Resource: github_team_repository.team_pull_access
```
# github_team_repository.team_pull_access:
resource "github_team_repository" "team_pull_access" {
    etag       = "W/\"0127b1acac7c69ea77a6c9231f9a3a0c2be7728a08ec09a43c1bdd1d02b71d0a\""
    id         = "8646897:ExampleRepository"
    permission = "pull"
    repository = "ExampleRepository"
    team_id    = "8646897"
}

```
------------------------------------------------------------
Resource: github_team_repository.team_push_access
```
# github_team_repository.team_push_access:
resource "github_team_repository" "team_push_access" {
    etag       = "W/\"12587599a8eb6918d8d547a1dcf49993b57ba363c2b6573c07de557b53625d7f\""
    id         = "8646899:ExampleRepository"
    permission = "push"
    repository = "ExampleRepository"
    team_id    = "8646899"
}

```
------------------------------------------------------------
## Results can be observed
![img.png](img.png)

# Final all infrastructure states
# Terraform state list
```
module.app_cpp.docker_container.app
module.app_cpp.docker_image.gilvanov_image
module.app_python.docker_container.app
module.app_python.docker_image.gilvanov_image
module.github.github_branch_default.core_main
module.github.github_branch_default.main
module.github.github_branch_protection.default
module.github.github_repository.core
module.github.github_repository.repo
module.github_teams.github_repository.example_repo
module.github_teams.github_team.team_admin
module.github_teams.github_team.team_pull
module.github_teams.github_team.team_push
module.github_teams.github_team_repository.team_admin_access
module.github_teams.github_team_repository.team_pull_access
module.github_teams.github_team_repository.team_push_access
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
module.yandex_cloud.yandex_compute_instance.default
module.yandex_cloud.yandex_vpc_address.vm1
module.yandex_cloud.yandex_vpc_network.networkabobus
module.yandex_cloud.yandex_vpc_subnet.networkabobus
```

# **Terraform state** for each module
Resource: module.app_cpp.docker_container.app
```
# module.app_cpp.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "./startServer",
        "10000",
    ]
    env                                         = []
    hostname                                    = "870420f7857c"
    id                                          = "870420f7857cfd4a2820bb730d460cd75933edf433f6ab7408ba3011e67950b8"
    image                                       = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_cplusplus"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/startServer"

    ports {
        external = 10000
        internal = 10000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```
------------------------------------------------------------
Resource: module.app_cpp.docker_image.gilvanov_image
```
# module.app_cpp.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212dashvayet/app_cplusplus"
    image_id     = "sha256:b4bfcf8ce5ea1d369665c6ca806812603caac20e36231042749459271c94f212"
    keep_locally = false
    name         = "dashvayet/app_cplusplus"
    repo_digest  = "dashvayet/app_cplusplus@sha256:e87bc1f6118617cbe110b9b9a38e97d9cfa9251c08f9a4ce64b29af52011853d"
}

```
------------------------------------------------------------
Resource: module.app_python.docker_container.app
```
# module.app_python.docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python3",
        "src/web/__main__.py",
    ]
    env                                         = []
    hostname                                    = "03616b6ad93c"
    id                                          = "03616b6ad93cb905f29ca2496196a5bb8f3e943027fc83fbb07606e4cbbca57f"
    image                                       = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
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
    rm                                          = true
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
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```
------------------------------------------------------------
Resource: module.app_python.docker_image.gilvanov_image
```
# module.app_python.docker_image.gilvanov_image:
resource "docker_image" "gilvanov_image" {
    id           = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30ccdashvayet/python_app"
    image_id     = "sha256:731b1d549df2bdfe8b78f940f1b113cccbe2013c19df9c5f45fb9e43a8eb30cc"
    keep_locally = false
    name         = "dashvayet/python_app"
    repo_digest  = "dashvayet/python_app@sha256:08179edca5cf76d7211fe165d2e4f374f4c9c03b2a0dff7dc79d81a17ae42eee"
}

```
------------------------------------------------------------
Resource: module.github.github_branch_default.core_main
```
# module.github.github_branch_default.core_main:
resource "github_branch_default" "core_main" {
    branch     = "main"
    id         = "devopsTest"
    rename     = false
    repository = "devopsTest"
}

```
------------------------------------------------------------
Resource: module.github.github_branch_default.main
```
# module.github.github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "Devops_repo"
    rename     = false
    repository = "Devops_repo"
}

```
------------------------------------------------------------
Resource: module.github.github_branch_protection.default
```
# module.github.github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOKYdhE84CgQ7g"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "Devops_repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false
}

```
------------------------------------------------------------
Resource: module.github.github_repository.core
```
# module.github.github_repository.core:
resource "github_repository" "core" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Innopolis DevOps 2023 core repository"
    etag                        = "W/\"84876b3a4fd4d2717ce7866ea50ea565726c1e6ce9bc42b2b413f5e809777294\""
    full_name                   = "Elestrias/devopsTest"
    git_clone_url               = "git://github.com/Elestrias/devopsTest.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Elestrias/devopsTest"
    http_clone_url              = "https://github.com/Elestrias/devopsTest.git"
    id                          = "devopsTest"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devopsTest"
    node_id                     = "R_kgDOKYdhJQ"
    private                     = false
    repo_id                     = 696738085
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Elestrias/devopsTest.git"
    svn_url                     = "https://github.com/Elestrias/devopsTest"
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
------------------------------------------------------------
Resource: module.github.github_repository.repo
```
# module.github.github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = false
    allow_squash_merge          = false
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Devops_repo"
    etag                        = "W/\"bf439ec55095fb6d8e3b2b1a3637bcc34241f26a54eca2bbe2c138545d2f3c25\""
    full_name                   = "Elestrias/Devops_repo"
    git_clone_url               = "git://github.com/Elestrias/Devops_repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Elestrias/Devops_repo"
    http_clone_url              = "https://github.com/Elestrias/Devops_repo.git"
    id                          = "Devops_repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "Devops_repo"
    node_id                     = "R_kgDOKYdhEw"
    private                     = false
    repo_id                     = 696738067
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Elestrias/Devops_repo.git"
    svn_url                     = "https://github.com/Elestrias/Devops_repo"
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
------------------------------------------------------------
Resource: module.github_teams.github_repository.example_repo
```
# module.github_teams.github_repository.example_repo:
resource "github_repository" "example_repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Example repo"
    etag                        = "W/\"9acec6ad848d96efe285841112c978a8f42e57b8a723a519d9097556501feb60\""
    full_name                   = "ElestriasOrg/ExampleRepository"
    git_clone_url               = "git://github.com/ElestriasOrg/ExampleRepository.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/ElestriasOrg/ExampleRepository"
    http_clone_url              = "https://github.com/ElestriasOrg/ExampleRepository.git"
    id                          = "ExampleRepository"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "ExampleRepository"
    node_id                     = "R_kgDOKYdhNQ"
    private                     = false
    repo_id                     = 696738101
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:ElestriasOrg/ExampleRepository.git"
    svn_url                     = "https://github.com/ElestriasOrg/ExampleRepository"
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
------------------------------------------------------------
Resource: module.github_teams.github_team.team_admin
```
# module.github_teams.github_team.team_admin:
resource "github_team" "team_admin" {
    create_default_maintainer = false
    etag                      = "W/\"62e3c3417d064e91d206d5660e884c256cfec2ae3424b0e35d8080892aa23011\""
    id                        = "8643181"
    members_count             = 0
    name                      = "team-admin"
    node_id                   = "T_kwDOCLK5Bc4Ag-Jt"
    privacy                   = "secret"
    slug                      = "team-admin"
}

```
------------------------------------------------------------
Resource: module.github_teams.github_team.team_pull
```
# module.github_teams.github_team.team_pull:
resource "github_team" "team_pull" {
    create_default_maintainer = false
    etag                      = "W/\"f52e127b08899daae5f20f90e42e06bb33ea798df3c3de137127ebacdc4ba744\""
    id                        = "8643183"
    members_count             = 0
    name                      = "team-pull"
    node_id                   = "T_kwDOCLK5Bc4Ag-Jv"
    privacy                   = "secret"
    slug                      = "team-pull"
}

```
------------------------------------------------------------
Resource: module.github_teams.github_team.team_push
```
# module.github_teams.github_team.team_push:
resource "github_team" "team_push" {
    create_default_maintainer = false
    etag                      = "W/\"0965481fe2737ba1e6176a0db497b2d0e31ef9673261159806a2c2e1f609aef4\""
    id                        = "8643182"
    members_count             = 0
    name                      = "team-push"
    node_id                   = "T_kwDOCLK5Bc4Ag-Ju"
    privacy                   = "secret"
    slug                      = "team-push"
}

```
------------------------------------------------------------
Resource: module.github_teams.github_team_repository.team_admin_access
```
# module.github_teams.github_team_repository.team_admin_access:
resource "github_team_repository" "team_admin_access" {
    etag       = "W/\"1216a16b8f188933e049ade09e091ee98331410f03212c5a024196e4dcb88cd3\""
    id         = "8643181:ExampleRepository"
    permission = "admin"
    repository = "ExampleRepository"
    team_id    = "8643181"
}

```
------------------------------------------------------------
Resource: module.github_teams.github_team_repository.team_pull_access
```
# module.github_teams.github_team_repository.team_pull_access:
resource "github_team_repository" "team_pull_access" {
    etag       = "W/\"3681d86b23fc9ccf8b04884b873eed8acb6e75358134e5e01463df8cf5bf5344\""
    id         = "8643183:ExampleRepository"
    permission = "pull"
    repository = "ExampleRepository"
    team_id    = "8643183"
}

```
------------------------------------------------------------
Resource: module.github_teams.github_team_repository.team_push_access
```
# module.github_teams.github_team_repository.team_push_access:
resource "github_team_repository" "team_push_access" {
    etag       = "W/\"4ae25e72d7ea6ec1207a5c2824e7105309e9d52714c5d1c948525d80cc390476\""
    id         = "8643182:ExampleRepository"
    permission = "push"
    repository = "ExampleRepository"
    team_id    = "8643182"
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
```
# module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts:
data "yandex_compute_image" "ubuntu-2204-lts" {
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
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_compute_instance.default
```
# module.yandex_cloud.yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2023-09-26T10:44:48Z"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    fqdn                      = "test-hostname.ru-central1.internal"
    hostname                  = "test-hostname"
    id                        = "fhmrdaqnb3vute2c41ua"
    metadata                  = {
        "serial-port-enable" = "1"
        "ssh-keys"           = "ubuntu:"
    }
    name                      = "test-name"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmujrf5v4hn7stsupem"
        disk_id     = "fhmujrf5v4hn7stsupem"
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
        ip_address         = "10.228.0.30"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1b:6a:b5:75"
        nat                = true
        nat_ip_address     = "51.250.82.233"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bcbrjlms08ro7jk3ic"
    }

    placement_policy {
        host_affinity_rules = []
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_vpc_address.vm1
```
# module.yandex_cloud.yandex_vpc_address.vm1:
resource "yandex_vpc_address" "vm1" {
    created_at          = "2023-09-26T10:44:44Z"
    deletion_protection = false
    folder_id           = "b1gkr31c0tt9f3k2cm7b"
    id                  = "e9bq7pnc8qs6tkda2ttv"
    labels              = {}
    name                = "vm1-devops"
    reserved            = true
    used                = false

    external_ipv4_address {
        address = "51.250.82.233"
        zone_id = "ru-central1-a"
    }
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_vpc_network.networkabobus
```
# module.yandex_cloud.yandex_vpc_network.networkabobus:
resource "yandex_vpc_network" "networkabobus" {
    created_at                = "2023-09-26T10:44:44Z"
    default_security_group_id = "enp1ia9sej8c33p5lg0g"
    folder_id                 = "b1gkr31c0tt9f3k2cm7b"
    id                        = "enpb9t6itnhbs58f07kr"
    labels                    = {}
    subnet_ids                = []
}

```
------------------------------------------------------------
Resource: module.yandex_cloud.yandex_vpc_subnet.networkabobus
```
# module.yandex_cloud.yandex_vpc_subnet.networkabobus:
resource "yandex_vpc_subnet" "networkabobus" {
    created_at     = "2023-09-26T10:44:46Z"
    folder_id      = "b1gkr31c0tt9f3k2cm7b"
    id             = "e9bcbrjlms08ro7jk3ic"
    labels         = {}
    network_id     = "enpb9t6itnhbs58f07kr"
    v4_cidr_blocks = [
        "10.228.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}

```
------------------------------------------------------------
# terraform output
```
cplusplus_container_id = "870420f7857cfd4a2820bb730d460cd75933edf433f6ab7408ba3011e67950b8"
github_repo_name = "Elestrias/Devops_repo"
python_container_id = "03616b6ad93cb905f29ca2496196a5bb8f3e943027fc83fbb07606e4cbbca57f"
vm_external_ip = "51.250.82.233"
```


