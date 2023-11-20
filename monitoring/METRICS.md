# Task 1
Prometheus targets:
![targets](screenshots/prometheus-targets.png)
I added all services to targets in advace


# Task 2
#### Prometheus dashboard:
![prom-dash-1](screenshots/prom-dashboard-1.png)
![prom-dash-1](screenshots/prom-dashboard-2.png)

#### Loki dashboard:
![prom-dash-1](screenshots/loki-dashboard-1.png)
![prom-dash-1](screenshots/loki-dashboard-2.png)

### Enhance configuration
Use docker' deploy.resource.limit param and storage.tsdb.retention.time

### Metrics from all services:
![targets](screenshots/prometheus-targets.png)


# Bonus
For FastAPI it's necessary just to add 'Instrumentator().instrument(app).expose(app)'
to app initialization:
![python-target](screenshots/python-target.png)

For Kotlin it's needed to add actuator:
![kotlin-target](screenshots/kotlin+python-target.png)


## Healthy check:
### After start:
```
$ docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                            PORTS                    NAMES
4e401229dc1c   edikgoose/moscow-time-app:latest   "uvicorn src.main:ap…"   4 seconds ago    Up 3 seconds (health: starting)   0.0.0.0:8080->80/tcp     moscow-time-app
744f272cbce6   grafana/loki:2.9.1                 "/usr/bin/loki -conf…"   12 minutes ago   Up 3 seconds (health: starting)   0.0.0.0:3100->3100/tcp   loki
32a8ca802383   grafana/grafana:latest             "/run.sh"                12 minutes ago   Up 3 seconds (health: starting)   0.0.0.0:3000->3000/tcp   grafana
4a6f427a39b8   edikgoose/base-converter:latest    "java -jar /app/base…"   12 minutes ago   Up 3 seconds (health: starting)   0.0.0.0:8081->8080/tcp   base-converter-app
3d745e124f44   grafana/promtail:2.9.1             "/usr/bin/promtail -…"   12 minutes ago   Up 3 seconds (health: starting)   0.0.0.0:9080->9080/tcp   promtail
e392c43e7085   prom/prometheus:v2.47.2            "/bin/prometheus --c…"   12 minutes ago   Up 3 seconds (health: starting)   0.0.0.0:9090->9090/tcp   prometheus
```

### After all containers start
```
$ docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED              STATUS                        PORTS                    NAMES
4e401229dc1c   edikgoose/moscow-time-app:latest   "uvicorn src.main:ap…"   About a minute ago   Up About a minute (healthy)   0.0.0.0:8080->80/tcp     moscow-time-app
744f272cbce6   grafana/loki:2.9.1                 "/usr/bin/loki -conf…"   13 minutes ago       Up About a minute (healthy)   0.0.0.0:3100->3100/tcp   loki
32a8ca802383   grafana/grafana:latest             "/run.sh"                13 minutes ago       Up About a minute (healthy)   0.0.0.0:3000->3000/tcp   grafana
4a6f427a39b8   edikgoose/base-converter:latest    "java -jar /app/base…"   13 minutes ago       Up About a minute (healthy)   0.0.0.0:8081->8080/tcp   base-converter-app
3d745e124f44   grafana/promtail:2.9.1             "/usr/bin/promtail -…"   13 minutes ago       Up About a minute (healthy)   0.0.0.0:9080->9080/tcp   promtail
e392c43e7085   prom/prometheus:v2.47.2            "/bin/prometheus --c…"   13 minutes ago       Up About a minute (healthy)   0.0.0.0:9090->9090/tcp   prometheus
```

_I needed to install curl in a container with a python application because it doesn't have curl/wget by default_