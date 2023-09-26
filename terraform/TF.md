

yandex:

terraform state list:

```
yandex_compute_instance.my_vm
yandex_vpc_network.my_network
yandex_vpc_subnet.my_subnetwork
```

terraform show

```
# yandex_compute_instance.my_vm:
resource "yandex_compute_instance" "my_vm" {
    created_at                = "2023-09-26T22:02:42Z"
    folder_id                 = "b1gcsukd39lji9up1ohe"
    fqdn                      = "epdi2ggisto571h7jm1o.auto.internal"
    id                        = "epdi2ggisto571h7jm1o"
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdf45mf4qtse1re776m"
        disk_id     = "epdf45mf4qtse1re776m"
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
        ip_address         = "10.129.0.26"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:12:14:21:2e"
        nat                = false
        security_group_ids = []
        subnet_id          = "e2la6hksalj13g2vu6ma"
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
    created_at                = "2023-09-26T22:00:59Z"
    default_security_group_id = "enpus0o4b692jt8qft19"
    folder_id                 = "b1gcsukd39lji9up1ohe"
    id                        = "enpjvfav2l2pom29080g"
    labels                    = {}
    name                      = "terraform-network"
    subnet_ids                = [
        "e2la6hksalj13g2vu6ma",
    ]
}

# yandex_vpc_subnet.my_subnetwork:
resource "yandex_vpc_subnet" "my_subnetwork" {
    created_at     = "2023-09-26T22:01:02Z"
    folder_id      = "b1gcsukd39lji9up1ohe"
    id             = "e2la6hksalj13g2vu6ma"
    labels         = {}
    name           = "terraform-network-ru-central1-b"
    network_id     = "enpjvfav2l2pom29080g"
    v4_cidr_blocks = [
        "10.129.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}


Outputs:

instance_created_at = "2023-09-26T22:02:42Z"
instance_id = "epdi2ggisto571h7jm1o"

```