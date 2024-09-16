# Metrics

## Prometheus Targets

![alt_text](./images/prometheus_targets.png)

## Grafana dashboards

Used advised dashboards for Loki and Prometheus

### Loki

![alt_text](./images/loki_dash.png)

### Prometheus

![alt_text](./images/prometheus_dash.png)

## Service Configuration

### Log rotation

Update options of `logger`

```shell
options:
    max-size: "100m"
    max-file: "2"
    tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```

### Memory limits

Update services to specify memory limits

```shell
deploy:
  resources:
    limits:
      memory: "512M"
```

### Metrics and healthchecks

All services are configured to provide metrics and healthchecks 