# Output of `terraform state list`

## Output of `terraform state show docker_container.app_python`

```hcl
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "uvicorn",
        "--host",
        "0.0.0.0",
        "--port",
        "8080",
        "app_python.main:app",
    ]
    env                                         = []
    hostname                                    = "425633d789aa"
    id                                          = "425633d789aa06db39eb825418b5fdbec30495d0d3386362dfe416d64ce73db0"
    image                                       = "sha256:4cd47d1858607449e27d65859be4a037bc7b1465d31784e35dd9a9affae65e7b"
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
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## Output of `terraform state show docker_image.app_python`

```hcl
# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:4cd47d1858607449e27d65859be4a037bc7b1465d31784e35dd9a9affae65e7bamoriodi/app_python:latest"
    image_id     = "sha256:4cd47d1858607449e27d65859be4a037bc7b1465d31784e35dd9a9affae65e7b"
    keep_locally = false
    name         = "amoriodi/app_python:latest"
    repo_digest  = "amoriodi/app_python@sha256:f9ae871ef853af2531f1fcfee56f1213a1940685a3224f2a5273e61fd9aa0af0"
}
```

# Output of `terraform output`

```hcl
container_id = "e792a286aa938cad204fd7cd81b9131a8fb58239642f1e351ea0c9d49357d37c"
image_id = "sha256:4cd47d1858607449e27d65859be4a037bc7b1465d31784e35dd9a9affae65e7bamoriodi/app_python:latest"
```
