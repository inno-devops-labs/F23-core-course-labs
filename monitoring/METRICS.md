# Metrics

## Memory and log rotation
The following memory and resources utilization was applied:
- all the containers were limited to use 0.2 of CPU resources (except for Grafana with 0.3 parameter, as it need to build UI)
- all the containers were limited to fill up to 256MB of memory (except for Grafana with 512MB due to logs creation in UI process)

There was also added log rotation technique, using 10 files of 10MB max size each.

## Dashboards
As for the dashboards in Grafana, the following setups from GrafanaLabs were used:
- Loki dashboard - https://grafana.com/grafana/dashboards/13407-loki2-0-global-metrics/
- Prometheus dashboard - https://grafana.com/grafana/dashboards/3662-prometheus-2-0-overview/

## Screenshots

![Verify Prometheus Targets](images/targets.png)

![Loki Dashboard](images/loki_dashboard.png)

![Prometheus Dashboard](images/prometheus_dashboard.png)



