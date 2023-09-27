# Terraform info

### Best practices
- Use terraform module for the github
- Provide outputs
- Use `terraform fmt`
- Use a variable for the github token
- Use `terraform validate` and `terraform plan` before `terraform apply`

### Initial setup
```
terraform show

# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "uvicorn",
        "main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "80",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "e79b145c9949"
    id                                          = "e79b145c9949cab646d6e09b1a5266f2bebabe146356bd8fcb701c7a42db0faa"
    image                                       = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6"
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
    rm                                          = true
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
    working_dir                                 = "/code"

    ports {
        external = 8081
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.test_image:
resource "docker_image" "test_image" {
    id           = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6xdkomel/myimage:0.0.1"
    image_id     = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6"
    keep_locally = false
    name         = "xdkomel/myimage:0.0.1"
    repo_digest  = "xdkomel/myimage@sha256:42a32fd36d5603b184cf714672171733c048d27f9357c6605d4ba72f46523016"
}
```

```
terraform state list

docker_container.app_python
docker_image.test_image
```

### After adding variables and outputs
```
terraform show

# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "uvicorn",
        "main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "80",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "9307de047739"
    id                                          = "9307de04773913d1f34684eb2ad2241d54a4145ecfe150f4603a43240bc735a3"
    image                                       = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python_container"
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
    rm                                          = true
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
    working_dir                                 = "/code"

    ports {
        external = 8081
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.myimage:
resource "docker_image" "myimage" {
    id           = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6xdkomel/myimage:0.0.1"
    image_id     = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6"
    keep_locally = false
    name         = "xdkomel/myimage:0.0.1"
    repo_digest  = "xdkomel/myimage@sha256:42a32fd36d5603b184cf714672171733c048d27f9357c6605d4ba72f46523016"
}


Outputs:

container_id = "9307de04773913d1f34684eb2ad2241d54a4145ecfe150f4603a43240bc735a3"
image_id = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6xdkomel/myimage:0.0.1"
```

```
terraform state list

docker_container.app_python
docker_image.myimage
```

```
terraform output

container_id = "9307de04773913d1f34684eb2ad2241d54a4145ecfe150f4603a43240bc735a3"
image_id = "sha256:e6cbdbf0a6c78dbc6ead6272f0740055b521afcc04dec3cf761e673ebea9e3c6xdkomel/myimage:0.0.1"
```

