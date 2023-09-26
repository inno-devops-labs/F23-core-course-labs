## Docker Infrastructure Using Terraform

### Terraform State Information

- Output of `terraform state show`:
```commandline
    # docker_container.container:
resource "docker_container" "container" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python3",
        "app.py",
    ]
    env                                         = []
    hostname                                    = "610d4683bd3d"
    id                                          = "610d4683bd3d68399ebd66f6a6df7d0d49cba2ec695541a2fbe1573bbef8e5ea"
    image                                       = "sha256:a42244c58860684bfe70e956e5257fa6ef11d8c4b9c7809c7b44466e0ef59d20"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my-container"
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
    user                                        = "simpleuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8090
        internal = 8090
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.image:
resource "docker_image" "image" {
    id           = "sha256:a42244c58860684bfe70e956e5257fa6ef11d8c4b9c7809c7b44466e0ef59d20dshamik/dshamik_msk_time:latest"
    image_id     = "sha256:a42244c58860684bfe70e956e5257fa6ef11d8c4b9c7809c7b44466e0ef59d20"
    keep_locally = false
    name         = "dshamik/dshamik_msk_time:latest"
    repo_digest  = "dshamik/dshamik_msk_time@sha256:7259161e6e0cdc6c69fc38a2f2d7d44f9b6d3174175ac1c0c28fd9a707359854"
}

```

- Output of `terraform state list`: 
```commandline
docker_container.container
docker_image.image
```

### Log after applying the changes:

```commandline
docker_image.image: Refreshing state... [id=sha256:a42244c58860684bfe70e956e5257fa6ef11d8c4b9c7809c7b44466e0ef59d20dshamik/dshamik_msk_time:latest]
docker_container.container: Refreshing state... [id=610d4683bd3d68399ebd66f6a6df7d0d49cba2ec695541a2fbe1573bbef8e5ea]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.container must be replaced
-/+ resource "docker_container" "container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python3",
          - "app.py",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "610d4683bd3d" -> (known after apply)
      ~ id                                          = "610d4683bd3d68399ebd66f6a6df7d0d49cba2ec695541a2fbe1573bbef8e5ea" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "my-container" -> "new-container" # forces replacement
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
      - user                                        = "simpleuser" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8090 -> 80 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.container: Destroying... [id=610d4683bd3d68399ebd66f6a6df7d0d49cba2ec695541a2fbe1573bbef8e5ea]
docker_container.container: Destruction complete after 1s
docker_container.container: Creating...
docker_container.container: Creation complete after 0s [id=e76d47299f2cf502d66c07b8a0a55acce71cfd35b73e0cf13d6af2c5815c35a9]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

### Terraform Output

- Output of `terraform output`:
```commandline
container_id = "e76d47299f2cf502d66c07b8a0a55acce71cfd35b73e0cf13d6af2c5815c35a9"
```

## AWS Infrastructure Using Terraform

### Terraform State Information

- Output of `terraform state show`:
```commandline
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:682849823866:instance/i-0d180bd03a049cfb5"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0d180bd03a049cfb5"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    primary_network_interface_id         = "eni-0d1ff137f88c502d9"
    private_dns                          = "ip-172-31-18-47.us-west-2.compute.internal"
    private_ip                           = "172.31.18.47"
    public_dns                           = "ec2-54-245-162-196.us-west-2.compute.amazonaws.com"
    public_ip                            = "54.245.162.196"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0aab25821e22bed79"
    tags                                 = {
        "Name" = "dshamikServer"
    }
    tags_all                             = {
        "Name" = "dshamikServer"
    }
    tenancy                              = "default"
    vpc_security_group_ids               = [
        "sg-0ba46fa84cd286e3e",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 0
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-08549bb2cb1fdf18f"
        volume_size           = 8
        volume_type           = "standard"
    }
}

```

- Output of `terraform state list`: 
```commandline
aws_instance.app_server
```


### Log after applying the changes:

```commandline
aws_instance.app_server: Refreshing state... [id=i-0d180bd03a049cfb5]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy

Terraform will perform the following actions:

  # aws_instance.app_server will be destroyed
  # (because aws_instance.app_server is not in configuration)
  - resource "aws_instance" "app_server" {
      - ami                                  = "ami-830c94e3" -> null
      - arn                                  = "arn:aws:ec2:us-west-2:682849823866:instance/i-0d180bd03a049cfb5" -> null
      - associate_public_ip_address          = true -> null
      - availability_zone                    = "us-west-2a" -> null
      - cpu_core_count                       = 1 -> null
      - cpu_threads_per_core                 = 1 -> null
      - disable_api_termination              = false -> null
      - ebs_optimized                        = false -> null
      - get_password_data                    = false -> null
      - hibernation                          = false -> null
      - id                                   = "i-0d180bd03a049cfb5" -> null
      - instance_initiated_shutdown_behavior = "stop" -> null
      - instance_state                       = "running" -> null
      - instance_type                        = "t2.micro" -> null
      - ipv6_address_count                   = 0 -> null
      - ipv6_addresses                       = [] -> null
      - monitoring                           = false -> null
      - primary_network_interface_id         = "eni-0d1ff137f88c502d9" -> null
      - private_dns                          = "ip-172-31-18-47.us-west-2.compute.internal" -> null
      - private_ip                           = "172.31.18.47" -> null
      - public_dns                           = "ec2-54-245-162-196.us-west-2.compute.amazonaws.com" -> null
      - public_ip                            = "54.245.162.196" -> null
      - secondary_private_ips                = [] -> null
      - security_groups                      = [
          - "default",
        ] -> null
      - source_dest_check                    = true -> null
      - subnet_id                            = "subnet-0aab25821e22bed79" -> null
      - tags                                 = {
          - "Name" = "dshamikServer"
        } -> null
      - tags_all                             = {
          - "Name" = "dshamikServer"
        } -> null
      - tenancy                              = "default" -> null
      - vpc_security_group_ids               = [
          - "sg-0ba46fa84cd286e3e",
        ] -> null

      - capacity_reservation_specification {
          - capacity_reservation_preference = "open" -> null
        }

      - credit_specification {
          - cpu_credits = "standard" -> null
        }

      - enclave_options {
          - enabled = false -> null
        }

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_put_response_hop_limit = 1 -> null
          - http_tokens                 = "optional" -> null
          - instance_metadata_tags      = "disabled" -> null
        }

      - root_block_device {
          - delete_on_termination = true -> null
          - device_name           = "/dev/sda1" -> null
          - encrypted             = false -> null
          - iops                  = 0 -> null
          - tags                  = {} -> null
          - throughput            = 0 -> null
          - volume_id             = "vol-08549bb2cb1fdf18f" -> null
          - volume_size           = 8 -> null
          - volume_type           = "standard" -> null
        }
    }

  # aws_instance.server will be created
  + resource "aws_instance" "server" {
      + ami                                  = "ami-830c94e3"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "dshamikNewServer"
        }
      + tags_all                             = {
          + "Name" = "dshamikNewServer"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + vpc_security_group_ids               = (known after apply)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + public_ip = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.app_server: Destroying... [id=i-0d180bd03a049cfb5]
aws_instance.server: Creating...
aws_instance.app_server: Still destroying... [id=i-0d180bd03a049cfb5, 10s elapsed]
aws_instance.server: Still creating... [10s elapsed]
aws_instance.app_server: Still destroying... [id=i-0d180bd03a049cfb5, 20s elapsed]
aws_instance.server: Still creating... [20s elapsed]
aws_instance.app_server: Destruction complete after 26s
aws_instance.server: Still creating... [30s elapsed]
aws_instance.server: Still creating... [40s elapsed]
aws_instance.server: Creation complete after 47s [id=i-0a8a2ea81d5978751]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

public_ip = "35.93.139.154"
```

### Terraform Output

- Output of `terraform output`:
```commandline
public_ip = "35.93.139.154"
```

## Terraform-Related Best Practices
1. **Modularization**: Organized Terraform code into reusable modules to prevent duplication and promote reusability.
2. **Variable Usage**: Used input variables to customize configurations, making code adaptable and maintainable.
3. **Remote Backend**: Stored Terraform state files remotely for centralized management, locking, and collaboration.
4. **Output Variables**: Expose essential data from Terraform configurations for external use, enhancing flexibility and automation.

