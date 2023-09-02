# Variables for Terraform VM provisioning

variable "vm_cores" {
    type = number
    default = 2
}

variable "vm_ram" {
    type = number
    default = 2 
}

variable "vm_name" {
    type = string
    default = "terraform-vm"
}

variable "os_image_id" {
    type = string
    default = "fd8clogg1kull9084s9o" # Ubuntu 22.04 
}

variable "az" {
    type = string
    default = "ru-central1-a"
}

variable "ssh_pubkey" {
    type = string
    sensitive = true
}