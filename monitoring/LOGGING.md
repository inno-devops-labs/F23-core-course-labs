# Logging

## Run

`docker compose up -d --pull always`

[docker-compose.yml](File) includes Loki, Promtail, Prometheus, Grafana, and Python + Rust apps

## Using

### We can select by job

docker job

![](img/3.png)

### Python logs

app_python container name

![](img/1.png)

### Rust logs

app_rust container name

![](img/2.png)
