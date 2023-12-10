# Metrics

## Prometheus Targets:

![prometheus](images/prometheus_targets.png)

## Grafana Dashboards:

![prometheus](images/prometheus_dashboard.png)
![loki](images/loki_dashboard.png)

## Service Configuration Updates:

- Log rotation:

```yaml
logging:
  driver: "json-file"
  options:
    tag: "{{.ImageName}}|{{.Name}}"
    max-size: "1k"
    max-file: "3"
```

- Memory limits:

```yaml
deploy:
  resources:
  limits:
    memory: 100M
```

## Application Metrics

Thanks to FastAPI they done in one line

```python
Instrumentator().instrument(app).expose(app)
```

![app_python](images/app_python_target.png)
