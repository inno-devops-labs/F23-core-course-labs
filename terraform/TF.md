# Terraform

Shakirov Azamat B20-CS

a.shakirov@innopolis.university



---

### Docker Terraform

Output of `terraform state list`:

```bash
docker_container.nginx
docker_image.nginx
```

Output of `terraform state show docker_container.nginx` :

```bash
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
    hostname                                    = "1b38ab6e384c"
    id                                          = "1b38ab6e384c369ee98d8f6ec2d582d46fb7926d6d3392e8b370b54a5281fa66"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
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
```

Output of `terraform state show docker_image.nginx`:

```bash
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

Output of `terraform output `

```bash
container_id = "a5bc5d3bdfa732cbde7c6c2d1e440249926f27f4001817e3aa62f320ac83f412"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
```



### YandexCloud Terraform

Output of `terraform state list`:

```bash
yandex_compute_instance.vm-1
yandex_compute_instance.vm-2
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

Output of `terraform state show yandex_vpc_subnet.subnet-1` :

```bash
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-09-27T01:07:46Z"
    folder_id      = "b1g036972ff6lkdkh1t2"
    id             = "e9bo8mbnferolmv9ghth"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp61a53sv0ij2lbg9rg"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

Output of `terraform state show yandex_vpc_network.network-1`:

```bash
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2023-09-27T01:07:44Z"
    default_security_group_id = "enpm0v3t1khdjtsp5nbp"
    folder_id                 = "b1g036972ff6lkdkh1t2"
    id                        = "enp61a53sv0ij2lbg9rg"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}
```

Output of `terraform output `

```bash
external_ip_address_vm_1 = "51.250.73.24"
external_ip_address_vm_2 = "51.250.10.192"
internal_ip_address_vm_1 = "192.168.10.7"
internal_ip_address_vm_2 = "192.168.10.14"
```



