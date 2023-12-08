* > terraform show
```
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "gunicorn",
        "-b",
        ":8000",
        "app:app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "0b942ed58a4b"
    id                                          = "0b942ed58a4b29fa5bf2a798e9e77397b8fb10e1ec3a86529385f8d1e4311ed7"
    image                                       = "sha256:a3bad80a84cd02d65d3f7688333c3204812a88912b6158494ed79cbbd52e4fa2"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-lab-4"
    network_data                                = [
        {
            gateway                   = "192.168.215.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "192.168.215.5"
            ip_prefix_length          = 24
            ipv6_gateway              = ""
            mac_address               = "02:42:c0:a8:d7:05"
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
    user                                        = "newuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:a3bad80a84cd02d65d3f7688333c3204812a88912b6158494ed79cbbd52e4fa2midnoon/devops-lab:latest"
    image_id     = "sha256:a3bad80a84cd02d65d3f7688333c3204812a88912b6158494ed79cbbd52e4fa2"
    keep_locally = false
    name         = "midnoon/devops-lab:latest"
    repo_digest  = "midnoon/devops-lab@sha256:5efe9cfb9878e2aea826a36ec910570df1710b8d99d9908fefb7f4509077bf46"
}
```

* > terraform state list
```
docker_container.app
docker_image.app
```

* > terraform output
```
container_id = "0b942ed58a4b29fa5bf2a798e9e77397b8fb10e1ec3a86529385f8d1e4311ed7"
image_id = "sha256:a3bad80a84cd02d65d3f7688333c3204812a88912b6158494ed79cbbd52e4fa2midnoon/devops-lab:latest"
```
