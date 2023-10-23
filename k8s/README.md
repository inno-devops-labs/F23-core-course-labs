## K8s

### Pods and services

```shell
maruf@lenovo~$ kubectl get pods,svc


NAME                                         READY   STATUS    RESTARTS   AGE
pod/python-app-deployment-7df86476d7-4kbft   1/1     Running   0          36m
pod/python-app-deployment-7df86476d7-cr49q   1/1     Running   0          36m
pod/python-app-deployment-7df86476d7-d2qvh   1/1     Running   0          36m

NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/python-app-service   ClusterIP      10.109.136.225   <pending>     5000/TCP         15m
service/kubernetes           ClusterIP      10.96.0.1        <none>        443/TCP          137m
```

### minikube service

```shell
maruf@lenovo~$ minikube service --all

|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------------|-------------|--------------|
| NAMESPACE |      NAME          | TARGET PORT |     URL      |
|-----------|--------------------|-------------|--------------|
| default   | python-app-service |             | No node port |
|-----------|--------------------|-------------|--------------|
😿  service default/python-app-service has no node port
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service python-app-service.
|-----------|--------------------|-------------|------------------------|
| NAMESPACE |      NAME          | TARGET PORT |          URL           |
|-----------|--------------------|-------------|------------------------|
| default   | kubernetes         |             | http://127.0.0.1:59661 |
| default   | python-app-service |             | http://127.0.0.1:59665 |
|-----------|--------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/python-app-service in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
^C✋  Stopping tunnel for service python-app-service.
✋  Stopped tunnel for service kubernetes.

```

### Clean up

```shell
maruf@lenovo~$ kubectl delete deployments --all
deployment.apps "python-app-deployment" deleted

maruf@lenovo~$ kubectl delete all --all --namespace default
service "python-app-service" deleted
service "kubernetes" deleted
```
