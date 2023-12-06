# Lab 8: Monitoring with Prometheus
## Task 1: Prometheus Setup

1. Learn About Prometheus:

- Done

2. Integration with Docker Compose:
Expand your existing docker-compose.yml file from the previous lab to include Prometheus.

- Done

3. Prometheus Configuration:

Configure Prometheus to collect metrics from both Loki and Prometheus containers.

- To do this, we will create a configuration file `prometheus.yml` and include Loki and Prometheus for scraping.

4. Verify Prometheus Targets:

Access http://localhost:9090/targets to ensure that Prometheus is correctly scraping metrics.
Capture screenshots that confirm the successful setup and place them in a file named METRICS.md within the monitoring folder.

- Here are the screenshots:

![Prometheus scraping Loki and Prometheus](https://i.imgur.com/CvswNoO.png)
![Graph](https://i.imgur.com/5zXCeDB.png)

## Task 2: Dashboard and Configuration Enhancements

1. Grafana Dashboards:

Prometheus Dashboard:
![Prometheus Grafana Dashboard](https://i.imgur.com/FHNpyP5.png)
Loki Dashboard:
![Loki Grafana Dashboard](https://i.imgur.com/Hkrn4SL.png)

2. Service Configuration Updates:
Enhance the configuration of all services in the `docker-compose.yml` file:
Add log rotation mechanisms.
Specify memory limits for containers.

- I have updated log_setup template to include log rotation.
    - Max file size: 10 MB
    - Max number of files: 3
- I have added two resource cap templates: for app and for monitoring services.
    - App resource cap: 0.1 CPU, 128 MB RAM (apps are fairly simple)
    - Monitoring resource cap: 0.5 CPU, 512 MB RAM

3. Metrics Gathering:

Extend Prometheus to gather metrics from all services defined in the `docker-compose.yml` file.

- Now we gather metrics from all the monitoring services, app_python and app_go services are yet to be modified in the bonus task (see below) to gather metrics from them:
![Prometheus for all services](https://i.imgur.com/If1EyNP.png)

## Bonus

1. Application Metrics:

    - See below

2. Obtain Application Metrics:
Configure your applications to export metrics.

- I have implemented metrics in my applications:
    1. For Python: using `prometheus_client` and `prometheus_async` modules.
    2. For Go: using `prometheus` module.

Now we can see that Prometheus gathers metrics for all the services:

![Prometheus for all services](https://i.imgur.com/IE5PDta.png)

3. METRICS.md Update:
Document your progress with the bonus tasks, including screenshots, in the `METRICS.md` file.

- Done

4. Health Checks:
Further enhance the `docker-compose.yml` file's service configurations by adding health checks for the containers.

- I have added healthcheck for app_python and app_go services.
- For app_python, it is a script that executes curl on the `/time` endpoint
- For app_go, it is a Go-built binary that performs GET request on the `/time` endpoint

Now we can see the health status:
![docker ps health status](https://i.imgur.com/JGV1ana.png)
![prometheus healthy targets](https://i.imgur.com/znjGqSx.png)