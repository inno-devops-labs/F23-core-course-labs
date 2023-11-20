// Network and subnet
resource "yandex_vpc_network" "this" {
  name = "network-devopscourse"
}

resource "yandex_vpc_subnet" "this" {
  name           = "subnet-devopscourse"
  zone           = var.yc_zone
  network_id     = yandex_vpc_network.this.id
  v4_cidr_blocks = ["10.5.0.0/24"]
}

// Instance
resource "yandex_compute_instance" "this" {
  name                      = "devopscourse"
  allow_stopping_for_update = var.allow_stopping_for_update

  resources {
    cores         = var.cores
    core_fraction = var.core_fraction
    memory        = var.memory
  }

  boot_disk {
    initialize_params {
      image_id = var.yc_image_id
      size     = var.size
    }
  }

  scheduling_policy {
    preemptible = var.preemptible
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.this.id
    nat       = var.is_nat
  }

  metadata = {
    ssh-keys = "${var.ssh_username}:${file("${var.ssh_pubkey}")}"
  }
}
