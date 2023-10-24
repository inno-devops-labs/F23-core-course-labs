## 1.
![image](https://github.com/nikitosing/core-course-labs/assets/32202610/9ec89723-4406-4a8b-8258-80e947ce1598)

## 2. 
Prometheus

![image](https://github.com/nikitosing/core-course-labs/assets/32202610/029f1927-d7fb-4449-9266-ff389eb0f332)

loki:

![image](https://github.com/nikitosing/core-course-labs/assets/32202610/2c62bf33-2553-4373-9fc6-28115e749d5f)


## Bonus:

![image](https://github.com/nikitosing/core-course-labs/assets/32202610/020c3c18-15f4-4d02-b852-b1dbe58c0f38)


![image](https://github.com/nikitosing/core-course-labs/assets/32202610/ff4742e9-b9c5-4f62-844d-bbf10b4a4e70)


![image](https://github.com/nikitosing/core-course-labs/assets/32202610/91dbc6e1-858c-431c-9d37-11af79c359ff)


### Health Checks

Enhanced the service configurations in the `docker-compose.yml` file by adding health checks for the containers. Health checks ensure that the containers are running and responding as expected.

Here are the service configurations with added health checks:

```yaml
services:
  app_python:
    # ... (previous configuration)
    healthcheck:
      test: "curl -f http://localhost/ || exit 1" 
      interval: 30s
      timeout: 10s
      retries: 3

  app_elixir:
    # ... (previous configuration)
    healthcheck:
      test: "curl -f http://localhost:4000/time || exit 1"
      interval: 30s
      timeout: 10s
      retries: 3
```

### prometheus

For python simple total requests counter metric

For elixir: comprehensive prometheus metrics