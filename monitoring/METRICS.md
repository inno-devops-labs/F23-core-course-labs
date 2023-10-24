## The screenshot that shows configured Prometheus:

<img width="1478" alt="image" src="https://github.com/sl1depengwyn/core-course-labs/assets/53992153/7163fb3c-202e-4c1c-b615-e1a9db11b3bb">

## Dasboards screenshots:

### Prometheus: <img width="1434" alt="image" src="https://github.com/sl1depengwyn/core-course-labs/assets/53992153/9ce94411-43fe-47cd-9a94-67243771dff9">

### Loki: <img width="1478" alt="image" src="https://github.com/sl1depengwyn/core-course-labs/assets/53992153/dc7e8d8c-10f7-40f2-9741-773c57efff96">

## Service Configuration Updates:

- Log rotation is implemented by specifying the `max-size` and `max-file` options of logging with `json-file` driver.
- Memory limits are specified by adding such field to containers:

```yaml
deploy:
  resources:
    limits:
      memory: 500M
```

that limits container memory usage to 500MB

## Metrics gathering:

All containers are added to Prometheus scrape config like this:

```yaml
scrape_configs:
  - job_name: prometheus
    honor_timestamps: true
    scrape_interval: 15s
    scrape_timeout: 10s
    metrics_path: /metrics
    scheme: http
    static_configs:
      - targets:
          - localhost:9090

  - job_name: "loki"
    static_configs:
      - targets: ["loki:3100"]

  - job_name: "python"
    static_configs:
      - targets: ["app_python:80"]

  - job_name: "elixir"
    static_configs:
      - targets: ["app_elixir:4000"]

  - job_name: "promtail"
    static_configs:
      - targets: ["promtail:9080"]

  - job_name: "grafana"
    static_configs:
      - targets: ["grafana:3000"]
```

## Application Metrics:

I've used [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator) for my python app and [Prometheus.ex](https://github.com/deadtrickster/prometheus.ex) for my elixir app.



## Health Checks:

Health checks are implemented using following snippet in docker compose:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:80"]
  interval: 1m30s
  timeout: 10s
  retries: 3
  start_period: 40s
```
