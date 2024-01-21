#Docker

##terraform show:

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
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "b4292dbe7a72"
    id                                          = "b4292dbe7a72f2f4e9ae7073c3c605eb26abba21ad443e01c1d0705561a43754"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "lab4-container"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

## terraform state list:

```
docker_container.nginx
docker_image.nginx
```

## Documented changes(change of port to 5000) in terraform show:

```
ports {
    external = 5000
    internal = 80
    ip       = "0.0.0.0"
    protocol = "tcp"
}
```

## terraform output

```
container_id = "965a6e81fa7af853c5d7b40485e67f6272a0c3740effbb10f413f9c0c5635b1e"
```

# Yandex Cloud

## terraform show
```
 # yandex_compute_instance.docker-vm
  + resource "yandex_compute_instance" "docker-vm" {
      + created_at                = "2023-26-09T20:07:11Z"
      + folder_id                 = "b1gjbm51n00a8fsff0qm"
      + fqdn                      = "fhmjnnd7umoti4f542g8.ru-central1.internal"
      + hostname                  = irina
      + id                        = "fhmjnnd7umoti4f542g8"
      + metadata                  = {
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: irina
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh-authorized-keys:
                      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMXyE5d4KHZWUcjW7U1QKyruhenRGwJcsDGbMTCGD1zx user@DESKTOP-J0PVR6L
            EOT
        }
      + name                      = "vm-1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v3"
      + service_account_id        = "ajetl4pbdhvboqrcthd1"
      + status                    = "running"
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = "fhm01ivgvv7m97o3k88o"
          + disk_id     = "fhm01ivgvv7m97o3k88o"
          + mode        = "READ_WRITE"

          + initialize_params {
              + block_size  = 4096
              + image_id    = "fd8cuq254pag9t4pkasb"
              + size        = 5
              + type        = "network-hdd"
            }
        }

      + network_interface {
          + index              = 0
          + ip_address         = "192.168.55.17"
          + ipv4               = true
          + ipv6               = false
          + mac_address        = "d0:0d:37:05:16:10"
          + nat                = true
          + nat_ip_address     = "51.250.79.172"
          + nat_ip_version     = "IPV4"
          + security_group_ids = ["default-sg-enp30lgp9vp771vt6n6s"]
          + subnet_id          = "e9br6fi4f9sjhvbrd8oh"
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_container_registry.my-registry
  + resource "yandex_container_registry" "my-registry" {
      + created_at = "2023-26-09T20:07:11Z"
      + folder_id  = "b1gjbm51n00a8fsff0qm"
      + id         = "crp3voqf5cfcseqdahc2"
      + labels     = {
          + "my-label" = "my-label-value"
        }
      + name       = "time-app"
      + status     = "running"
    }

  # yandex_iam_service_account.registry-sa
  + resource "yandex_iam_service_account" "registry-sa" {
      + created_at = "2023-26-09T20:07:11Z"
      + folder_id  = "b1gjbm51n00a8fsff0qm"
      + id         = "ajetl4pbdhvboqrcthd1"
      + name       = "time-app-acc"
    }

  # yandex_resourcemanager_folder_iam_member.registry-sa-role-images-puller
  + resource "yandex_resourcemanager_folder_iam_member" "registry-sa-role-images-puller" {
      + folder_id = "b1gjbm51n00a8fsff0qm"
      + id        = "ajetl4pbdhvboqrcthd1"
      + member    = "serviceAccount:ajetl4pbdhvboqrcthd1"
      + role      = "container-registry.images.puller"
    }

  # yandex_vpc_network.docker-vm-network
  + resource "yandex_vpc_network" "docker-vm-network" {
      + created_at                = "2023-26-09T20:07:11Z"
      + folder_id                 = "b1gjbm51n00a8fsff0qm"
      + id                        = "enrstfvcdu11u09kke1g"
      + labels                    = {}
      + name                      = "default"
      + subnet_ids                = []
    }

  # yandex_vpc_subnet.docker-vm-network-subnet-a
  + resource "yandex_vpc_subnet" "docker-vm-network-subnet-a" {
      + created_at     = "2023-26-09T20:07:12Z"
      + folder_id      = "b1gjbm51n00a8fsff0qm"
      + id             = "ef3hqwadlm223sa3as7i"
      + labels         = {}
      + name           = "default-ru-central1-a"
      + network_id     = "enrstfvcdu11u09kke1g"
      + v4_cidr_blocks = [
          + "192.168.1.0/24",
        ]
      + v6_cidr_blocks = []
      + zone           = "ru-central1-a"
    }
```

## terraform state list:

```
yandex_compute_instance.docker-vm
yandex_container_registry.my-registry
yandex_iam_service_account.registry-sa
yandex_resourcemanager_folder_iam_member.registry-sa-role-images-puller
yandex_vpc_network.docker-vm-network
yandex_vpc_subnet.docker-vm-network-subnet-a
```

## terraform output

```
service_account_id_on_vm = "ajetl4pbdhvboqrcthd1"
```
