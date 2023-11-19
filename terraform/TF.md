# Lab 4

> **Note that this lab is submitted from the organizational fork of the course repository to illustrate how a repo within organization was managed with Terraform (see Task 2 and bonus task).**

# Task 1
## Using Docker

After deploying the Terraform configuration with `terraform apply`:

```json
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
    hostname                                    = "64e71553bf02"
    id                                          = "64e71553bf0255f500be5f825fbd57dcdbc4baa5e4f5e84d472f0265675cd200"
    image                                       = "sha256:34a9d55b4f47735251bc37f19f21b9e791c02e3f34e8c00e0c6b485b396b8514"
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

```bash
$ terraform state list
docker_container.app_python
docker_image.app_python
```

### Using input variables
Container name and external port number are parametrized with input variables. Using them:

```
terraform apply -var 'container_name=app_python' -var 'external_port=8080'
```

### Terraform output

```bash
$ terraform output
container_id = "fd9251c97aed6623b5991147ffd948060dcad8948fbe7da84c5a77852b4c3bae"
image_id = "sha256:34a9d55b4f47735251bc37f19f21b9e791c02e3f34e8c00e0c6b485b396b8514ar7ch/devops_lab3_app_python:latest"
```

## Using cloud provider (Yandex Cloud)
Access tokens are passed as environment variables.

```bash
$ terraform state list
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```json
$ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-09-26T21:18:13Z"
    folder_id                 = "b1god2svr783gv020cmg"
    fqdn                      = "fhmi4j3npjacmhus7tnt.auto.internal"
    id                        = "fhmi4j3npjacmhus7tnt"
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
        device_name = "fhmcr3kamv4d9uohd98m"
        disk_id     = "fhmcr3kamv4d9uohd98m"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8clogg1kull9084s9o"
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
        subnet_id          = "e9b3l8s62jvadggtv7ff"
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

VM was created and is running:
![VM created and running](https://i.imgur.com/NDd5Kbu.png)

### Terraform output
I have added another output `vm_status` that display, as the name suggests, the status of the VM.

Check terraform outputs:
```
$ terraform output
external_ip_address_vm_1 = "51.250.69.25"
internal_ip_address_vm_1 = "192.168.10.21"
vm_status = "running"
```

# Task 2
This Terraform project creates the repository within the organizaton and configures:
+ Repository name
+ Repository description
+ Visibility settings
+ Default branch
+ Branch protection rule for the default branch

The GitHub token as taken as environment variable.


+ In this task, I would like to have a foundation for the bonus task.
+ Since the bonus task requires us to create teams and it is possible to create teams only within a GitHub Organization, in this task I will also manage repo within the Organization `iu-devops-test-org`.
+ However, since my fork of core-course-labs is on my personal account, I can't perform `terraform import` of it using the organization profile and vice versa.
Thus, I have to make another fork from the `core-course-labs` as an organization repo.
Here we can see that core-course-labs description was updated according to Terraform configuration:
![project description updated by Terraform](https://i.imgur.com/ihmiPXq.png)

Best practices that were employed:

+ Using modules to organize code:
    * The lab is structured in 3 subdirectories for each major task: `docker`, `yacloud`, `github`, each as its own module.
+ Using variables to parameterize the configuration.
+ Using pinned versions of external dependencies (providers).
+ Using output values to extract useful information.
+ Using version control to manage the Terraform code.
+ Using `terraform.tfvars` file to store variables.
    * put `terraform.tfvars` to `.gitignore` to avoid leaking sensitive information.
+ Using `terraform fmt` and `terraform plan` to verify the Terraform code.

# Bonus Task
+ Here we can see that the repository is created within the organization `iu-devops-test-org` and the teams `team-alpha`, `team-bravo`, `team-devops` have access to it. 

![Teams' access rules added to the repository via Terraform](https://i.imgur.com/4getnBn.png)