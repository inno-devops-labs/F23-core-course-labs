
# Docker

## terraform state list

```
module.app_python.docker_container.python_app
module.app_python.docker_image.python_app_image
module.app_typescript.docker_container.python_app
module.app_typescript.docker_image.python_app_image
```

## terraform show

```
# module.app_python.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = [
        "python",
        "manage.py",
        "runserver",
        "0.0.0.0:8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = []
    env                                         = []
    group_add                                   = []
    hostname                                    = "7e8f5445668a"
    id                                          = "7e8f5445668adde40aa9e23f66256da4350f1e5c9ac9b59547e38812a3290e27"
    image                                       = "sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
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
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    user                                        = "cooluser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.python_app_image:
resource "docker_image" "python_app_image" {
    id           = "sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031rametago/my-first-repo:latest"
    image_id     = "sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031"
    keep_locally = false
    name         = "rametago/my-first-repo:latest"
    repo_digest  = "rametago/my-first-repo@sha256:7aa92828447bdc7b82fb9ded07f674769d0bac4fb8be1b55186f34e74f2d6120"
}
# module.app_typescript.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "npm",
        "run",
        "dev",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "37d6821be5ae"
    id                                          = "37d6821be5ae484ff173d54720214061b6c1d88d00a62288644f4f155963f61b"
    image                                       = "sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "typescript_app"
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
    }
}

# module.app_typescript.docker_image.python_app_image:
resource "docker_image" "python_app_image" {
    id           = "sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0rametago/my-first-repo:svelte"
    image_id     = "sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0"
    keep_locally = false
    name         = "rametago/my-first-repo:svelte"
    repo_digest  = "rametago/my-first-repo@sha256:67f9ac5d63f678b79cb9c995d450cbded94c8ad3d863c8bf1c25bc62635bd3f8"
}


Outputs:

python_container_id = "7e8f5445668adde40aa9e23f66256da4350f1e5c9ac9b59547e38812a3290e27"
typescript_container_id = "37d6821be5ae484ff173d54720214061b6c1d88d00a62288644f4f155963f61b"
```

## terraform plan
After changing container name

```
module.app_python.docker_image.python_app_image: Refreshing state... [id=sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031rametago/my-first-repo:latest]
module.app_typescript.docker_image.python_app_image: Refreshing state... [id=sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0rametago/my-first-repo:svelte]
module.app_typescript.docker_container.python_app: Refreshing state... [id=37d6821be5ae484ff173d54720214061b6c1d88d00a62288644f4f155963f61b]
module.app_python.docker_container.python_app: Refreshing state... [id=7e8f5445668adde40aa9e23f66256da4350f1e5c9ac9b59547e38812a3290e27]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy

Terraform will perform the following actions:

  # module.app_python.docker_container.my_python_app will be created
  + resource "docker_container" "my_python_app" {
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
      + image                                       = "sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "my_python_app"
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
          + external = 5000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.app_python.docker_container.python_app will be destroyed
  # (because docker_container.python_app is not in configuration)
  - resource "docker_container" "python_app" {
      - attach                                      = false -> null
      - command                                     = [
          - "python",
          - "manage.py",
          - "runserver",
          - "0.0.0.0:8000",
        ] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      - entrypoint                                  = [] -> null
      - env                                         = [] -> null
      - group_add                                   = [] -> null
      - hostname                                    = "7e8f5445668a" -> null
      - id                                          = "7e8f5445668adde40aa9e23f66256da4350f1e5c9ac9b59547e38812a3290e27" -> null
      - image                                       = "sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031" -> null
      - init                                        = false -> null
      - ipc_mode                                    = "private" -> null
      - log_driver                                  = "json-file" -> null
      - log_opts                                    = {} -> null
      - logs                                        = false -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      - must_run                                    = true -> null
      - name                                        = "python_app" -> null
      - network_data                                = [
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
        ] -> null
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      - read_only                                   = false -> null
      - remove_volumes                              = true -> null
      - restart                                     = "no" -> null
      - rm                                          = false -> null
      - runtime                                     = "runc" -> null
      - security_opts                               = [] -> null
      - shm_size                                    = 64 -> null
      - start                                       = true -> null
      - stdin_open                                  = false -> null
      - stop_timeout                                = 0 -> null
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - tty                                         = false -> null
      - user                                        = "cooluser" -> null
      - wait                                        = false -> null
      - wait_timeout                                = 60 -> null
      - working_dir                                 = "/app" -> null

      - ports {
          - external = 5000 -> null
          - internal = 5000 -> null
          - ip       = "0.0.0.0" -> null
          - protocol = "tcp" -> null
        }
    }

  # module.app_typescript.docker_container.my_python_app will be created
  + resource "docker_container" "my_python_app" {
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
      + image                                       = "sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "my_typescript_app"
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
          + external = 5137
          + internal = 5137
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.app_typescript.docker_container.python_app will be destroyed
  # (because docker_container.python_app is not in configuration)
  - resource "docker_container" "python_app" {
      - attach                                      = false -> null
      - command                                     = [] -> null
      - container_read_refresh_timeout_milliseconds = 15000 -> null
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      - entrypoint                                  = [
          - "npm",
          - "run",
          - "dev",
        ] -> null
      - env                                         = [] -> null
      - group_add                                   = [] -> null
      - hostname                                    = "37d6821be5ae" -> null
      - id                                          = "37d6821be5ae484ff173d54720214061b6c1d88d00a62288644f4f155963f61b" -> null
      - image                                       = "sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0" -> null
      - init                                        = false -> null
      - ipc_mode                                    = "private" -> null
      - log_driver                                  = "json-file" -> null
      - log_opts                                    = {} -> null
      - logs                                        = false -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      - must_run                                    = true -> null
      - name                                        = "typescript_app" -> null
      - network_data                                = [
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
        ] -> null
      - stop_timeout                                = 0 -> null
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - tty                                         = false -> null
      - user                                        = "myuser" -> null
      - wait                                        = false -> null
      - wait_timeout                                = 60 -> null
      - working_dir                                 = "/app" -> null

      - ports {
          - external = 5137 -> null
          - internal = 5137 -> null
          - ip       = "0.0.0.0" -> null
          - protocol = "tcp" -> null
        }
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ python_container_id     = "7e8f5445668adde40aa9e23f66256da4350f1e5c9ac9b59547e38812a3290e27" -> (known after apply)
  ~ typescript_container_id = "37d6821be5ae484ff173d54720214061b6c1d88d00a62288644f4f155963f61b" -> (known after apply)

```

## terraform apply

```
module.app_typescript.docker_image.python_app_image: Refreshing state... [id=sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0rametago/my-first-repo:svelte]
module.app_python.docker_image.python_app_image: Refreshing state... [id=sha256:1ee188ee093eccd79c290c7a0124ddc9cb5f3fad996d98dbbd373c3d6e6f6031rametago/my-first-repo:latest]
module.app_typescript.docker_container.my_python_app: Refreshing state... [id=bd2d57065b8ee5e13f93c966478719de584d9b92584fba7a8a9d16d6f16c0860]
module.app_python.docker_container.my_python_app: Refreshing state... [id=00da0fd199ce4e5d0151ef8ff41a2fec33684414e653ebac42f161ae0c6afd89]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

  # module.app_typescript.docker_container.my_python_app has been deleted
  - resource "docker_container" "my_python_app" {
      - id                                          = "bd2d57065b8ee5e13f93c966478719de584d9b92584fba7a8a9d16d6f16c0860" -> null
        name                                        = "my_typescript_app"
        # (16 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following plan may include actions to undo or
respond to these changes.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.app_typescript.docker_container.my_python_app will be created
  + resource "docker_container" "my_python_app" {
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
      + image                                       = "sha256:2e6f493e826171d69a1942acf3b498eea6c7b8657ef178e7d33a6b52a14a97b0"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "my_typescript_app"
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
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.app_typescript.docker_container.my_python_app: Creating...
module.app_typescript.docker_container.my_python_app: Creation complete after 2s [id=895943a470d3614559693837baca96fd3d4333c1ebb2a06e0d20335fd40efe0f]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

python_container_id = "00da0fd199ce4e5d0151ef8ff41a2fec33684414e653ebac42f161ae0c6afd89"
typescript_container_id = "895943a470d3614559693837baca96fd3d4333c1ebb2a06e0d20335fd40efe0f"
```

## terraform output

```
python_container_id = "0fa450e2677645f00c1ef4532c1b02d3d1addeb56910f1131b06b4ef21377632"
typescript_container_id = "272f97e1e1ad3192d379be407238961d01b185fb8bb280f17df1e60ddd3a2874"
```
