# Metrics

## Task 1

- Prometheus Targets
![Targets](screenshots/targets.png)


## Task 2

### Grafana Dashboards

- Loki
![Loki Dashboard](screenshots/dashboard_loki.png)

- Prometheus
![Prometheus Dashboard](screenshots/dashboard_prometheus.png)

### Service Configuration Updates

- Log rotation
```
x-logging: &logging
  driver: "json-file"
  options:
    max-size: "50m"
    max-file: "3"
    tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```

- Memory limits

| Name               | Size |
|--------------------|------|
| python_application | 128m |
| sharp_application  | 256m |
| loki               | 128m |
| promtail           | 128m |
| grafana            | 512m |
| prometheus         | 512m |

## Bonus task

### Dashboard

- Applications metrics
![Metrics](screenshots/all_metrics.png)

### Metrics page

- Python
![Python Metrics](screenshots/python_metrics.png)

- C#
![C# Metrics](screenshots/c_sharp_metrics.png)

### Health check
```
x-healthcheck: &healthcheck
  interval: 10s
  timeout: 5s
  retries: 5
  start_period: 5s
```

```
healthcheck:
  test: ["CMD-SHELL", "wget --quiet --spider --timeout=1 http://localhost:PORT/healthz || exit 1"]
  <<: *healthcheck
```
