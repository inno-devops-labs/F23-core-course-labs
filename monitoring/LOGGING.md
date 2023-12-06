# Logging

## Loki

Loki is a lightweight and efficient log aggregation system designed for storing and analyzing log data. 
It allows to centralize logs from various sources, search and filter logs efficiently, and gain visibility into system behavior, 
troubleshoot issues, and monitor application performance.

Loki starts at `loki:3100`.

## Promtail

Promtail is a lightweight log shipper. Promtail is needed to collect and forward log data from various sources to 
a centralized log aggregation system. It enables real-time log streaming, parsing, filtering, and 
integration with log storage solutions like Loki.

In the project Promtail has `promtail` directory with config file, starts at `promtail:9080`

## Grafana

Grafana is a powerful data visualization and monitoring tool that is widely used in various 
industries and organizations. Grafana allows to visualize and monitor data, gain insights, track system performance, 
and make data-driven decisions.

Grafana starts at `grafana:3000`.

# Best practices

## Data Source Configuration

I properly specify Loki datasource for grafana.

## Config file utilisation

I created a separate config file for Promtail and formed it according to official guide.

## Network naming

I explicitly specify name of the network for easier usage.

# Results

## Containers

![Containers](./assets/containers.png)

## Python application logs

![Python application 1](./assets/python_app-1.png)
![Python application 2](./assets/python_app-2.png)

## Loki logs

![Loki 1](./assets/loki-1.png)
![Loki 2](./assets/loki-2.png)

## Promtail logs

![Promtail 1](./assets/promtail-1.png)
![Promtail 2](./assets/promtail-2.png)

## Grafana logs

![Grafana 1](./assets/grafana-1.png)
![Grafana 2](./assets/grafana-2.png)