# Terraform

---
Inside the `./teraform` directory you can find three directories for each of the lab tasks:
1. `/docker`
2. `/yandex`
3. `/github`
---

## Best practices applied
* Use `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf` instead of big `main.tf`
* Use `terraform validate`
* Use `terraform fmt`
* Include description on all variables even if you think it is obvious
* Keep secrets in environment variables instead of putting them in code

## Docker
* Output of `terraform state list`
    ```
    docker_container.app_python
    docker_image.app_python
    ```
* Output of `terraform show`
    ```
    # docker_container.app_python:
    resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
    "python3",
    "src/app.py",
    ]
    env                                         = []
    hostname                                    = "26bfa204cfe1"
    id                                          = "26bfa204cfe1e34f458a7eb3f015f546bce9334ba7f53c21cd1b1080d4ca68b8"
    image                                       = "sha256:5680ac2126b8a319b20b842547ba0e1d84a1be226cf5547805c284b3603e4a6b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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
    user                                        = "user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

        ports {
            external = 8080
            internal = 8080
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }

    # docker_image.app_python:
    resource "docker_image" "app_python" {
    id           = "sha256:5680ac2126b8a319b20b842547ba0e1d84a1be226cf5547805c284b3603e4a6biskanred/app_python:1.0.0"
    image_id     = "sha256:5680ac2126b8a319b20b842547ba0e1d84a1be226cf5547805c284b3603e4a6b"
    keep_locally = false
    name         = "iskanred/app_python:1.0.0"
    repo_digest  = "iskanred/app_python@sha256:25f583ff0989187c800aca68116472594c740d8534ea0d47fc3c1abd9ff3d6ae"
    }


    Outputs:

    container_id = "26bfa204cfe1e34f458a7eb3f015f546bce9334ba7f53c21cd1b1080d4ca68b8"
    image_id = "sha256:5680ac2126b8a319b20b842547ba0e1d84a1be226cf5547805c284b3603e4a6biskanred/app_python:1.0.0"
    ```
* Output of `terraform output`
    ```
    container_id = "26bfa204cfe1e34f458a7eb3f015f546bce9334ba7f53c21cd1b1080d4ca68b8"
    image_id = "sha256:5680ac2126b8a319b20b842547ba0e1d84a1be226cf5547805c284b3603e4a6biskanred/app_python:1.0.0"
    ```

## Yandex Cloud

* Output of `terraform state list`
    ```
    yandex_compute_instance.my_vm
    yandex_vpc_network.my_network
    yandex_vpc_subnet.my_subnetwork
    ```
* Output of `terraform show`
    ```
    # yandex_compute_instance.my_vm:
    resource "yandex_compute_instance" "my_vm" {
    created_at                = "2023-09-25T20:54:15Z"
    folder_id                 = "b1g51f9qr8db97oierom"
    fqdn                      = "epdpoln8vi2aflud6uul.auto.internal"
    id                        = "epdpoln8vi2aflud6uul"
    labels                    = {}
    metadata                  = {}
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

        boot_disk {
            auto_delete = true
            device_name = "epd4q35tsj22gtqmkkl1"
            disk_id     = "epd4q35tsj22gtqmkkl1"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd8dfofgv8k45mqv25nq"
                name       = "ubuntu-20-04-lts-v20230918"
                size       = 5
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
            ip_address         = "10.129.0.30"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:19:c5:6e:8f"
            nat                = false
            security_group_ids = []
            subnet_id          = "e2lngbk1fpde9956c0q8"
        }

        placement_policy {
            host_affinity_rules = []
        }

        resources {
            core_fraction = 20
            cores         = 2
            gpus          = 0
            memory        = 1
        }

        scheduling_policy {
            preemptible = false
        }
    }

    # yandex_vpc_network.my_network:
    resource "yandex_vpc_network" "my_network" {
    created_at                = "2023-09-25T20:53:10Z"
    default_security_group_id = "enpinabv31g7f3gj3hbs"
    folder_id                 = "b1g51f9qr8db97oierom"
    id                        = "enpjldbilvhn6mk98hpq"
    labels                    = {}
    name                      = "terraform-network"
    subnet_ids                = [
    "e2lngbk1fpde9956c0q8",
    ]
    }

    # yandex_vpc_subnet.my_subnetwork:
    resource "yandex_vpc_subnet" "my_subnetwork" {
    created_at     = "2023-09-25T20:53:12Z"
    folder_id      = "b1g51f9qr8db97oierom"
    id             = "e2lngbk1fpde9956c0q8"
    labels         = {}
    name           = "terraform-network-ru-central1-b"
    network_id     = "enpjldbilvhn6mk98hpq"
    v4_cidr_blocks = [
    "10.129.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
    }


    Outputs:

    instance_created_at = "2023-09-25T20:54:15Z"
    instance_id = "epdpoln8vi2aflud6uul"
    ```
* Output of `terraform output`
    ```
    instance_created_at = "2023-09-25T20:54:15Z"
    instance_id = "epdpoln8vi2aflud6uul"
    ```

## GitHub

* Output of `terraform state list`
    ```
    
    ```
* Output of `terraform show`
    ```
    
    ```
* Output of `terraform output`
    ```
    
    ```


