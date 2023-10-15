# Logging
## Graphana
Used to access the log using pretty UI.

In this case we use graphana with default options. We add Loki's datasource from compose.

## Loki
Concentrates the logs.

Used with totally default config from image

## Promtail
Brings the logs from given sources.

In this solution we keep tracking of logs with the following tags:
![Tag list](img/tags.png)

## The result
### List of containers
![Container list](img/containers.png)

### Python app logs
![Python App Logs](img/python.png)

### Kotlin Native app logs
![Kotlin Naitve App Logs](img/kotlin-native.png)

### Promtail logs
![Promtail Logs](img/promtail-logs.png)