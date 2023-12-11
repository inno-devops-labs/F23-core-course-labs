# Services and Deployments

```shell
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app_python-7756f8df6f-7zmn9   1/1     Running   0          32m
pod/app_python-7756f8df6f-bln6d   1/1     Running   0          32m
pod/app_python-7756f8df6f-fmw80   1/1     Running   0          32m

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/app_python   ClusterIP   10.108.230.187   <none>        80/TCP    32m
service/kubernetes   ClusterIP   10.96.0.2        <none>        443/TCP   55m
```

```shell
$ minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | app_python |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/app_python has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app-python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app_python |             | http://127.0.0.1:36475 |
| default   | kubernetes |             | http://127.0.0.1:46215 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app_python in default browser...
🎉  Opening service default/kubernetes in default browser...

```

![python.png](img/python.png)

# Ingress

```shell
$ curl --resolve "apps.info:80:$( minikube ip )" -i http://apps.info/python
{"time":"2023-10-31 14:19:12"}
```