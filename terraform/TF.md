### **Result of terraform state show:**

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
    hostname                                    = "c03b5c5b2132"
    id                                          = "c03b5c5b21322616113949bc566cfb38f1632ada3ba52d6e4dc0d495aad1950b"
    image                                       = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647"
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
    id           = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647nginx"
    image_id     = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6"
}
```

### **Result of terraform state list:**
```
docker_container.nginx
docker_image.nginx
```

### **Applied changes:**
```
ports {
        external = 80
        internal = 8080
```

### **Log with the applied changes:**
```
Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

### **Result of terraform output:**
```
container_id = "45c5af98f1892cb48a6bbfb4cc2eff7df330e80042406248255b805599f84c91"
image_id = "sha256:c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647nginx"
```

### **Terraform on VKCloud:**
```
terraform {
    required_providers {
        vkcs = {
            source = "vk-cs/vkcs"
            version = "~> 0.1.12" 
        }
    }
}

provider "vkcs" {
    # Your user account.
    username = "evgn.worker@gmail.com"

    # The password of the account
    password = "YOUR_PASSWORD"

    # The tenant token can be taken from the project Settings tab - > API keys.
    # Project ID will be our token.
    project_id = "2cd713920a2443fa9c08c5e4f0208c82"
    
    # Region name
    region = "RegionOne"
    
    auth_url = "https://infra.mail.ru:35357/v3/" 
}
```

### **Best Practices:**
1. Adhere to a conventional module hierarchy. Each module should begin with a main.tf file, which is where the default resources are saved.
2. Use underscores to separate words in the names of all configuration objects (**f.e. github_branch_default**). This procedure guarantees that resource types, data source types, and other preset values are all named consistently.
3. Put all the outputs into a file called outputs.tf.
4. Keep expression complexity to a minimum
5. Group resources logically by giving them descriptive names like loadbalancer.tf, instances.tf, or network.tf, along with their own files.
6. In variables.tf, declare every variable.
7. Give variables names that are descriptive and appropriate for their intended use.
