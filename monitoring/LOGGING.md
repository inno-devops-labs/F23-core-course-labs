# Log Management and Surveillance

## Overview

### Grafana

- Grafana, primarily a web-based application, specializes in visualization and analysis. Deployed, for instance, as a Docker container, it presents an easy-to-use interface for creating and adjusting **dashboards**. These dashboards feature various **panels** like **graphs**, **bars**, **gauges**, **charts**, etc., useful for displaying data such as **metrics** or **logs**. These data are gathered by monitoring tools like **Prometheus** or **Grafana Loki** from various systems or databases.
- Grafana also enables the creation of **alerts** and has a robust **[plugin ecosystem](https://grafana.com/grafana/plugins/)**, enhancing its features and facilitating integration with other software.

### Grafana Loki

- Similar to Prometheus but with a focus on application **logs**, Grafana Loki is a monitoring tool that collects these logs through **[clients](https://grafana.com/docs/loki/latest/clients/)**. Unlike Prometheus, it doesn't manage general metrics.
- Loki stores logs as compressed data and uses indexing methods for efficient querying, utilizing the **LogQL** language for this purpose.

### Promtail

- A key component in the Prometheus network, Promtail is dedicated to the effective gathering and forwarding of application **logs** to Grafana Loki for further analysis.
- Its adaptable and configurable nature makes it essential for improved observability, ensuring centralized log collection and storage.

## Run

Use `docker-compose up` in the monitoring directory, then go to:

- http://localhost:5000 - making request to python_app
- http://localhost:3000 - checking Grafana UI

## Screenshot

![pic1](/monitoring/pic1.png)
