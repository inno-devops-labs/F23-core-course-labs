# Monitoring


## Overview of the system

- `grafana/promtail:2.9.0:` 
    - Promtail is a log shipper specifically designed to work with Grafana Loki, which is a log aggregation system. Promtail is responsible for collecting log entries from various log files and streams, parsing them, and then forwarding them to Loki for storage and analysis. In a containerized environment, it's often used to scrape logs from containers and send them to Loki for centralized log management. 
    - It helps in gathering log data from different containers, making it easier to troubleshoot and analyze application issues and performance problems. You can also use Grafana to create dashboards and visualizations based on the log data from Loki.

- `grafana/loki:2.9.0`:
    - Loki is another open-source project, often used in conjunction with Grafana and Prometheus for log aggregation and querying. The container with this image runs Loki, which is designed to store and query log data efficiently and cost-effectively.
    - Loki works in tandem with Promtail to scrape and store log data efficiently. It provides a query language that allows users to search, filter, and extract relevant log data for troubleshooting and analysis. Loki's data can be visualized in Grafana, making it easier to correlate log events with other performance and infrastructure data

- `grafana/grafana:10.0.5`
    - The container with this image runs Grafana, and its primary role is to provide a centralized dashboard and visualization system for monitoring various data sources, including data from Prometheus, Loki and more.
    - Grafana allows users to create customizable dashboards and panels to visualize data from different sources. It supports various data source integrations, making it an essential tool for creating informative and real-time dashboards for performance monitoring, log analysis, and data visualization


---

- Additionally, prometheus with nodeexporter were set up

- `prom/prometheus:v2.47.0`
    - Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability.
    - Scraping Metrics: Prometheus periodically scrapes metrics from various targets, such as applications, services, and infrastructure components. It uses target-specific configurations to collect data, including custom metrics and system-level metrics.
    - Data Storage: Prometheus stores the scraped metrics in a local time-series database. This time-series data can be queried and analyzed to monitor the performance and health of systems and applications over time.
    - Alerting: Prometheus also supports alerting rules, allowing you to define custom alert conditions based on the collected metrics. When a defined alert condition is met, Prometheus can trigger alerts, which can be forwarded to alert managers or notification systems.
    - Service Discovery: Prometheus supports various service discovery mechanisms, making it suitable for dynamic environments like container orchestration platforms. It can automatically discover and scrape targets as they come and go.

- `prom/node-exporter:v1.6.1`
    - Node Exporter is a Prometheus exporter for collecting various system and hardware metrics from a host machine. It exposes system-level information such as CPU usage, memory usage, disk space, network activity, and more as Prometheus metrics.
    Node Exporter is typically installed on each host or node in a cluster and allows Prometheus to scrape and store system-level data. This data can be used to monitor the health and performance of the underlying infrastructure, helping you identify resource bottlenecks, troubleshoot issues, and ensure the overall stability of your containerized applications.


## 1. Loki

- After starting containers we can check loki status in order to verify that it's ready
using `/ready` route 
    - ![Loki Ready](/assets/screenshots/loki_ready.png)


- We can verify that loki has obtained initial metrics by checking `/metrics` route
    - ![](/assets/screenshots/2023-10-17-22-11-30.png)

## 2. Grafana



https://github.com/grafana/loki/blob/main/production/docker-compose.yaml
https://github.com/haenno/traefik-docker-compose-grafana-prometheus-loki-promtail-portainer/tree/main   



- ![](/assets/screenshots/2023-10-17-22-13-07.png)

- We can find Loki data source in the:
    - Home -> Administration -> Data sources
    - ![](/assets/screenshots/2023-10-17-22-15-40.png)

- We can ensure that current data source is set to Loki in the `Explore` tab
    - ![](/assets/screenshots/2023-10-17-22-16-36.png)
    
- Then, we can perform a query using LogQL. From the initial configuraiton we have `dockerlogs` job
    - Example query for errors
    - ![](/assets/screenshots/2023-10-17-22-23-44.png)


## 3. Logs from applications


### 3.1 app_python

- Ensure that the application is launched behind Traefik proxy
    - ![](/assets/screenshots/2023-10-17-22-52-31.png)

- Ensure that logs from container are displaying appropriately.
    - ![](/assets/screenshots/2023-10-17-23-26-51.png)

### 3.2 app_go

- Ensure that logs from container are displaying appropriately.
    - P.S. Since the `app_go` is responsible for performing redirects, 
    there is no purpose in showing it's screenshot explicitly
    - ![](/assets/screenshots/2023-10-18-01-19-50.png)

## 4. Prometheus


- Exported series can be viewed in the dedicated tab from the Explorer
    - For example, simple query for the traefik 
    - ![](/assets/screenshots/2023-10-17-23-34-45.png)

