# Terraform

## Docker tutorial

### terraform show

```hcl
# module.app_python.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "gunicorn",
        "-k",
        "uvicorn.workers.UvicornWorker",
        "-w",
        "4",
        "--bind",
        "0.0.0.0:8080",
        "app:app",
    ]
    env                                         = []
    hostname                                    = "e135970ecc65"
    id                                          = "e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18"
    image                                       = "sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7"
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
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.dvechtomova_image:
resource "docker_image" "dvechtomova_image" {
    id           = "sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7dvechtomova/python_app"
    image_id     = "sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7"
    keep_locally = false
    name         = "dvechtomova/python_app"
    repo_digest  = "dvechtomova/python_app@sha256:75042cddcec60f5fd5572c26d5a957dc092afaaa75a32e09e4b7eb1cefa5f4fe"
}
# module.app_rust.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/app/app_rust",
    ]
    env                                         = []
    hostname                                    = "0d5fc62dbff4"
    id                                          = "0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb"
    image                                       = "sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_rust"
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
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_rust.docker_image.dvechtomova_image:
resource "docker_image" "dvechtomova_image" {
    id           = "sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1dvechtomova/rust_app"
    image_id     = "sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1"
    keep_locally = false
    name         = "dvechtomova/rust_app"
    repo_digest  = "dvechtomova/rust_app@sha256:293fb19ebeb36641772fb790b70d1e17b1a91e402604ab4b1c63b268fae6ea7a"
}


Outputs:

python_container_id = "e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18"
rust_container_id = "0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb"
```

### terraform state list

```hcl
module.app_python.docker_container.python_app
module.app_python.docker_image.dvechtomova_image
module.app_rust.docker_container.python_app
module.app_rust.docker_image.dvechtomova_image
```

## Docker tutorial - container name change

### terraform plan

```hcl
module.app_rust.docker_image.dvechtomova_image: Refreshing state... [id=sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1dvechtomova/rust_app]
module.app_python.docker_image.dvechtomova_image: Refreshing state... [id=sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7dvechtomova/python_app]
module.app_rust.docker_container.python_app: Refreshing state... [id=0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb]
module.app_python.docker_container.python_app: Refreshing state... [id=e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # module.app_python.docker_container.python_app must be replaced
-/+ resource "docker_container" "python_app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "gunicorn",
          - "-k",
          - "uvicorn.workers.UvicornWorker",
          - "-w",
          - "4",
          - "--bind",
          - "0.0.0.0:8080",
          - "app:app",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "e135970ecc65" -> (known after apply)
      ~ id                                          = "e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "app_python" -> "python_app" # forces replacement
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.3"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:03"
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
      - user                                        = "user" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

  # module.app_rust.docker_container.python_app must be replaced
-/+ resource "docker_container" "python_app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/app/app_rust",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "0d5fc62dbff4" -> (known after apply)
      ~ id                                          = "0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "app_rust" -> "rust_app" # forces replacement
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
      - user                                        = "user" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ python_container_id = "e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18" -> (known after apply)
  ~ rust_container_id   = "0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb" -> (known after apply)
```

### terraform apply

```hcl
module.app_rust.docker_image.dvechtomova_image: Refreshing state... [id=sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1dvechtomova/rust_app]
module.app_python.docker_image.dvechtomova_image: Refreshing state... [id=sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7dvechtomova/python_app]
module.app_rust.docker_container.python_app: Refreshing state... [id=0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb]
module.app_python.docker_container.python_app: Refreshing state... [id=e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # module.app_python.docker_container.python_app must be replaced
-/+ resource "docker_container" "python_app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "gunicorn",
          - "-k",
          - "uvicorn.workers.UvicornWorker",
          - "-w",
          - "4",
          - "--bind",
          - "0.0.0.0:8080",
          - "app:app",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "e135970ecc65" -> (known after apply)
      ~ id                                          = "e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "app_python" -> "python_app" # forces replacement
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.3"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:03"
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
      - user                                        = "user" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

  # module.app_rust.docker_container.python_app must be replaced
-/+ resource "docker_container" "python_app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/app/app_rust",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "0d5fc62dbff4" -> (known after apply)
      ~ id                                          = "0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "app_rust" -> "rust_app" # forces replacement
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
      - user                                        = "user" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ python_container_id = "e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18" -> (known after apply)
  ~ rust_container_id   = "0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.app_python.docker_container.python_app: Destroying... [id=e135970ecc658e356c208f9415dc672a5ba4a0622fcf8522ccd437fe4fcdcd18]
module.app_rust.docker_container.python_app: Destroying... [id=0d5fc62dbff44da11d0da057c390c575dbc8239c05f3fb274133ad3b42971dfb]
module.app_rust.docker_container.python_app: Destruction complete after 1s
module.app_rust.docker_container.python_app: Creating...
module.app_python.docker_container.python_app: Destruction complete after 1s
module.app_python.docker_container.python_app: Creating...
module.app_rust.docker_container.python_app: Creation complete after 1s [id=5ab81165c3f295bbac41498a3e5bcc0a20937d62b8f0dc44cad1500994a7c506]
module.app_python.docker_container.python_app: Creation complete after 1s [id=b00da1bf87969677920b3a27bcd42cb0788737f27e1f90c81abf0391c8e99a7e]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

python_container_id = "b00da1bf87969677920b3a27bcd42cb0788737f27e1f90c81abf0391c8e99a7e"
rust_container_id = "5ab81165c3f295bbac41498a3e5bcc0a20937d62b8f0dc44cad1500994a7c506"
```

### terraform show

```hcl
# module.app_python.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "gunicorn",
        "-k",
        "uvicorn.workers.UvicornWorker",
        "-w",
        "4",
        "--bind",
        "0.0.0.0:8080",
        "app:app",
    ]
    env                                         = []
    hostname                                    = "b00da1bf8796"
    id                                          = "b00da1bf87969677920b3a27bcd42cb0788737f27e1f90c81abf0391c8e99a7e"
    image                                       = "sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.dvechtomova_image:
resource "docker_image" "dvechtomova_image" {
    id           = "sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7dvechtomova/python_app"
    image_id     = "sha256:cc3b85e272b5afa89fe75af936806b454d8d99fbb0388a6ee475da640db0c2c7"
    keep_locally = false
    name         = "dvechtomova/python_app"
    repo_digest  = "dvechtomova/python_app@sha256:75042cddcec60f5fd5572c26d5a957dc092afaaa75a32e09e4b7eb1cefa5f4fe"
}
# module.app_rust.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/app/app_rust",
    ]
    env                                         = []
    hostname                                    = "5ab81165c3f2"
    id                                          = "5ab81165c3f295bbac41498a3e5bcc0a20937d62b8f0dc44cad1500994a7c506"
    image                                       = "sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "rust_app"
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
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_rust.docker_image.dvechtomova_image:
resource "docker_image" "dvechtomova_image" {
    id           = "sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1dvechtomova/rust_app"
    image_id     = "sha256:6f34323f4066a9ca5a44406a4ca6f6bd08b420e406f97bb7098e447c12be8ae1"
    keep_locally = false
    name         = "dvechtomova/rust_app"
    repo_digest  = "dvechtomova/rust_app@sha256:293fb19ebeb36641772fb790b70d1e17b1a91e402604ab4b1c63b268fae6ea7a"
}


Outputs:

python_container_id = "b00da1bf87969677920b3a27bcd42cb0788737f27e1f90c81abf0391c8e99a7e"
rust_container_id = "5ab81165c3f295bbac41498a3e5bcc0a20937d62b8f0dc44cad1500994a7c506"
```
