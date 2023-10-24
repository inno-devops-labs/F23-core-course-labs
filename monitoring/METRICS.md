
### Configured prometheus targets:
![prometheus_targets.png](resources/prometheus_targets.png)

Then I also added other services to scrape metrics from:
![all_services_targets.png](resources/all_services_targets.png)


### Scraped Loki metrics:
![scraped_loki_metrics.png](resources/scraped_loki_metrics.png)


### Scraped Promtail metrics:
![scraped_prometheus_metrics.png](resources/scraped_prometheus_metrics.png)




### Loki Grafana Dashboard:
![loki_grafana_dashboard.png](resources/loki_grafana_dashboard.png)

![loki_grafana_dashboard_2.png](resources/loki_grafana_dashboard_2.png)


### Prometheus Grafana Dashboard:
![prometheus_grafana_dashboard.png](prometheus_grafana_dashboard.png)
![prometheus_grafana_dashboard_2.png](prometheus_grafana_dashboard_2.png)

## Log rotation
For log rotation I used options for docker default json-file logging driver:
```
logging:
  driver: "json-file"
  options:
    max-size: "100k"
    max-file: "10"
```
which means that docker will store all the logs in files of maximum 100KB.

## Memory limits
To limit resources for each container I used docker-compose `deploy` option:
```
deploy:
  resources:
    limits:
      memory: 100M
```
This option also supports CPU limits.

I chose different values of memory limit for different containers appropriately by their needs.
