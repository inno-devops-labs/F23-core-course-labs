# Metrics

## Prometheus & Graphana
Prometheus targets
![Targets](img/prometheus-targets.png)

Loki metrics in graphana
![Loki metrics in graphana](img/prometheus-loki.png)

Prometheus metrics in graphana
![Prometheus metrics in graphana](img/prometheus-prometheus.png)

Dashboard with promtail (you can see logging rate from all containers)
![Dashboard](img/dashboard-loki-and-prometheus.png)

Python app metrics in prometheus (starlette middleware plugin used to collect the data)
![Python app](img/prometheus-python.png)

Kotlin native app metrics in prometheus (well, it's not a metric we need, but definitely metric we deserve - mean value for each thrown dice)
![Dice stat](img/prometheus-kotlin.png)

## Memory and log rotation
For all containers except grafana I gave 0.1 of CPU and 100M of memory. For grafana I gave 0.3 and 300M because it has lots of heavy tasks

About log rotation, 10 files of 10M seems suitable in our case

## Healthcheck
For both apps healthcheck implemented using simple commands `wget` or `curl`