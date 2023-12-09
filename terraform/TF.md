# Lab 4

# Task 1
## Docker

Upon executing the terraform apply command to deploy the Terraform configuration:

```
$ terraform state show docker_container.app_python
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python3",
        "main.py",
        "0.0.0.0",
        "80",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "64e7153b4f02"
    id                                          = "64e71553bf0255f500be5f25fbd57dc4dbc4aa5e4f5e484d472f025675cd200"
    image                                       = "sha256:434a955b4f47734521bc3f19f21b9e7491c2e3f34e8c00e0c46b485b396b8514"
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
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/proj/app"

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```
$ terraform state list
docker_container.app_python
docker_image.app_python
```

### Using input variables
I've parameterized the container name and external port number by incorporating input variables. 

```
terraform apply -var 'container_name=app_python' -var 'external_port=8080'
```

### Terraform output

```
$ terraform output
container_id = "fd9251c97aed6623b5991147ffd948060dcad8948fbe7da84c5a77852b4c3bae"
image_id = "sha256:34a9d55b4f47735251bc37f19f21b9e791c02e3f34e8c00e0c6b485b396b8514beleet/devops_lab3_app_python:latest"
```

## Using cloud provider (Yandex Cloud)
Access tokens are passed as environment variables.

```
$ terraform state list
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```
$ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-09-26T21:18:13Z"
    folder_id                 = "b1goh2svr783gv020cmg"
    fqdn                      = "fhmf4j3npjacmhus7tnt.auto.internal"
    id                        = "fhmf4j3npjacmhus7tnt"
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmcr3famv4d9uohd68m"
        disk_id     = "fhmcr3famv4d9uohd68m"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8clo6g1kull9d84s9o"
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
        ip_address         = "192.168.10.21"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:12:24:c7:7c"
        nat                = true
        nat_ip_address     = "51.250.69.25"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b3l8e62jva6ggtvhff"
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

VM was created and is running

### Terraform output
I have added another output `vm_status` that display, as the name suggests, the status of the VM.

Check terraform outputs:
```
$ terraform output
external_ip_address_vm_1 = "51.250.69.25"
internal_ip_address_vm_1 = "192.168.10.21"
vm_status = "running"
```

In this Terraform project, we establish a repository within the organization, configuring essential aspects such as the repository name, description, visibility settings, default branch, and a branch protection rule for the default branch. The GitHub token is obtained from an environment variable.

To lay the groundwork for the upcoming bonus task, we extend our management to repositories within the organization 'iu-devops-test-org.' Since creating teams is restricted to GitHub Organizations, this task involves handling repositories within this organization. However, due to the limitation of performing terraform import between a personal account fork and an organization profile, a new fork of 'core-course-labs' is created as an organizational repository.

The Terraform configuration updates the 'core-course-labs' description to align with best practices:

Code organization through modules: The lab is divided into three modules ('docker,' 'yacloud,' 'github') within separate subdirectories, each addressing a major task.
Parameterization through variables.
Use of pinned versions for external dependencies (providers).
Extraction of valuable information through output values.
Version control to manage Terraform code.
Utilization of 'terraform.tfvars' to store variables, with proper inclusion in '.gitignore' to prevent sensitive information leaks.
Verification of Terraform code through 'terraform fmt' and 'terraform plan.'