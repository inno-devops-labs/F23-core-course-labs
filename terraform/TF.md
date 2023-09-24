## Terraform

> Note: Docker infrastructure is stored in ./docker/ subfolder as there will be several instances.

Following the turorial I built inftastructure for my `app_python` using docker container, and here are the outputs of requested commands:

---

`terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.app_python_container will be created
  + resource "docker_container" "app_python_container" {
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
      + name                                        = "app_python_terraform"
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
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.app_python will be created
  + resource "docker_image" "app_python" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "elatypovinno/devops_inno:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.app_python: Creating...
docker_image.app_python: Still creating... [10s elapsed]
docker_image.app_python: Creation complete after 18s [id=sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3felatypovinno/devops_inno:latest]
docker_container.app_python_container: Creating...
docker_container.app_python_container: Creation complete after 1s [id=fc9045d89fa91daf4f7cf4b059a52b3c7566198ce5fe7c0f17d55a30c0f60da3]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "fc9045d89fa91daf4f7cf4b059a52b3c7566198ce5fe7c0f17d55a30c0f60da3"
image_id = "sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3felatypovinno/devops_inno:latest"
```

---

`terraform show` (there is a mistake in requested command, cause `terraform state show` expect specified state to show, while `terraform show` shows all the states)

```
# docker_container.app_python_container:
resource "docker_container" "app_python_container" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "fc9045d89fa9"
    id                                          = "fc9045d89fa91daf4f7cf4b059a52b3c7566198ce5fe7c0f17d55a30c0f60da3"
    image                                       = "sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python_terraform"
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
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3felatypovinno/devops_inno:latest"
    image_id     = "sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3f"
    keep_locally = false
    name         = "elatypovinno/devops_inno:latest"
    repo_digest  = "elatypovinno/devops_inno@sha256:2505173e38c3876e53a89dbd9f401eae5f8e97dfc0000061463eaf9e6bbd3b19"
}


Outputs:

container_id = "fc9045d89fa91daf4f7cf4b059a52b3c7566198ce5fe7c0f17d55a30c0f60da3"
image_id = "sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3felatypovinno/devops_inno:latest"
```

---

`terraform state list`

```
docker_container.app_python_container
docker_image.app_python
```

---

`terraform output`

```
container_id = "fc9045d89fa91daf4f7cf4b059a52b3c7566198ce5fe7c0f17d55a30c0f60da3"
image_id = "sha256:0c585da953ad654d26bc1d0a3a08c58e1563e956134ccfd8594bbbc070e77e3felatypovinno/devops_inno:latest"
```