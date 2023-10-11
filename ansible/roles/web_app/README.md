It's role for deploying dockerized web app using docker compose. It consists of:

 1. Tasks:
     1. main.yml - consists of delegated wipe and deploy steps
     2. wipe_web_app - remove previously created docker app
     3. deliver_docker_compose_file.yml - create and deliver docker compose file to destination. Also activate handler for restart docker compose
     4. pull_container.yml, run_container.yml - files for installation one docker container (from task 1)
 2. Handlers:
     1. One handler for restarting docker compose when changing docker-compose file
 3. Defaults:
     1. All params for docker container (image, tag, container_name and etc.)
 4. Meta:
     Dependency this role of 'docker' role