# Monitoring with Prometheus

Command to run docker-compose:
```
docker-compose -f docker-compose.yaml up
```

### Screenshot that confirm the successful setup:
![Targets](images/prometheus_targets.png)

To set up a dashboard we need to go to http://localhost:3000, then go to dashboards -> new -> import. Then add urls of dashboards:
https://grafana.com/grafana/dashboards/13407
https://grafana.com/grafana/dashboards/3662

Then load, choose prometheus as source and import.

### Screenshots displaying your successful dashboard configurations:
![Loki dashboard](images/loki_dashboard.png)

![Prometheus dashboard](images/prometheus_dashboard.png)

### Added log rotation mechanisms:
![Log rotation](images/log_rotation.png)

### Added memory limits for all containers:
![Memory limits](images/memory_limits.png)

## Bonus

### Integrated metrics into python app:
![Python metrics](images/metrics_python_code.png)
![Python metrics](images/python_metrics.png)

### Integrated metrics into javascript app:
![Javascript metrics](images/metrics_javascript_code.png)
![Javascript metrics](images/javascript_metrics.png)



### Added healthchecks to docker containers (in my apps they are already inside from  previous labs, for new ones created healthchecks in docker-compose.yml):
![Healthchecks](images/healthchecks.png)