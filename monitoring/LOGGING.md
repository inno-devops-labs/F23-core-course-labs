
Task 1: Configuration of Logging Stack
Familiarization with Logging Stack: Completed
Establishment of Monitoring Folder: Completed
Configuration of Docker Compose: Completed
Testing: The operational demonstration of both the logging stack and the application is scheduled for the subsequent task.
Task 2: Documentation and Reporting
Functional Roles of Each Component:
Promtail - Acts as an agent, collecting logs from containers and transmitting them to Loki.
Loki - Functions as a storage platform, compressing and indexing logs to facilitate rapid queries.
Grafana - Serves the purpose of visualizing logs sourced from Loki.
The utilization of a log_setup shortcut streamlines the configuration of docker logs parameters for individual containers. The settings for Promtail to gather logs from all containers are consolidated within the docker-config.yml file.