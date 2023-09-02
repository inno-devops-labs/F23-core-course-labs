# Lab 7: Monitoring and Logging

## Task 1: Logging Stack Setup
1. Study the Logging Stack: Done
2. Create a Monitoring Folder: Done
3. Docker Compose Configuration: Done
4. Testing: demonstration of the logging stack and the application working can be seen in the next task


## Task 2: Documentation and Reporting

1. Role of each component:
    - **Promtail** - agent that collects logs from containers and sends them to Loki.
    - **Loki** - stores logs in a compressed format and indexes them for fast queries
    - **Grafana** - visualizes logs from Loki

2. Screenshots:

![containers in grafana](https://i.imgur.com/E55ZkKL.png)

![logs of python app container](https://i.imgur.com/4Xl2ICq.png)


## Bonus
I have added `app_go` service to the docker-compose.
Logs from `app_go` service:

![logs of go app container](https://i.imgur.com/anMkr0d.png)

I use a log_setup shortcut to setup `docker logs` parameters for each container.
`docker-config.yml` contains settings for promtail to collect logs from all containers.

## References
[Docker Container Logging using Promtail](https://gist.github.com/ruanbekker/c6fa9bc6882e6f324b4319c5e3622460)