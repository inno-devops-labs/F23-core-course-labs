It's custom docker deploy role. It consists of:

1. Tasks:
    1. main.yml - check if docker is not installed yet and start other tasks
    2. install_docker - add docker apt repo and using apt install it
    3. install_pip - install latest pip
    4. install_docker_compose - install the docker compose for needed arch
2. Handlers:
    1. One handler for restarting docker service after installtion
3. Defaults:
    1. All needed requirements (apt-transport-https, ca-certificates, curl, software-properties-common)
    2. All params for installation