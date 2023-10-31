# Services and Deployments

```shell
kubectl get pods,svc
```

```text
NAME                             READY   STATUS             RESTARTS       AGE
pod/hello-node-d5bc6d557-jvxpx   0/1     CrashLoopBackOff   14 (72s ago)   53m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/hello-node   LoadBalancer   10.106.209.91   <pending>     8080:31534/TCP   52m
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          92m
```

```shell
minikube service --all
```shell

```text
|-----------|------------|-------------|-----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |             URL             |
|-----------|------------|-------------|-----------------------------|
| default   | hello-node |        8080 | http://172.28.208.251:31534 |
|-----------|------------|-------------|-----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
* service default/kubernetes has no node port
* Opening service default/hello-node in default browser...
```