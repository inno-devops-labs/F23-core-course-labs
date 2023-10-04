terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = var.zone
  cloud_id  = var.cloud_id
  token     = var.yandex_token
  folder_id = var.folder_id
}

# https://terraform-provider.yandexcloud.net/Resources/serverless_container
resource "yandex_serverless_container" "nginx_container" {
  count = var.nginx_container_enabled ? 1 : 0
  name               = "anothernginx"
  description        = "yet another nginx container deployed for known purposes"
  memory             = 256
  execution_timeout  = "15s"
  cores              = 1
  core_fraction      = 100
  service_account_id = var.service_account_id
  image {
    url    = var.image_url
    digest = var.image_digest
  }
}


resource "yandex_vpc_network" "default" {
  name = "Default"
}

resource "yandex_vpc_subnet" "subnet_1" {
  name           = "Subnet 1"
  zone           = var.zone 
  network_id     = yandex_vpc_network.default.id
  v4_cidr_blocks = ["192.168.20.0/24"]
}

# https://github.com/darzanebor/terraform-yandex-compute-instance
resource "yandex_compute_instance" "vm_1" {
  name = var.vm_name

  resources {
    memory = var.vm_ram_gb
    cores  = var.vm_cores
  }

  boot_disk {
    initialize_params {
      image_id = var.vm_os_image_id
    }
  }

  metadata = {
    # user-data = "./user_data.yml"
    # ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
    # ssh-keys = "ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCrEh8AEeHWANb5uETRc31s0ffXAYKnqdqVxIgf0TmgM8xmegNf7IC8aOBqdYaqXTHU77ilksExY9VsQJSBvQiw+2+n9v7F1vneJErV+UWuYSwJBxAEVB8IcIvcGNAGADnKQ/P/H9rhAT46yP6+L4C43mYByIR1mnOfChtl00zKGTw23MLMPTK25W6gz0XkpK41Btl0/hIB1dlVLE/BOQ8tDh9aKHGbzrmqxw2hOQhgnoZnnfsk/pQM4aE3GONiVqsMY6gnQhDqIguPnlm49FDAG/RIR59XSwzarF/7pIywWlG6wQxAXscFZESqFNDPz+uCTrWe5vQTgFVKMKmI/WPRbTMHbwNDbV+iaAzLJaZbSnaeYteJ/augpDzMr1lNqAR7DwmTrBkua+5MwwLU88ekNl1j92K0vu0ykLSCNbWIZNEhC7kOUVYSYPlqOnTWpfkTJwPd5WPisEbd4biKbnpn3tPNjf04+1R3Qlj8shNlTCeA4Bpgn5zQ2MXmbUz3ytqM9aMqdtHvst65HSx8R8q3jYDss1ABXMEgwLILADZT3cCwM7gnxb5+qm0dZo/XBHiSJ2K9YSyWKLHktIBdDeDx4P254RXRial63Y+tLDlH5zJJx9F0xB/XGIucXSfZLL3GVs0ZWS6r2dPKaQFZVowy4mfktR4/znb6cnox2wHEmw== yacloud-admin"
    # ssh-keys = "ubuntu:${file(var.ssh_pubkey_path)}" 
    ssh-keys = format("%s:%s", var.vm_user, file(var.ssh_pubkey_path)) 
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }
}