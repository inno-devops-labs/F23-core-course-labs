## DOCKER

<details> <summary> Spoiler </summary> 

```
➜  docker git:(lab4) ✗ tf state list
docker_container.app_python
docker_image.app_python
```

```
➜  docker git:(lab4) ✗ tf state show docker_image.app_python
# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03wiirtex/python_time_service:0.2.0"
    image_id     = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03"
    keep_locally = false
    name         = "wiirtex/python_time_service:0.2.0"
    repo_digest  = "wiirtex/python_time_service@sha256:7ac8ee903951245fe7fb880a87868d0c28eea0a2e8325124dcc28631ec24fd9f"
}

➜  docker git:(lab4) ✗ tf state show docker_container.app_python
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "/bin/sh",
        "-c",
        ". ~/opt/venv/bin/activate && exec python app_python/src/main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "e49ad91ba5b3"
    id                                          = "e49ad91ba5b3706fb074a90ab9ac1e796d175245f0c968bd75a037ab34395649"
    image                                       = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03"
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
    user                                        = "python_runner"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/python_runner/python/src/app"

    ports {
        external = 7098
        internal = 7098
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```
➜  docker git:(lab4) ✗ tf output
container_id = "e49ad91ba5b3706fb074a90ab9ac1e796d175245f0c968bd75a037ab34395649"
image_id = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03wiirtex/python_time_service:0.2.0"
```

</details>


## YANDEX


<details> <summary> Spoiler </summary> 


```
➜  yandex git:(lab4) ✗ tf state list                     
yandex_compute_instance.my_vm
yandex_vpc_network.my_network
yandex_vpc_subnet.my_subnetwork
```

```
➜  yandex git:(lab4) ✗ tf state show yandex_compute_instance.my_vm
# yandex_compute_instance.my_vm:
resource "yandex_compute_instance" "my_vm" {
    created_at                = "2023-09-26T20:22:03Z"
    folder_id                 = "b1g5pgfas4utv31ktp1u"
    fqdn                      = "epdqiqj5qfsipioq3gar.auto.internal"
    id                        = "epdqiqj5qfsipioq3gar"
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epd9k5r82a7admmon495"
        disk_id     = "epd9k5r82a7admmon495"
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
        mac_address        = "d0:0d:1a:96:a6:5d"
        nat                = false
        security_group_ids = []
        subnet_id          = "e2lvbv14cnm43upaso1f"
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
```

```
➜  yandex git:(lab4) ✗ tf state show yandex_vpc_network.my_network
# yandex_vpc_network.my_network:
resource "yandex_vpc_network" "my_network" {
    created_at                = "2023-09-26T20:21:59Z"
    default_security_group_id = "enp82meje01p97md8a4s"
    folder_id                 = "b1g5pgfas4utv31ktp1u"
    id                        = "enpqgmio59rc3ive2kl1"
    labels                    = {}
    name                      = "terraform-network"
    subnet_ids                = []
}
```

```
➜  yandex git:(lab4) ✗ tf state show yandex_vpc_subnet.my_subnetwork
# yandex_vpc_subnet.my_subnetwork:
resource "yandex_vpc_subnet" "my_subnetwork" {
    created_at     = "2023-09-26T20:22:01Z"
    folder_id      = "b1g5pgfas4utv31ktp1u"
    id             = "e2lvbv14cnm43upaso1f"
    labels         = {}
    name           = "terraform-network-ru-central1-b"
    network_id     = "enpqgmio59rc3ive2kl1"
    v4_cidr_blocks = [
        "10.129.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}
```

```
➜  docker git:(lab4) ✗ tf output
instance_created_at = "2023-09-26T20:22:03Z"
instance_id = "epdqiqj5qfsipioq3gar"
```

</details>
