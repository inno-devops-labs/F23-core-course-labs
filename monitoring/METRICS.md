# Metrics

## Prometheus

### Targets

![Prometheus Targets](./assets/targets.png)

## Dashboards

The dashboards are created from templates provided in the lab description.

### Loki
![Loki Dashboard](./assets/loki_dashboard.png)

### Prometheus
![Prometheus Dashboard](./assets/prometheus_dashboard.png)

## Enhancements

### Log Rotation

I specified log rotation for each service in `docker-compose` file using the following code snippet:
```
logging: &logger
  driver: "json-file"
  options:
    max-size: "100m"
    tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```
Here I set tag, max size of the file (100 m) and driver type (JSON).

### Memory Limits

I defined memory limits for each service using:
```
deploy:
  resources:
    limits:
      memory: Xm
```
Where **X** in memory limit is specific for each service.

### Health Check

Health checks have different commands for each service below is an example for **app_python**:
```
healthcheck:
  test: [ "CMD-SHELL", "curl -f http://localhost:8080/health" ]
  interval: 10s
  timeout: 10s
  start_period: 10s
```
For each services I set _interval_, _timeout_ and _start_period_. In the `test` parameter I define the url.