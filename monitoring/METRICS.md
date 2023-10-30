# Monitoring
## Metrics are captured
### Targets
![Targets](img/targets.png)

### Some metrics examples
![Loki](img/loki_metrics.png)

![promtail](img/promtail.png)

## Grafana dashboards
### Prometheus
![Prometheus dashboard](img/prometheus_dash.png)

### Loki
![Loki dashboard](img/loki_dash.png)

## Docker compose updates
### Memory limits
Added 512mb to all containers
### Log rotation
Added general configuration for logger `x-logger` that was added to all containers.
