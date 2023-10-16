## Logging stack

### Promtail
Used to collect logs from containers and send them to Loki.
Labels are used to extract information about the container from the log tag.
Configuration file: `configs/promtail.yml`

### Loki
Used to store logs from Promtail and provide a query interface.
Loki uses its default configuration file.
![grafana_data_sources](img/grafana_data_sources.png)

### Grafana
Used to query and visualize logs from Loki.
Configuration file: `configs/grafana-datasources.yml`
Promtail, Loki and Grafana are configured to use the same network, so they can communicate with each other by service name.
![grafana_label_filters](img/grafana_label_filters.png)

## Application logs
Both Python and Golang app's logs are sent to stdout and collected by Promtail.
All containers, including logging stack, are configured to use the same logging driver, so the same labels are used for all containers.
```yaml
logging: &default-logging
  driver: "json-file"
  options:
    tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
```
Here is the examples of queries in Grafana for Golang and Python apps:
![app_go_query](img/app_go_query.png)
![app_go_result](img/app_go_result.png)
![app_python_query](img/app_python_query.png)
![app_python_result](img/app_python_result.png)

#### References
Parts of the docker-compose.yml reused from proposed resources:
https://github.com/grafana/loki/blob/main/production/
https://gist.github.com/ruanbekker/c6fa9bc6882e6f324b4319c5e3622460
