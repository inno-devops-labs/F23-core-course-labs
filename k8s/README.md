```
linkstaple@MacBook-Pro-Michael ~ % kubectl get pods 
NAME                          READY   STATUS    RESTARTS        AGE
app-python-5b4bb5dddc-gm5fn   1/1     Running   1 (4m13s ago)   6m51s
linkstaple@MacBook-Pro-Michael ~ % kubectl get svc
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
app-python   LoadBalancer   10.107.192.205   <pending>     5555:32177/TCP   5m21s
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          8m4s
linkstaple@MacBook-Pro-Michael ~ % 
```
