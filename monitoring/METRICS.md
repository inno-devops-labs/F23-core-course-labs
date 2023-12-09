# Lab 8: Monitoring with Prometheus
## Task 1: Prometheus Setup


Prometheus Setup:
Set up Prometheus to gather metrics from both Loki and Prometheus containers.

To achieve this, generate a configuration file named prometheus.yml that includes configurations for scraping both Loki and Prometheus.
Confirm Prometheus Targets:
Visit http://localhost:9090/targets to validate that Prometheus is effectively collecting metrics.
Document the successful configuration by taking screenshots and save them in a file called METRICS.md within the monitoring folder.

Attached are the corresponding screenshots:

![Prometheus scraping Loki and Prometheus](https://i.imgur.com/CvswNoO.png)
![Graph](https://i.imgur.com/5zXCeDB.png)

## Task 2: Dashboard and Configuration Enhancements

1. Dashboards:

Prometheus:
![Prometheus Grafana Dashboard](https://i.imgur.com/FHNpyP5.png)
Loki:
![Loki Grafana Dashboard](https://i.imgur.com/Hkrn4SL.png)


2. Service Configuration Updates:
Revise the settings for all services within the docker-compose.yml file:
Implement log rotation mechanisms.
Specify memory limits for containers.

The log_setup template has been modified to incorporate log rotation:
Maximum file size: 10 MB
Maximum number of files: 3
Two resource cap templates have been added for app and monitoring services:
App resource cap: 0.1 CPU, 128 MB RAM (considering the simplicity of apps)
Monitoring resource cap: 0.5 CPU, 512 MB RAM

3. Metrics Gathering:

Expand Prometheus to collect metrics from all services defined in the docker-compose.yml file.

Currently, metrics are collected from all monitoring services, while modifications are pending for the bonus task to include metric gathering for app_python and app_go services (refer to the task below).


![Prometheus for all services](https://i.imgur.com/If1EyNP.png)
