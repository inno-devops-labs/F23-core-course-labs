## Task 1: Introduction to Terraform

- `terraform state list`

```
data.twc_configurator.configurator
data.twc_os.os
twc_server.cygnus
twc_ssh_key.timeweb-0xf
```
![[Pasted image 20230926224421.png]]


- `terraform state show data.twc_configurator.configurator`

```
data "twc_configurator" "configurator" {
    cpu_frequency = "3.3"
    disk_type     = "nvme"
    id            = "21"
    location      = "nl-1"

    requirements {
        cpu_max                = 104
        cpu_min                = 2
        cpu_step               = 1
        disk_max               = 2048000
        disk_min               = 40960
        disk_step              = 5120
        network_bandwidth_max  = 1000
        network_bandwidth_min  = 200
        network_bandwidth_step = 100
        ram_max                = 747520
        ram_min                = 2048
        ram_step               = 1024
    }
}
```

- `terraform state show data.twc_os.os`

```
# data.twc_os.os:
data "twc_os" "os" {
    family           = "linux"
    id               = "79"
    name             = "ubuntu"
    version          = "22.04"
    version_codename = "jammy"

    requirements {
        bandwidth_min = 0
        cpu_min       = 0
        disk_min      = 0
        ram_min       = 0
    }
}
```

- `terraform state show twc_ssh_key.timeweb-0xf`

```
# twc_ssh_key.timeweb-0xf:
resource "twc_ssh_key" "timeweb-0xf" {
    body       = (sensitive value)
    created_at = "2023-09-24T18:11:04.000Z"
    id         = "117219"
    name       = "timeweb-0xf"
    used_by    = []
}
```

- `terraform state show twc_server.cygnus` 

```
# twc_server.cygnus:
resource "twc_server" "cygnus" {
    boot_mode       = "std"
    configurator_id = 21
    cpu             = 2
    cpu_frequency   = "3.3"
    disks           = [
        {
            id          = 12674579
            is_mounted  = true
            is_system   = true
            size        = 51200
            status      = "done"
            system_name = "vda"
            type        = "nvme"
            used        = 3860
        },
    ]
    id              = "2001123"
    is_ddos_guard   = false
    location        = "nl-1"
    main_ipv4       = "185.125.203.87"
    name            = "Reasonable Cygnus"
    networks        = [
        {
            bandwidth     = 200
            ips           = [
                {
                    ip      = "185.125.203.87"
                    is_main = true
                    ptr     = ""
                    type    = "ipv4"
                },
            ]
            is_ddos_guard = false
            nat_mode      = ""
            type          = "public"
        },
    ]
    os              = [
        {
            id      = 79
            name    = "ubuntu"
            version = "22.04"
        },
    ]
    os_id           = 79
    preset_id       = 0
    project_id      = 468201
    ram             = 4096
    software        = []
    ssh_keys_ids    = [
        117219,
    ]
    start_at        = "2023-09-26T04:57:00.000Z"
    status          = "on"
    vnc_pass        = (sensitive value)

    configuration {
        configurator_id = 21
        cpu             = 2
        disk            = 51200
        ram             = 4096
    }
}
```

![[Pasted image 20230926224541.png]]

---

## Task 2: Terraform for GitHub

- `terraform output`

```hcl
repositories = [
  {
    "branch_protection_rule" = "BPR_kwDOKXtCqs4CgOWR"
    "default_branch" = "main"
    "description" = "Automatically provisioned codebase"
    "name" = "DevOps-Demo-Repo-2023"
    "visibility" = "public"
  },
  {
    "default_branch" = "main"
    "description" = ""
    "name" = "core-course-labs"
    "visibility" = "public"
  },
]
```

- In order to import the repository the following command was used:	
	- `terraform import "github_repository.course" "core-course-labs"`
![[Pasted image 20230926224707.png]]




## Implemented best practices


- **Naming Conventions**: Follow consistent naming conventions for Terraform resources and variables. Use underscore (snake_case) as recommended in the [Terraform best practices guide](https://www.terraform-best-practices.com/naming).
    
- **Terraform Formatting**: Enforce Terraform code formatting using `terraform fmt` to maintain consistent code style throughout your configuration.
    
- **Modularization**: Organize Terraform code in different folders based on the provider.
    
- **Variable Separation**: Move input variables to a dedicated `variables.tf` file to provide a clear overview of all configurable parameters.
    
- **Output Separation**: Similarly, move output variables to an `outputs.tf` file to centralize the definition of what data your modules or configurations expose.
    
- **Parameterization**: Parameterize any interchangeable inputs, such as server names or SSH public key paths, by defining them as variables in your configuration files.
    
    
## Bonus task

- GitHub includes teams only in the context of organizations. However, our projects are already managed within the context of the current user. Additionally, the Terraform GitHub module can be used only for either user or organization. Therefore, the entire Terraform infrastructure needs to be replicated for the organization.
- When transferring a large project with a significant number of issues, artifacts, etc., from the user to the organization, we first need to transfer the project on GitHub and then import it into Terraform using `terraform import`. However, in our case, a simple empty project is used for testing team permissions. Therefore, it will be sufficient to create a new project in the organization.

![[Pasted image 20230926224207.png]]

![[Pasted image 20230926223928.png]]
![[Pasted image 20230926224020.png]]