(venv) purfreak@Tashas-MBP terraform % terraform state list
docker_container.my_python_app
docker_image.image_python_app


(venv) purfreak@Tashas-MBP terraform % terraform state show docker_container.my_python_app

# docker_container.my_python_app:
resource "docker_container" "my_python_app" {
    attach                                      = false
    command                                     = [
        "uvicorn",
        "app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "8a7ee502d65a"
    id                                          = "8a7ee502d65a15b5ee1ea87d164bd36774855deadf2d5ec138abde1f57231bf0"
    image                                       = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412e"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my_python_app"
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
    user                                        = "myuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/myuser/app"

    ports {
        external = 5555
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

(venv) purfreak@Tashas-MBP terraform % terraform state show docker_image.image_python_app 

# docker_image.image_python_app:
resource "docker_image" "image_python_app" {
    id           = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412epurfreak/lab2_devops:latest"
    image_id     = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412e"
    keep_locally = false
    name         = "purfreak/lab2_devops:latest"
}


(venv) purfreak@Tashas-MBP terraform % terraform apply
docker_image.image_python_app: Refreshing state... [id=sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412epurfreak/lab2_devops:latest]
docker_container.my_python_app_new: Refreshing state... [id=f40b53004c4a9aa77ac2789d3125bcc8513fbc97665bbbd9059fea1ec2a4069f]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.my_python_app will be created
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
      + image                                       = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412e"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "my_python_app_new"
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
          + external = 5555
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.my_python_app: Creating...
docker_container.my_python_app: Creation complete after 1s [id=d05856b8bbd0ecd92dfe444a9bc980f73b468e8b7ddb4c45ff3b4e4e7a87bc1d]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.


(venv) purfreak@Tashas-MBP terraform % terraform output
container_id = "d05856b8bbd0ecd92dfe444a9bc980f73b468e8b7ddb4c45ff3b4e4e7a87bc1d"
image_id = "sha256:d688c9693b47de3de6d4dad63ba440fd7d3a3c36118fbc1c3c29005420ae412epurfreak/lab2_devops:latest"
