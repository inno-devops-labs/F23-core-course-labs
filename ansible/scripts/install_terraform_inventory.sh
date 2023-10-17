#!/bin/bash

TFI_BINARY="/usr/bin/terraform-inventory"

[[ $EUID -ne 0 ]] && exec sudo /bin/bash "$0" "$@" 

wget -qO- https://github.com/adammck/terraform-inventory/releases/download/v0.10/terraform-inventory_v0.10_linux_amd64.zip | zcat >> ${TFI_BINARY}
chmod +x ${TFI_BINARY}