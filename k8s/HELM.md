# Helm

## Task 1: Helm Setup and Chart Creation

- Add a helm repository

```
helm repo add bitnami https://charts.bitnami.com/bitnami
```


- Create a chart for the app_python


```
helm create app_python
```

helm install app-python-chart app-python --values app-python/values.yaml

 helm upgrade app-python-chart app-python -f app-python/values.yaml



- Verify that application is working on workloads page
    - ![](/assets/screenshots/2023-11-05-16-04-00.png)
- List entities