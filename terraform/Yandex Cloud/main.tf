locals {
  username         = "irina"
  ssh_key_path     = "C:/Users/User/.ssh/id_ed25519.pub"
  target_folder_id = "b1gjbm51n00a8fsff0qm"
  registry_name    = "time-app"
  sa_name          = "time-app-acc"
  network_name     = "default"
  subnet_name      = "default-ru-central1-a"
  vm_name          = "vm-1"
  image_id         = "ubuntu-1604-lts-1549457823"
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
  zone = var.zone
  service_account_key_file = "C:/Users/User/PycharmProjects/DevOps_labs/authorized_key.json"
  cloud_id = "b1geumonv5j8ou45vrp6"
  folder_id = "b1gjbm51n00a8fsff0qm"
}

resource "yandex_container_registry" "my-registry" {
  name       = local.registry_name
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

resource "yandex_vpc_network" "docker-vm-network" {
  name = local.network_name
}

resource "yandex_vpc_subnet" "docker-vm-network-subnet-a" {
  name           = local.subnet_name
  zone           = var.zone
  v4_cidr_blocks = ["192.168.1.0/24"]
  network_id     = yandex_vpc_network.docker-vm-network.id
}

resource "yandex_compute_instance" "docker-vm" {
  name               = local.vm_name
  platform_id        = "standard-v3"
  zone               = var.zone
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
