# Metrics


## Prometheus

![prometheus_1](prometheus/images/prometheus_targets_1.jpg)

![prometheus_2](prometheus/images/prometheus_targets_2.jpg)

## Grafana

### Grafana Dashboards

![grafana_dashboards](prometheus/images/grafana_dashboards.jpg)


#### Total Requests logs

![total_requests_logs](prometheus/images/grafana_requeses_logs.jpg)

#### Loki Dashboard

![loki_dashboards](prometheus/images/loki.jpg)

#### Prometheus Overview

![prometheus_overview](prometheus/images/prometheus_overview.jpg)

#### Prometheus Stats

![prometheus_stats](prometheus/images/prometheus_stats.jpg)


# Health Checkers

![docker_health_checkers](prometheus/images/docker_health_checkers.jpg)


# Configuration details

### Log rotation

Log rotation with 5 files of 15 MB is set

```shell
options:
    tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
    max-size: "15m"
    max-file: "5"
```

### Memory limits

1 GB memory limit is specified

```shell
deploy:
    resources:
    limits:
        memory: 1g
```