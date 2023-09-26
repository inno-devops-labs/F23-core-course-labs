## DOCKER

```
➜  docker git:(lab4) ✗ tf state list
docker_container.app_python
docker_image.app_python
```

```
➜  docker git:(lab4) ✗ tf state show docker_image.app_python
# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03wiirtex/python_time_service:0.2.0"
    image_id     = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03"
    keep_locally = false
    name         = "wiirtex/python_time_service:0.2.0"
    repo_digest  = "wiirtex/python_time_service@sha256:7ac8ee903951245fe7fb880a87868d0c28eea0a2e8325124dcc28631ec24fd9f"
}

➜  docker git:(lab4) ✗ tf state show docker_container.app_python
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "/bin/sh",
        "-c",
        ". ~/opt/venv/bin/activate && exec python app_python/src/main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "e49ad91ba5b3"
    id                                          = "e49ad91ba5b3706fb074a90ab9ac1e796d175245f0c968bd75a037ab34395649"
    image                                       = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03"
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
    user                                        = "python_runner"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/python_runner/python/src/app"

    ports {
        external = 7098
        internal = 7098
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```
➜  docker git:(lab4) ✗ tf output
container_id = "e49ad91ba5b3706fb074a90ab9ac1e796d175245f0c968bd75a037ab34395649"
image_id = "sha256:9cbf91966df4b4160414dd20df81450cbeba839865dd1961b3a63532dd0f5a03wiirtex/python_time_service:0.2.0"
```