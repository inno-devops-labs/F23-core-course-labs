#!/usr/bin/env bash

# from ansible dir run
# ansible-playbook --inventory-file=./inventory/dynamic_inventory.sh ./playbooks/dev/main.yml
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TERRAFORM_INVENTORY=`which terraform-inventory`
TF_STATE="$CURRENT_DIR/../../vk_cloud"    # <<== relative path to dir with .tfstate
"$TERRAFORM_INVENTORY" "$@" "$TF_STATE"
