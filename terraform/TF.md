# Terraform

Current terraform configuration creates **Yandex VM** and deploy **Nginx container** on it

```bash
$> terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + metadata                  = {
          + "user-data" = <<-EOT
                #!/bin/bash
                apt-get update
                apt-get install -y docker.io
                systemctl start docker
                systemctl enable docker
                docker run --name nginx-container -p 80:80 -d nginx
            EOT
        }
      + name                      = "terraform1"
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
              + image_id    = "fd82nvvtllmimo92uoul"
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
          + memory        = 2
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
```
<br>

## State information

Resources:
```bash
$> terraform state list
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```
<br>

VM State:
```bash
$> terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-12-11T19:35:30Z"
    folder_id                 = "b1giv9grvevdcjkngmkk"
    fqdn                      = "fhm82uv1vd9cuo16jsco.auto.internal"
    id                        = "fhm82uv1vd9cuo16jsco"
    labels                    = {}
    metadata                  = {
        "user-data" = <<-EOT
            #!/bin/bash
            apt-get update
            apt-get install -y docker.io
            systemctl start docker
            systemctl enable docker
            docker run --name nginx-container -p 80:80 -d nginx
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmt297a4jj2rj7ttaf8"
        disk_id     = "fhmt297a4jj2rj7ttaf8"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd82nvvtllmimo92uoul"
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
        ip_address         = "192.168.10.3"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:81:7b:e1:fb"
        nat                = true
        nat_ip_address     = "62.84.119.172"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b8l4mn59cvhomqne0u"
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

## Container Name Variable

To set container name I use `nginx_container_name` variable in `variables.tf`

```bash
variables.tf:

<other variables>

variable "nginx_container_name" {
  description = "The name of the Nginx Docker container"
  type        = string
  default     = "nginx-container"
}
```
<br>

Variable usage:
```bash
main.tf:

<other code>

metadata = {
    user-data = <<-EOT
                #!/bin/bash
                apt-get update
                apt-get install -y docker.io
                systemctl start docker
                systemctl enable docker
                docker run --name ${var.nginx_container_name} -p 80:80 -d nginx
                EOT
}

<other code>
```

## Terraform Output

```bash
$> terraform output
external_ip_address_vm_1 = "51.250.77.94"
internal_ip_address_vm_1 = "192.168.10.33"
```