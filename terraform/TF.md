# Terraform

## Terraform best practices 

- Divide the configuration into multiple files.
- Utilize terraform fmt to verify the correct formatting of the files.
- Treat the .tfstate file as sensitive data that should not be publicly shared or distributed among developers. It is more secure to use a "remote" backend to store it on a server, allowing multiple developers to collaborate on the same state.
- Limit the use of the terraform.tfvars file to compositions only.

## terraform-docker

```
terraform apply
```

```
terraform show
```

Output: 

```sh
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
    hostname                                    = "e49a05ff930a"
    id                                          = "e49a05ff930afe7bc6dbe4fbf37496b345af77a369cafaf26ae7e31604d5d310"
    image                                       = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
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
    id           = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73nginx"
    image_id     = "sha256:2a4fbb36e96607b16e5af2e24dc6a1025a4795520c98c6b9ead9c4113617cb73"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```
---
```
 terraform state list
```
Output: 

```sh
docker_container.nginx
docker_image.nginx
```
---
```
terraform output
```
output:
```sh
container_id = "dc9f9aeadabada45995be345e91c45043643abba54858fffe11091373a347b91"
image_id = "sha256:61395b4c586fa2b9b3b8ca903ea6a448e6783drdd7f768ff2c1a0f3360aaba99nginx:latest"
```