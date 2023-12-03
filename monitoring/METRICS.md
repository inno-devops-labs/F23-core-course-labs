# Metrics

## Prometheus targets

Prometheus is successfully scraping metrics from 4 apps:
- Prometheus
- Loki
- App Python
- App Golang

Targets: `http://localhost:9090/targets`

![Prometheus targets](./images/prometheus_targets.png)

## Grafana dashboards

Used external dashboards:
[Loki](https://grafana.com/grafana/dashboards/13407),
[Prometheus](https://grafana.com/grafana/dashboards/3662)

### Loki

![Loki dashboard](./images/loki_dash.png)

### Prometheus

![Prometheus dashboard](./images/prometheus_dash.png)

## Service configuration

### Log rotation

All logs are stored in the json-format and if they reach a `max-size` limit, then they will be rotated.

```yaml
max-size: "100m"
max-file: "2"
```

### Memory limits

All services have memory limit that is described in `docker-compose.yml` file:

- **app_python**: 256 MB
- **app_golang**: 256 MB
- **loki**: 512 MB
- **promtail**: 512 MB
- **grafana**: 1 GB
- **prometheus**: 1 GB

To set these limits, I used docker compose v3 format:

```yaml
deploy:
  resources:
    limits:
      memory: 256m
```

## Application metrics

Python application contains metrics to count amount of requests:

![Python metrics](./images/app_python_metrics.png)

Golang application also contains metrics for amount of requests:

![Golang metrics](./images/app_golang_metrics.png)

Totally, I have dashboard in Grafana to see amount of requests:

![Metrics dashboard](./images/requests_total.png)

## Health Checks

Each service in `docker-compose.yml` file has healthcheck:

- **app_python**: `/healthz`
- **app_golang**: `/healthz`
- **loki**: `/ready`
- **promtail**: use root path `/`
- **grafana**: `/api/health`
- **prometheus**: `/healthy`

Docker compose checks endpoint by using `curl` and `wget` commands.