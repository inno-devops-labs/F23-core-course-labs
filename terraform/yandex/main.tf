locals {
  zone             = "ru-central1-a"
  username         = "tnechepurencko"
  ssh_key_path     = "C:\\Users\\321av\\.ssh\\id_ed25519.pub"
  target_folder_id = "b1g4i9h96jsf422npoe8"
  sa_name          = "tnesa"
  vm_name          = "my_vm"
  image_id         = data.yandex_compute_image.ubuntu-2204-lts.image_id
}

terraform {
  required_providers {
    yandex    = {
      source  = "yandex-cloud/yandex"
      version = ">= 0.47.0"
    }
  }
}

provider "yandex" {
  zone = local.zone
}

resource "yandex_container_registry" "my-registry" {
  name       = var.registry_name
  folder_id  = local.target_folder_id
  labels     = {
    my-label = "my-label-value"
  }
}

resource "yandex_iam_service_account" "registry-sa" {
  name      = local.sa_name
  folder_id = local.target_folder_id
}

resource "yandex_resourcemanager_folder_iam_member" "registry-sa-role-images-puller" {
  folder_id = local.target_folder_id
  role      = "container-registry.images.puller"
  member    = "serviceAccount:${yandex_iam_service_account.registry-sa.id}"
}

resource "yandex_vpc_network" "docker-vm-network" {}

resource "yandex_vpc_subnet" "docker-vm-network-subnet-a" {
  zone           = local.zone
  v4_cidr_blocks = ["192.168.1.0/24"]
  network_id     = yandex_vpc_network.docker-vm-network.id
}

resource "yandex_compute_instance" "docker-vm" {
  name               = local.vm_name
  platform_id        = "standard-v3"
  zone               = local.zone
  service_account_id = "${yandex_iam_service_account.registry-sa.id}"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = local.image_id
      size     = 5
    }
  }

  network_interface {
    subnet_id = "${yandex_vpc_subnet.docker-vm-network-subnet-a.id}"
    nat       = true
  }

  metadata = {
    user-data = "#cloud-config\nusers:\n  - name: ${local.username}\n    groups: sudo\n    shell: /bin/bash\n    sudo: 'ALL=(ALL) NOPASSWD:ALL'\n    ssh-authorized-keys:\n      - ${file("${local.ssh_key_path}")}"
  }
}
