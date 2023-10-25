# 1. Prometheus setup


## Prometheus base targets
 ![](prometheus_base_targets.png)

## Promethesus application targets

![](prometheus_app_targets.png)


---

# 2. Grafana dashboards

##  Dashboard for loki


![](loki_dashboard_2.png)

![](loki_dashboard_1.png)

---

## Dashboard for prometheus


![](prometheus_dashboard_2.png)

![](prometheus_dashboard_1.png)


Targets sync with applications included
![](prometheus_dashboard_apps.png)

# 3. Resources limits 

## Log rotation

The log rotation configuration has a maximum log file size of "10M" and a maximum number of retained log files of "7," is a reasonable choice for many scenarios. This configuration helps balance the storage requirements for log files while ensuring a reasonable history of logs.

However, the appropriateness of these settings can also depend on specific use cases and available storage resources.

## Memory limits


- `traefik`: 50MB - Traefik is a lightweight reverse proxy and load balancer, and for testing purposes without a heavy load, a small memory limit should suffice.

- `grafana`: 150MB - Grafana is a dashboard and visualization tool. Allocating a bit more memory allows for smoother rendering and better user experience during testing.

- `loki`: 100MB - Loki is a log aggregation system. A moderate memory limit should be sufficient to collect and manage logs in a testing environment.

- `prometheus`: 200MB - Prometheus is a monitoring system. Allotting extra memory ensures it can handle basic metrics and scraping operations efficiently in a testing environment.

- `node-exporter`: 50MB - Node Exporter is a lightweight service that collects system-level metrics. Since it's not resource-intensive, a small memory limit is adequate.

- `promtail`: 100MB - Promtail is used for log collection. A moderate memory limit allows it to efficiently collect and forward logs to Loki during testing.

- `app_python` and `app_go`: 20MB each - Since these are simple apps displaying the time, a minimal memory limit should be more than enough to run them smoothly for testing purposes.

These memory limits are estimated based on the assumption that these containers in a testing environment with minimal load. Adjustments may be necessary depending on the available resources on host machine.

## 4. Application metrics

In our testing environment, application metrics are exported via the /metrics route for Prometheus, allowing us to monitor and analyze performance. Note that in production this route should not be exposed.

## app_python metrics
![](app_python_metrics.png)


## app_go metrics
![](app_go_metrics.png)