# Kubernetes

## Task 1

```
minikube start --driver=docker
```

```
😄  minikube v1.31.2 on Microsoft Windows 10 Home Single Language 10.0.19045.3570 Build 19045.3570
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🤷  docker "minikube" container is missing, will recreate.
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.27.4 on Docker 24.0.4 ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

```
kubectl create deployment python-app --image=wareverdud/lab3:latest
```

```
deployment.apps/python-app created
```

```
kubectl get deployments
```

```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
python-app   0/1     1            0           10s
```

```
kubectl expose deployment python-app --type=LoadBalancer --port=8000
```

```
service/python-app exposed
```

```
kubectl get pods
```

```
NAME                          READY   STATUS    RESTARTS   AGE
python-app-6658f7659d-xt4jx   1/1     Running   0          51s
```

```
kubectl get svc
```

```
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          75s
python-app   LoadBalancer   10.106.237.160   <pending>     8000:32170/TCP   41s
```

```
minikube service --all
```

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        8000 | http://192.168.49.2:32170 |
|-----------|------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:53022 |
| default   | python-app |             | http://127.0.0.1:53023 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/python-app in default browser...
```

![Task 1](img/1.png)

## Task 2

```
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```

```
deployment.apps/deployment created
service/service created
```

```
kubectl get pods,svc
```

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/deployment-74d8586bd5-flvll   1/1     Running   0          37s
pod/deployment-74d8586bd5-j62tp   1/1     Running   0          37s
pod/deployment-74d8586bd5-xt7lp   1/1     Running   0          37s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          75s
service/service      LoadBalancer   10.104.237.163   <pending>     8000:31292/TCP   21s
```

```
minikube service --all
```

```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
|-----------|---------|-------------|---------------------------|
| NAMESPACE |  NAME   | TARGET PORT |            URL            |
|-----------|---------|-------------|---------------------------|
| default   | service |        8000 | http://192.168.49.2:31292 |
|-----------|---------|-------------|---------------------------|
* Starting tunnel for service kubernetes.
* Starting tunnel for service service.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | kubernetes |             | http://127.0.0.1:52837 |
| default   | service    |             | http://127.0.0.1:52838 |
|-----------|------------|-------------|------------------------|
* Opening service default/kubernetes in default browser...
* Opening service default/service in default browser...
```

![Task 2](img/2.png)