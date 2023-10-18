# Task 1

1. Did

2. Added Loki as data source to Grafana.

# Task 2

Additionally following these tutorials:

* https://medium.com/@gpiechnik/loki-effective-logging-and-log-aggregation-with-grafana-c3356e7f13ad
* https://stackoverflow.com/questions/71516943/promtail-service-discovery-based-on-label-with-docker-compose-and-label-in-gra

1. **Promtail** - Combines and pushes app logs to loki, it's a 'client' of this setup. Multiple Promtail agents can run on a single machine, collecting and forwarding logs. \\
   **Loki** - Loki stores and processes logs, it's a 'backend' of this logging setup. \\
   **Grafana** - This component is used to interact with Loki. Grafana queries Loki to perform filtering and select the desired results from the logs. These data can then be visualized as charts or other graphics.

2. ![Alt text](image.png)
