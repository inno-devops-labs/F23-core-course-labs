# Terraform

## list
    terraform state list

Output:

    docker_container.app_python
    docker_image.app_python_image


## show
    terraform show

Output:

    # docker_container.app_python:
    resource "docker_container" "app_python" {
        attach                                      = false
        command                                     = []
        container_read_refresh_timeout_milliseconds = 15000
        cpu_shares                                  = 0
        entrypoint                                  = [
            "python3",
            "-m",
            "flask",
            "run",
            "--host=0.0.0.0",
        ]
        env                                         = []
        hostname                                    = "a6973460a287"
        id                                          = "a6973460a287574461b480097acfb151a34589c7fd5f3b5573e74ebc6dde109c"
        image                                       = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1e"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "devops_msk_time"
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
        user                                        = "newuser"
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/msk_time"

        ports {
            external = 5000
            internal = 5000
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }

    # docker_image.app_python_image:
    resource "docker_image" "app_python_image" {
        id           = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1ekurohata7/devops_msk_time"
        image_id     = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1e"
        keep_locally = false
        name         = "kurohata7/devops_msk_time"
        repo_digest  = "kurohata7/devops_msk_time@sha256:48cb36f3e629274d373801220166f4382848272e7b69d1d6e3e49384ffb51681"
    }


    Outputs:

    container_id = "a6973460a287574461b480097acfb151a34589c7fd5f3b5573e74ebc6dde109c"
    image_id = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1ekurohata7/devops_msk_time"

## outputs

    terraform outputs

Output:

    container_id = "a6973460a287574461b480097acfb151a34589c7fd5f3b5573e74ebc6dde109c"
    image_id = "sha256:efa94cf3cd832855046de85be60a3d869d6e3e8f1a2e07772eb9c007f1868b1ekurohata7/devops_msk_time"
