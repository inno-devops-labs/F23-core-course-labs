# Kubernetes

Azamat Shakirov B20-CS

a.shakirov@innopolis.university





---

### Kubernetes outputs:

Output of `kubectl get pods,svc`:

```bash
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6b5c8d5f94-dxtnh   1/1     Running   0          58s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.109.31.123   <pending>     5000:31215/TCP   55s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          5m24s

```



Output of `kubectl get pods,svc` with `deployment.yml` and `service.yml`:

```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-7dfd95d75-hq2zx   1/1     Running   0          22s
pod/app-python-7dfd95d75-jpkqk   1/1     Running   0          22s
pod/app-python-7dfd95d75-m9rvq   1/1     Running   0          22s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.102.10.179   <pending>     5000:30367/TCP   17s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          15m

```



Output of `minikube service --all`:

```bash
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python |        5000 | http://192.168.49.2:30367 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python in default browser...

```

Browser screenshot:

![](https://i.ibb.co/hMGhcyw/image.png)