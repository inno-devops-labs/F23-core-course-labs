# K8s README

## Service

Python:

```
kubectl --kubeconfig=kubeconfig.yaml expose deploy app-python --type=LoadBalancer
```
Check:
```
kubectl --kubeconfig=kubeconfig.yml get svc
```

#Deploy

```
kubectl --kubeconfig=kubeconfig.yml apply -f app_python/deployment.yml 
kubectl --kubeconfig=kubeconfig.yml apply -f app_go/deployment.yml
```

```
kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           22m 
```

Go:

```
kubectl --kubeconfig=kubeconfig.yaml apply -f app_go/deployment.yml 
deployment.apps/app-go-deployment created
```
```
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
app-go-deployment   3/3     3            3           5m35s
app-go-deployment   3/3     3            3           14m

NAME                                     READY   STATUS    RESTARTS   AGE
app-go-deployment-7f439281n8-vbp3s   1/1     Running   0          3m21s
app-go-deployment-7f439281n8-k5c42   1/1     Running   0          3m21s
```
Result:
```
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-go-service     |        8080 | http://192.168.49.2:30000 |
|-----------|--------------------|-------------|---------------------------|
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | app-python-service |          80 | http://192.168.49.2:31546 |
|-----------|--------------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-go-service.
🏃  Starting tunnel for service app-python-service.
🏃  Starting tunnel for service kubernetes.
```
