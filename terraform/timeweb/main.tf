terraform {
  required_version = ">= 1.2.0"
  required_providers {
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
}

provider "twc" {
  token = var.timeweb_token
}


data "twc_configurator" "configurator" {
  location  = "pl-1"
  disk_type = "nvme"
}

# Create new SSH key
# SSH key can be imported by specifying the numeric identifier from URL
# terraform import twc_ssh_key.example 42
resource "twc_ssh_key" "timeweb-0xf" {
  name = "timeweb-0xf"
  body = file(var.timeweb_ssh_pubkey)
}

resource "twc_vpc" "internal" {
  name = "Internal VPC"
  description = "Internal VPC"
  subnet_v4 = "192.168.0.0/24"
  location = "pl-1"
}


data "twc_os" "os" {
  name    = "ubuntu"
  version = "22.04"
}


# Server can be imported by specifying the numeric identifier (from URL)
# terraform import twc_server.example 42 
resource "twc_server" "cygnus" {
  name  = var.instance_name
  os_id = data.twc_os.os.id

  configuration {
    configurator_id = data.twc_configurator.configurator.id
    disk            = 1024 * 50
    cpu             = 2
    ram             = 1024 * 4
  }

  ssh_keys_ids = [twc_ssh_key.timeweb-0xf.id]

  local_network {
    id = twc_vpc.internal.id
    ip = "192.168.0.15"
  }

}
