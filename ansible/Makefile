

PLAYBOOK_LAB5 := playbooks/dev/main.yml
INVENTORY := --inventory-file=/usr/bin/terraform-inventory
EXTRA_ENV_VARS := TF_STATE=../terraform/yandex/
PLAYBOOK_CMD := ${EXTRA_ENV_VARS} ansible-playbook ${INVENTORY}

MASK_IP := sed -E 's/([0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,7})/XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX/g' | \
		   sed -e 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/X.X.X.X/g'

terraform-inventory:
	which terraform-inventory || ./scripts/install_terraform_inventory.sh

lab5: terraform-inventory
	${PLAYBOOK_CMD} ${PLAYBOOK_LAB5} 

diff:
	${PLAYBOOK_CMD}  --diff ${PLAYBOOK_LAB5} | ${MASK_IP}

list: terraform-inventory
	${EXTRA_ENV_VARS} ansible-inventory --list ${INVENTORY} | ${MASK_IP}
		

