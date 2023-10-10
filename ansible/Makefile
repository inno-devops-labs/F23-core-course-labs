

VEBOSITY := -vvv
PLAYBOOK_LAB5 := playbooks/dev/main.yml
PLAYBOOK_APP_PYTHON := playbooks/dev/app_python/main.yml
INVENTORY := --inventory-file=/usr/bin/terraform-inventory
EXTRA_ENV_FILE := ansible.env
EXTRA_ENV_VARS := TF_STATE=../terraform/yandex/ 
PLAYBOOK_CMD := ${EXTRA_ENV_VARS} ansible-playbook ${VEBOSITY} ${INVENTORY}

MASK_IP := sed -E 's/([0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,7})/XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX/g' | \
		   sed -e 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/X.X.X.X/g'

terraform-inventory:
	which terraform-inventory || ./scripts/install_terraform_inventory.sh

requirements:
	ansible-galaxy install -r roles/requirements.yml

configure: terraform-inventory requirements
	[ -f ${EXTRA_ENV_FILE} ] || bash -c "touch ${EXTRA_ENV_FILE} && \
		echo Created empty ${EXTRA_ENV_FILE}. Extra environmental variables can be put there."

include ${EXTRA_ENV_FILE}
export

docker: 
	${PLAYBOOK_CMD} ${PLAYBOOK_LAB5} 

app_python: 
	${PLAYBOOK_CMD} ${PLAYBOOK_APP_PYTHON}

diff:
	${PLAYBOOK_CMD}  --diff ${PLAYBOOK_LAB5} | ${MASK_IP}

list: terraform-inventory
	${EXTRA_ENV_VARS} ansible-inventory --list ${INVENTORY} | ${MASK_IP}
		

