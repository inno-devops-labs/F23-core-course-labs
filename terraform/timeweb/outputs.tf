
locals {
  timeweb_servers = [
    {
      name = twc_server.cygnus.name
      disk = format("%d GB", twc_server.cygnus.configuration[0].disk)
      cpu  = twc_server.cygnus.cpu
      ram  = format("%d GB", twc_server.cygnus.configuration[0].ram)
    }
  ]
  timeweb_ssh_keys = [twc_ssh_key.timeweb-0xf.name]
}

output "servers" {
  value = local.timeweb_servers
}

output "ssh_keys" {
  value = local.timeweb_ssh_keys
}
