### It's role for deploying dockerized web app using docker compose. 

It has two additional tags:
- **wipe** - to clear docker container and all related file (example: `ansible-playbook playbooks/dev/app_python/main.yml --tags wipe`)
- **deploy** - to deploy your app

Also you can set "web_app_full_wipe: false" to disable default wiping

Role consists of:

1. Tasks:
    1. main.yml - consists of delegated wipe and deploy steps
    2. wipe_web_app - remove previously created docker app and all related files
    3. deliver_docker_compose_file.yml - create and deliver docker compose file to destination. Also activate handler for restart docker compose
    4. pull_image.yml, run_container.yml - files for installation one docker container (from task 1)
2. Handlers:
    1. One handler for restarting docker compose. Used in case of changing docker-compose file
3. Defaults:
    1. All params for docker container (like image, tag, container_name and etc.)
4. Meta:
    Dependency this role of 'docker' role