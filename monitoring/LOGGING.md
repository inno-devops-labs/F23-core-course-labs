# Logging Stack Report

## Components of the Logging Stack

### Loki

Loki is a horizontally scalable, highly available, multi-tenant log aggregation system. It collects and indexes log data from various sources and provides a query language to retrieve and analyze this data. Loki is responsible for collecting and storing log data from all the containers:

```
- Image: grafana/loki:latest
- Port: 3100
- Command: -config.file=/etc/loki/local-config.yaml
- Network: loki
- Logging Driver: json-file
- Tag Format: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```

### Promtail

Promtail is a component of Loki that tail logs from container files and sends them to Loki for indexing and storage. It works in conjunction with Loki to collect log data and enrich it with metadata:

```
- Image: grafana/promtail:latest
- Volumes:
  - ./promtail.yml:/etc/promtail/config.yml
  - /var/lib/docker/containers:/var/lib/docker/containers
- Command: -config.file=/etc/promtail/config.yml
- Network: loki
- Logging Driver: json-file
- Tag Format: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```

### Grafana

Grafana is a web-based dashboard and monitoring platform that allows you to visualize data and create alerts:

```
- Image: grafana/grafana:latest
- Port: 3000
- Environment Variables:
  - GF_PATHS_PROVISIONING=/etc/grafana/provisioning
  - GF_AUTH_ANONYMOUS_ENABLED=true
  - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
- Entrypoint: sh -euc /run.sh
- Volumes: ./grafana-datasources.yml:/etc/grafana/provisioning/datasources/datasources.yaml
- Network: loki
- Logging Driver: json-file
- Tag Format: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```

### Application Services (app_python and app_elixir)

two application services, app_python and app_elixir, which are running Python and Elixir applications, respectively. These services are responsible for generating log data that is collected by Loki and Promtail. They are configured with the following common settings:

- Image: nikitosing/app_python or nikitosing/app_elixir
- Ports: 80 (for app_python) and 4000 (for app_elixir)
- Network: loki
- Logging Driver: json-file
- Tag Format: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
- Additional Configuration (only for app_elixir):
  - Environment Variable: SECRET_KEY_BASE='WPcE2F5vjA5X3XBE+QcK7OHMiAuPovP4e62Gsl0VFxRHvu+xS2AiQWY0H3Qz6Q3O'

## Logging Flow

1. The application services (app_python and app_elixir) generate log data as they run and execute their respective applications.
2. Promtail, configured with a volume mapping to /var/lib/docker/containers, tails the log files within Docker containers.
3. Promtail uses the configuration specified in `promtail.yml` to enrich the log entries with metadata.
4. Promtail sends the enriched log entries to Loki via the network named "loki."
5. Loki stores and indexes the log data, making it available for querying and analysis.
6. Grafana provides a web-based interface for querying the log data stored in Loki, creating dashboards, and setting up alerts.


