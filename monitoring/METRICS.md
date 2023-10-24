# Metrics 
## Prometheus targets
![targets](./images/targets1.png)
![targets](./images/targets2.png)

## Dashboards 
I've used templates proposed in the task 
### Loki
![loki](./images/loki_dashboard.png)
 ### Prometheus
![prometheus](./images/prometheus_dashboard.png)




## Service configuration updates 
### Log rotation 
```
    logging: &logging
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "2"
        tag: '{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}'
```
### Memory limits for containers
```
    deploy:
      resources:
        limits:
          memory: 256m
```
## Metrics 
All applications have /health and /metrics endpoints 

