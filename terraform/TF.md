# The output of the following commands:

- output of ```terraform state list```:

```
docker_container.nginx
docker_image.nginx
```
- output of ```terraform state show docker_container.nginx```:

```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "5595fbbda4d5"
    id                                          = "5595fbbda4d5ea493214ad3eb9b3818ce11efd02d193f57ff167d1a3e865165f"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

- output of ```terraform state show docker_image.nginx```:
```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```
- output of ```terraform output```:
```
container_id = "af05e62289e4da2cf8c1ab3b2ce62288ad5787d1ed8510cdd224cc03544b3d1c"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
```


# Applied changes:

- port is changed to 8088; changes in logs:
  - before:
    ```
      ...
      ports {
        external = 8000
        internal = 80
      ...
    ```
  - after: 
  
    ```
      ...
      ports {
        external = 8088
        internal = 80
      ...
    ```
- input variable for the container name defined
  - before:
    ```
      ...
      must_run                                    = true
      name                                        = "Tutorial"
      network_data                                = [
      ...
    ```
  - after: 
  
    ```
      ...
      must_run                                    = true
      name                                        = "YetAnotherName"
      network_data                                = [
      ...
    ```
- outputs for ```container_id``` and ```image_id``` are defined
  - the following lines was added in the result of ```terraform show```:
  ```
    Outputs:
    
    container_id = "af05e62289e4da2cf8c1ab3b2ce62288ad5787d1ed8510cdd224cc03544b3d1c"
    image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    ```


# Best practices:

- Use separate directories for each application
- Terraform configurations files separation (main.tf, variables.tf, outputs.tf)
- Follow a standard module structure
- Personal data in variables
- Declare all variables in variables.tf; avoid hardcoding variable
- Organize all outputs in an outputs.tf file