# Metrics

## Prometheus

![Prometheus Targets](img/targets.png)

## Dashboards

![Loki Dashboard](img/loki_dashboard.png)

![Prometheus Dashboard](img/prometheus_dashboard.png)

## Memory

The resource allocation for the containers involved restricting the CPU usage to 0.2, except for Grafana, which required 0.3 due to its UI building tasks. Memory limits were set at 256MB for all containers, except for Grafana, which was allocated 512MB due to the generation of logs during the UI process

## Log Rotation

The implementation of a log rotation approach involved the strict limitation of each of the 10 log files to a maximum size of 10MB, ensuring careful management