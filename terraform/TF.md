# Terraform

## Best Practises

- **Leverage Variables.tf**:
Embrace the use of variables.tf to centralize and parameterize your configuration. This approach streamlines code modification, encourages flexibility, and supports scalability by allowing you to adjust settings without altering the underlying code.
- **Naming Conventions**:
Maintain a standardized naming convention across your Terraform codebase.
- **Secure Sensitive Data**:
Safeguard sensitive information, such as passwords or API keys, by securely storing them in variables.tf or using Terraform-specific mechanisms like environment variables or secret management systems.
- **Utilize Output.tf**:
Employ output.tf files to expose specific values or metadata from your infrastructure code after it has been applied.


## Docker infrastructure

Check terraform state
```shell
terraform state list
```

Output:
```text
docker_container.app_python
docker_image.app_python
```

Check terraform show
```shell
terraform show
```

Output:
```text
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "-m",
        "uvicorn",
        "app_python.src.main:app",
        "--port",
        "8000",
    ]
    env                                         = []
    hostname                                    = "bab3ba3fabbd"
    id                                          = "bab3ba3fabbdcda7d1b12169819e7a088225e28f8b7900502087edf2d949d5b8"
    image                                       = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7"
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
    user                                        = "0"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7yesliesnayder/app_python:1.0.3"
    image_id     = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7"
    keep_locally = false
    name         = "yesliesnayder/app_python:1.0.3"
    repo_digest  = "yesliesnayder/app_python@sha256:9c84ea15c98a163ee74f03fd1f586ecb1e746ce4653ac02a6eeae3f53d13d54c"
}
```

Check output:
```shell
terraform output
```

Output:
```text
container_id = "99ea9eb8ee2f7bcec45dc0665286b708d5e8f1eda6cb179d3a5297639851a2d0"
image_id = "sha256:cde5604b9030bcdf2be26fd64460dc07dd7b24acd84c3916feabf29b6bbfccb7yesliesnayder/app_python:1.0.3"
```