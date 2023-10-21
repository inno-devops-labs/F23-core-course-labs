## Logging

As the base, [Loki's GitHub Repository](https://github.com/grafana/loki) was taken, where I followed [this](https://grafana.com/docs/loki/latest/installation/docker/) tutorial. For logs monitoring `Grafana`, `Loki`, and `Promtail` configs which inspired also from the tutorial.

## Run

Use `docker-compose up` in the monitoring directory, then go to:

- http://localhost:5000 - making request to python_app
- http://localhost:3000 - checking Grafana UI

## Screenshot

![](/monitoring/screenshots/logging_grafana.png)
