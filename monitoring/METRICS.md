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
