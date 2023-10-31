
## Services and Deployments

```shell
$ kubectl get pods,svc

NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-55894c5d84-5tt9p   1/1     Running   0          14m

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          32m
service/python-app   LoadBalancer   10.107.100.198   <pending>     8081:32205/TCP   3m37s

```

```shell
$ minikube service --all 

|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app |        8081 | http://192.168.49.2:32205 |
|-----------|------------|-------------|---------------------------|
🎉  Opening service default/python-app in default browser...

```