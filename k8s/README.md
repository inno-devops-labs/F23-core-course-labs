# K8S

## Task 1: Kubernetes Setup and Basic Deployment

Output of command `kubectl get pods`:

```output
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
app-python              1/1     1            1           56s
```

Output of command `kubectl get svc`:

```output
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          128m
app-python   NodePort    10.96.121.28    <none>        5000:31413/TCP   7m
```

## Task 2: Declarative Kubernetes Manifests

Firstly, we need to apply deployment configuration by command `kubectl apply -f app_python/deployment.yaml`:

```output
deployment.apps/app-python-deployment created
```

Output of command `kubectl get pods`:

```output
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
app-python              1/1     1            1           6m6s
app-python-deployment   3/3     3            3           59s
```

And we need to exec command `kubectl apply -f app_python/service.yml`

Output of command `kubectl get svc`:

```output
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          128m
app-python-service   NodePort    10.96.121.28    <none>        5000:31413/TCP   1m2s
```

Output of command `minikube service --all`:

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |        5000 | http://192.168.48.4:31413 |
|-----------|--------------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service app-python-service.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |        NAME        | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | kubernetes         |             | http://127.0.0.1:55480 |
| default   | app-python-service |             | http://127.0.0.1:55682 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/app-python-service in default browser...
```

And we can see that application is running:

![app-python](images/Снимок%20экрана%202023-11-01%20в%2014.49.56.png)