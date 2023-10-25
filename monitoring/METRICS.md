
## Prometheus metrics

![prometheus metrics](images/prometheus.png)

![dashboard](images/dashboard.png)

## Task2 
Set memory RAM limit and logging size limit on each service
```
deploy:
  resources:
    limits:
      memory: 500M

logging:
    driver: "json-file"
    options:
    max-size: "200k"
    max-file: "10"
   ```