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
    - ![](/assets/screenshots/2023-11-05-16-04-56.png)


## Task 2: Helm Chart Hooks


```
helm lint app-python
```

![](/assets/screenshots/2023-11-06-02-31-50.png)



- Output of `helm install --dry-run helm-hooks app-python`:

```yml
# ... (trimmed)
# Source: app-python/templates/post-install-job.yml
apiVersion: batch/v1
kind: Job
metadata:
  name: post-install-hook-runner
  labels:
    app.kubernetes.io/managed-by: "Helm"
    app.kubernetes.io/instance: "helm-hooks"
    app.kubernetes.io/version: 1.16.0
    helm.sh/chart: "app-python-0.1.0"
  annotations:
    # This is what defines this resource as a hook. Without this line, the
    # job is considered part of the release.
    "helm.sh/hook": post-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    metadata:
      name: helm-hooks
      labels:
        app.kubernetes.io/managed-by: "Helm"
        app.kubernetes.io/instance: "helm-hooks"
        helm.sh/chart: "app-python-0.1.0"
    spec:
      restartPolicy: Never
      containers:
      - name: post-install-job
        image: "alpine:3.3"
        command: ["/bin/sleep","30"]
---
# Source: app-python/templates/pre-install-job.yml
apiVersion: batch/v1
kind: Job
metadata:
  name: pre-install-hook-runner
  labels:
    app.kubernetes.io/managed-by: "Helm"
    app.kubernetes.io/instance: "helm-hooks"
    app.kubernetes.io/version: 1.16.0
    helm.sh/chart: "app-python-0.1.0"
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    metadata:
      name: helm-hooks
      labels:
        app.kubernetes.io/managed-by: "Helm"
        app.kubernetes.io/instance: "helm-hooks"
        helm.sh/chart: "app-python-0.1.0"
    spec:
      restartPolicy: Never
      containers:
      - name: pre-install-job
        image: "alpine:3.3"
        command: ["/bin/sleep","30"]
MANIFEST:
# ...
```


- Perform hooks installation
```
helm install helm-hooks app-python
```

- Verify that sleeping pods are launched via `kubectl get pod`

![](/assets/screenshots/2023-11-06-03-12-14.png)



- Get detailed information about hook pods
```
kubectl describe post-install-<hook-id>
kubectl describe pre-install-<hook-id>
```


Note that ID of the pre-install-hook is different since screenshot was made at other run
![](/assets/screenshots/2023-11-06-03-07-49.png)

![](/assets/screenshots/2023-11-06-03-09-57.png)


## Bonus