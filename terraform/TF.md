# Infrastructure as Code Lab

> All the necessary files for each task are distributed to required folders. There is a main.tf, variables.tf and outputs.tf. Below, there is a result from running required commands after initialising, planning and applying terraform.

## Best Practices Applied : 

> In this module I describe all the best practices I used throughout completing the task. 

 1. *Modularization* : I have organized infrastructure code into separate modules for Docker, Yandex Cloud, GitHub, and GitHub teams. This promotes reusability and maintainability.

 2. *Module Descriptions* : Each module has a meaningful and concise description (e.g., module "nginx_server"). This helps in understanding the purpose of each module.

 3. *Variable Usage* : I'm using variables like var.github_token to make my code more flexible and avoid hardcoding values directly into configuration.

 4. *Source Paths* : I am specifying source paths for each module using relative paths (e.g., source = "./docker").

 5. *Explicit Dependency* : There's an explicit dependency relationship between modules. For example, the github-teams module depends on the github module.

 6. *Descriptive Names* : I'm using descriptive names for resources, like container_name = "my-nginx-app". This makes it easier to understand the purpose of each resource.

 8. *Consistent Naming Convention* : I tried to keep my naming conventions consistent. 

 9. *Provider Configuration* : I configure my Terraform providers properly, including authentication and region settings.

## Task 1: Docker Infrastructure Using Terraform 

#### terraform state list

```sh
terraform state list
```

```
docker_container.nginx
docker_image.nginx
```

#### terraform state show 

```sh
terraform state show docker_container.nginx

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
    hostname                                    = "b98f7cec04c9"
    id                                          = "b98f7cec04c9fef0005afa52be4005e3e2d6db9267d0e4b7fa82c2d9f9aa8292"
    image                                       = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my-nginx-app"
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

```sh
terraform state show docker_image.nginx

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73nginx:latest"
    image_id     = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

#### log with the applied changes

```sh
❯ terraform apply
var.container_name
  Enter a value: random-container

var.image_name
  Enter a value: nginx:latest

docker_image.nginx: Refreshing state... [id=sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73nginx:latest]
docker_container.nginx: Refreshing state... [id=0b8770d6fa197cbd5d43f01a4d19ad3165d74a9908c92e9db41a3c9dd5613e2f]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

  # docker_container.nginx has been deleted
  - resource "docker_container" "nginx" {
      - id                                          = "0b8770d6fa197cbd5d43f01a4d19ad3165d74a9908c92e9db41a3c9dd5613e2f" -> null
        name                                        = "random-container-name"
        # (16 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following plan may include actions to undo or respond to these changes.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
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
      + image                                       = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "random-container"
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
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=8afb3b8aa35610fa13dadd8d09a22cbb889b6650e32ac9100c6cec7c7c2d4544]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

container_id = "8afb3b8aa35610fa13dadd8d09a22cbb889b6650e32ac9100c6cec7c7c2d4544"
image_id = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73nginx:latest"
```

#### terraform output 

```
❯ terraform output
container_id = "8afb3b8aa35610fa13dadd8d09a22cbb889b6650e32ac9100c6cec7c7c2d4544"
image_id = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73nginx:latest"
```

## Task 2: Yandex Cloud Infrastructure Using Terraform 

#### terraform state list

```sh
❯ terraform state list
yandex_compute_instance.vm-1
yandex_compute_instance.vm-2
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```
#### terraform state show 

```sh
❯ terraform state show yandex_vpc_network.network-1
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2023-09-27T03:08:02Z"
    default_security_group_id = "enpgp3p6f2e4gavut1vf"
    folder_id                 = "b1g1aqrohbot4fl3e1vb"
    id                        = "enp7ckctka4ce3i3lnlh"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}

❯ terraform state show yandex_vpc_subnet.subnet-1
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-09-27T03:08:05Z"
    folder_id      = "b1g1aqrohbot4fl3e1vb"
    id             = "e9b2qbs7k3kul1bo22qo"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp7ckctka4ce3i3lnlh"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}

❯ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-09-27T03:08:08Z"
    folder_id                 = "b1g1aqrohbot4fl3e1vb"
    fqdn                      = "fhm6n20l4geif7u8e72r.auto.internal"
    id                        = "fhm6n20l4geif7u8e72r"
    name                      = "my-vm-1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm39e712ct1njgagot2"
        disk_id     = "fhm39e712ct1njgagot2"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd82sqrj4uk9j7vlki3q"
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
        ip_address         = "192.168.10.17"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:6b:88:15:24"
        nat                = true
        nat_ip_address     = "158.160.109.49"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b2qbs7k3kul1bo22qo"
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

#### log with the applied changes

```sh
❯ terraform apply

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
      + name                      = "my-vm-1"
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
              + image_id    = "fd82sqrj4uk9j7vlki3q"
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

  # yandex_compute_instance.vm-2 will be created
  + resource "yandex_compute_instance" "vm-2" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + name                      = "my-vm-2"
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
              + image_id    = "fd82sqrj4uk9j7vlki3q"
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
          + cores         = 4
          + memory        = 4
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

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + external_ip_address_vm_2 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_2 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Creation complete after 8s [id=enp7ckctka4ce3i3lnlh]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9b2qbs7k3kul1bo22qo]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-2: Creating...
yandex_compute_instance.vm-2: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-2: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-2: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-2: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-2: Creation complete after 40s [id=fhmn7k6epn41im89c8tp]
yandex_compute_instance.vm-1: Creation complete after 41s [id=fhm6n20l4geif7u8e72r]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "158.160.109.49"
external_ip_address_vm_2 = "158.160.115.243"
internal_ip_address_vm_1 = "192.168.10.17"
internal_ip_address_vm_2 = "192.168.10.22"
```

#### terraform output 

```sh
❯ terraform output
external_ip_address_vm_1 = "158.160.109.49"
external_ip_address_vm_2 = "158.160.115.243"
internal_ip_address_vm_1 = "192.168.10.17"
internal_ip_address_vm_2 = "192.168.10.22"
```

## Task 3: Terraform for GitHub
I imported existing repository, using *imports.tf* . 
And also created github infrastructure, the results are visible on the github, here is a link to the created repository - [My Core Course Labs ](https://github.com/m4k4rich/my-core-course-labs) 

## Bonus Task : Adding Teams 

Using terraform I created an organization called - 
*InnoDevopsCourseOrg*, added several teams to the repository with different levels of access. There is a team of admins, a team of people why are able to push and the team of people who are able to pull! Here is a link to the repo, where you can see all the teams - [gh-teams-terraform](https://github.com/InnoDevopsCourseOrg/gh-teams-terraform)