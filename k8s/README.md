# Kubernetes

Kubernetes is open source software that automates the deployment, 
scaling, and coordination of containerized applications in a cluster. 
Supports key containerization technologies such as Docker, rkt, and hardware virtualization technologies.

## Get

### Task1

`$ kubectl get pods,svc`

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-77bb7859c-xwvt4   1/1     Running   0          49s

NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.101.64.86  <pending>     5000:30499/TCP   9s
service/kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP          6m49s
```
### Task2

`$ kubectl get pods,svc`

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5b78b4948d-brqr4   1/1     Running   0          32s
pod/app-python-5b78b4948d-twt6z   1/1     Running   0          32s
pod/app-python-5b78b4948d-s6b62   1/1     Running   0          32s

NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   LoadBalancer   10.107.68.97     <pending>     5000:30363/TCP   3s
service/kubernetes           ClusterIP      10.96.0.1        <none>        443/TCP          6m27s
```

## Minikube

`$ minikube service --all`

```
|-----------|------------|-------------|---------------------------| 
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        5000 | http://192.168.49.2:30445 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
* Starting tunnel for service app-python.
* Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:34345 |
| default   | kubernetes |             | http://127.0.0.1:35343 |
|-----------|------------|-------------|------------------------|
* Opening service default/app-python in default browser...
* Opening service default/kubernetes in default browser...
```

## Ingress

`$ kubectl get ingress`

```
NAME      CLASS    HOSTS        ADDRESS        PORTS   AGE
ingress   nginx    *            192.168.49.2   80      4m7s
```