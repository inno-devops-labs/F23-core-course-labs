#!/bin/bash

# https://github.com/adammck/terraform-inventory/issues/121#issuecomment-749663776

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TERRAFORM_INVENTORY=`which terraform-inventory`
TF_STATE="$CURRENT_DIR/../../terraform/vkcloud"
"$TERRAFORM_INVENTORY" "$@" "$TF_STATE"
