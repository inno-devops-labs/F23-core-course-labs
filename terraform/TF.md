# Task 1
## Docker

### `terraform apply`

docker_image.app_python_image: Refreshing state... [id=sha256:f97842a3112551ec5811de994e56f62335be07bc211638979e242b498d5849c1annadluzhinskaya/python-moscow-time:latest]
docker_container.app_python_container: Refreshing state... [id=0eed0888ce6ef33a08422c7052826653aa6b3d6fbf3202335ee6a826d575a66a]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python_container must be replaced
-/+ resource "docker_container" "app_python_container" {
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
      ~ hostname                                    = "0eed0888ce6e" -> (known after apply)
      ~ id                                          = "0eed0888ce6ef33a08422c7052826653aa6b3d6fbf3202335ee6a826d575a66a" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "my_container" -> "my_container_2" # forces replacement
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
      - user                                        = "rootlessuser" -> null
      - working_dir                                 = "/app_python" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8000 -> 80 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python_container: Destroying... [id=0eed0888ce6ef33a08422c7052826653aa6b3d6fbf3202335ee6a826d575a66a]
docker_container.app_python_container: Destruction complete after 1s
docker_container.app_python_container: Creating...
docker_container.app_python_container: Creation complete after 0s [id=f2799c26eb81eea7bd24b61002985fbcfe74232fcc2e0734fa9bc623492285ff]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

### `terraform state show`

docker_container.app_python_container:
resource "docker_container" "app_python_container" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python3",
        "app.py",
    ]
    env                                         = []
    hostname                                    = "0eed0888ce6e"
    id                                          = "0eed0888ce6ef33a08422c7052826653aa6b3d6fbf3202335ee6a826d575a66a"
    image                                       = "sha256:f97842a3112551ec5811de994e56f62335be07bc211638979e242b498d5849c1"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my_container"
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
    user                                        = "rootlessuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

docker_image.app_python_image:
resource "docker_image" "app_python_image" {
    id           = "sha256:f97842a3112551ec5811de994e56f62335be07bc211638979e242b498d5849c1annadluzhinskaya/python-moscow-time:latest"
    image_id     = "sha256:f97842a3112551ec5811de994e56f62335be07bc211638979e242b498d5849c1"
    keep_locally = false
    name         = "annadluzhinskaya/python-moscow-time:latest"
    repo_digest  = "annadluzhinskaya/python-moscow-time@sha256:bfd132577214faaed3a559eda42806ea65044a83168858f33ab3a2e39d7f525f"
}


### `terraform state list`

docker_container.app_python_container
docker_image.app_python_image


### `terraform output`

container_id = "0600fa4c16c2c201b302b1d6400936b021e63ec2dd9d7d0afd67517f3c5c0e52"

## AWS

### `terraform apply`

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.app_server will be created
  + resource "aws_instance" "app_server" {
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
          + "Name" = "annadlu_server"
        }
      + tags_all                             = {
          + "Name" = "annadlu_server"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + vpc_security_group_ids               = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.app_server: Creating...
aws_instance.app_server: Still creating... [10s elapsed]
aws_instance.app_server: Still creating... [20s elapsed]
aws_instance.app_server: Still creating... [30s elapsed]
aws_instance.app_server: Still creating... [40s elapsed]
aws_instance.app_server: Still creating... [50s elapsed]
aws_instance.app_server: Still creating... [1m0s elapsed]
aws_instance.app_server: Creation complete after 1m7s [id=i-04d913ecfb48d2b6f]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

### `terraform state show`

aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:682849823866:instance/i-04d913ecfb48d2b6f"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-04d913ecfb48d2b6f"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    primary_network_interface_id         = "eni-0479dff1c35ad1cc6"
    private_dns                          = "ip-172-31-19-152.us-west-2.compute.internal"
    private_ip                           = "172.31.19.152"
    public_dns                           = "ec2-18-236-65-48.us-west-2.compute.amazonaws.com"
    public_ip                            = "18.236.65.48"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0aab25821e22bed79"
    tags                                 = {
        "Name" = "annadlu_server"
    }
    tags_all                             = {
        "Name" = "annadlu_server"
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
        volume_id             = "vol-0e17fb35591daea2d"
        volume_size           = 8
        volume_type           = "standard"
    }
}


### `terraform state list`

aws_instance.app_server

### `terraform output`

public_ip = "18.236.65.48"


# Task 2
## Terraform best practices

- Avoid variables hard-coding
- Always format and validate
- Implement a Secrets Management Strategy
- Include outputs

# Bonus task

https://github.com/DevOps-AnnaDluzhinskaya
