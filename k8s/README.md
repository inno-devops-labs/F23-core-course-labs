
## Task 1
### kubectl get pods,svc
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-6c9457577c-7pckh   1/1     Running   0          38s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          52s
service/python-app   LoadBalancer   10.103.136.179   <pending>     8000:32067/TCP   17s
```
## Task 2
### kubectl get pods,svc
```
NAME                                         READY   STATUS    RESTARTS   AGE
pod/python-app-6c9457577c-blh2d              1/1     Running   0          4m56s
pod/python-app-deployment-59b9bc6d64-9sp7k   1/1     Running   0          14s
pod/python-app-deployment-59b9bc6d64-q45qq   1/1     Running   0          18s
pod/python-app-deployment-59b9bc6d64-x4mtd   1/1     Running   0          10s

NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1        <none>        443/TCP          4m8s
service/python-app-service   LoadBalancer   10.106.159.151   <pending>     8000:30769/TCP   2m47s
```
### minikube service --all
```
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|--------------------|-------------|-----------------------------|
| NAMESPACE |        NAME        | TARGET PORT |             URL             |
|-----------|--------------------|-------------|-----------------------------|
| default   | python-app-service |        8000 | http://192.168.59.100:30769 |
|-----------|--------------------|-------------|-----------------------------|
🎉  Opening service default/python-app-service in default browser...
```
