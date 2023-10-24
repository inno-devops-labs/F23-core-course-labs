# Metrics

Azamat Shakirov B20-CS

a.shakirov@innopolis.university



---

### Prometheus screenshot:

![](https://i.ibb.co/t8QnvDj/image.png)

### Grafana dashboards:

*Loki*

![](https://i.ibb.co/0Cycz5T/image.png)



![](https://i.ibb.co/gFBsJb4/image.png)

*Prometheus*

![](https://i.ibb.co/SxnJZgZ/image.png)



### Services Configuration:

`Log rotation mechanism:`

```yaml
x-logging: &logging
  driver: "json-file"
  options:
    tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
    max-size: "10m"
    max-file: "1"
```

`Memory limits for containers: (add line for each container)`

```yaml
mem_limit: 100M
```

