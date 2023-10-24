# Prometheus setup
![img_9.png](img_9.png)
this screenshot shows that I have configured metric collection for all services

# Prometheus dashboard
![img_7.png](img_7.png)

# Loki dashboard
![img_8.png](img_8.png)

# Logging mechanism
 For logging rotation I have added:
 ```
    options:
      max-size: '50m'
      max-file: '2'
```

# Limitation mechanism
 For limitation of containers sources I have created:
 ```
     deploy: &limiter
      resources:
        limits:
          memory: 200M
 ```

# Healthchecks
![img_10.png](img_10.png)

# Applications metrics
## app_python
![img_11.png](img_11.png)

## app_cplusplus
![img_12.png](img_12.png)