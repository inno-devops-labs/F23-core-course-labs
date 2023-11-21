Task 1: Prometheus Configuration
Exploration of Prometheus:

Completed
Integration with Docker Compose:

Expansion of the existing docker-compose.yml file from the previous lab to incorporate Prometheus.

Completed

Configuration of Prometheus:

To enable Prometheus to collect metrics from both Loki and Prometheus containers, a configuration file named prometheus.yml will be created. This file will include specifications for scraping Loki and Prometheus.

In Progress

Verification of Prometheus Targets:

Access http://localhost:9090/targets to validate the accurate scraping of metrics by Prometheus.

Screenshots confirming the successful setup will be captured and compiled in a file named METRICS.md, located within the monitoring folder.

Task 2: Dashboard and Configuration Refinements
Service Configuration Updates:

Notable enhancements have been made to the configuration of all services in the docker-compose.yml file:

Log Rotation Mechanisms:

Log setup template has been updated to incorporate log rotation.
Maximum file size: 10 MB
Maximum number of files: 3
Memory Limits for Containers:

Two resource cap templates have been introduced for distinct service categories:
App Resource Cap: 0.1 CPU, 128 MB RAM (suited for relatively simple applications)
Monitoring Resource Cap: 0.5 CPU, 512 MB RAM
Metrics Gathering:

Efforts have been directed towards extending Prometheus to collect metrics from all services specified in the docker-compose.yml file.