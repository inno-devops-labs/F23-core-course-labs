# TF.md

## Terraform State List

``` bash
docker_container.nginx
docker_image.nginx
```

## Terraform State State

### Terraform State Show `docker_image.nginx`

``` bash
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

### Terraform State Show `docker_container.nginx`

``` bash
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
    hostname                                    = "aa54a2c33410"
    id                                          = "aa54a2c33410ec152b8eb8ab8dab9292dbe3de00536fe468657cbe891ddda12b"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "syslog"
    log_opts                                    = {
        "tag" = "docker-container-{{.ImageName}}-{{.ID}}"
    }
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my-nginx-container"
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
```

## Documented logs

``` bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
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
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "my-nginx-container"
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
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Still creating... [30s elapsed]
docker_image.nginx: Creation complete after 35s [id=sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=736c518eb50b0f1dbd5b3d2f040807908fd595e085fc669a210e035c5722af78]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "736c518eb50b0f1dbd5b3d2f040807908fd595e085fc669a210e035c5722af78"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx"

```

### Terraform Execution Plan

- Terraform is planning to create two resources:
  - `docker_container.nginx`: A Docker container named "my-nginx-container."
  - `docker_image.nginx`: A Docker image for the "nginx" image.

### `docker_container.nginx` Details

- Attributes such as `name`, `ports`, and `restart` are defined.
- Some attributes are marked as `(known after apply)`.

### `docker_image.nginx` Details

- `name` attribute is set to "nginx."

### Execution Plan Summary

- Terraform plans to add two resources (`2 to add`).

### User Confirmation

- Terraform asks for confirmation; type "yes" to proceed.

### Resource Creation Progress

- Terraform creates the resources:
  - `docker_image.nginx`: Shows progress and provides the resource ID.
  - `docker_container.nginx`: Created without issues.

### Apply Completion

- Terraform confirms the completion of the apply operation:
  - Two resources added.
  - No changes or destructions.

## Terraform Output

``` bash
container_id = "736c518eb50b0f1dbd5b3d2f040807908fd595e085fc669a210e035c5722af78"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx"
```

## Terraform Best Practices

### Use of Variables

The Terraform configuration makes extensive use of variables to parameterize various aspects of the infrastructure. This practice enhances flexibility and customization by allowing easy adjustments to configuration settings.

### Provider Configuration in Variables

Sensitive information, such as the GitHub token, is kept separate from the code using variables (e.g., `var.my_token`). This approach ensures secure management of sensitive data and simplifies configuration changes.

### Required Providers

Explicit version constraints for required providers are specified in the `terraform` block. This ensures that the correct provider versions are used, enhancing predictability and stability.

### Resource Configuration

Resource blocks are thoughtfully structured and parameterized with variables. This design facilitates code reuse and maintainability, making it easier to manage infrastructure resources.

### Documentation

Variables are well-documented with clear descriptions, aiding in code readability and helping other users understand the purpose and usage of each variable.

### Default Values

Default values are provided for variables, allowing users to override them when necessary. These defaults offer a smoother out-of-the-box experience while providing flexibility for customization.

### Resource Naming

Resource names are chosen carefully and convey their purpose effectively. This practice enhances the clarity of the configuration.
