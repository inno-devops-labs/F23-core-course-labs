## Outputs:
- `terraform show`:
    ```
    # docker_container.app:
    resource "docker_container" "app" {
        attach                                      = false
        command                                     = [
            "python3",
            "-m",
            "flask",
            "--app",
            "index",
            "run",
            "-h",
            "0.0.0.0",
            "-p",
            "5555",
        ]
        container_read_refresh_timeout_milliseconds = 15000
        cpu_shares                                  = 0
        entrypoint                                  = []
        env                                         = []
        hostname                                    = "88abea864a39"
        id                                          = "88abea864a3961fe2e95f1a7d7b0c00eab7c04acc194e59d8b34508489abea93"
        image                                       = "sha256:5d8cb27ff3af0e371dce8efc6e38fa5bce4263072f143242892f176b366ea70d"
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
        user                                        = "newuser"
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/python_app"

        ports {
            external = 4000
            internal = 4000
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }

    # docker_image.app:
    resource "docker_image" "app" {
        id           = "sha256:5d8cb27ff3af0e371dce8efc6e38fa5bce4263072f143242892f176b366ea70dlinkstaple/app_python"
        image_id     = "sha256:5d8cb27ff3af0e371dce8efc6e38fa5bce4263072f143242892f176b366ea70d"
        keep_locally = false
        name         = "linkstaple/app_python"
        repo_digest  = "linkstaple/app_python@sha256:41f15fd1ba3386e79ebfeb128d185aea85cd75e64438a1d335d270d408f211f2"
    }
    ```    
- `terraform state list`:
    ```
    docker_container.app
    docker_image.app
    ```
- `terraform output`:
    ```
    container_id = "88abea864a3961fe2e95f1a7d7b0c00eab7c04acc194e59d8b34508489abea93"
    image_id = "sha256:5d8cb27ff3af0e371dce8efc6e38fa5bce4263072f143242892f176b366ea70dlinkstaple/app_python"
    ```