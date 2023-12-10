```
linkstaple@MacBook-Pro-Michael ~ % kubectl get pods
NAME                          READY   STATUS    RESTARTS      AGE
my-app-chart-5499cd8c-7swnd   1/1     Running   1 (77s ago)   3m9s
linkstaple@MacBook-Pro-Michael ~ % kubectl get svc
NAME           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes     ClusterIP   10.96.0.1      <none>        443/TCP   45m
my-app-chart   ClusterIP   10.111.70.68   <none>        80/TCP    3m13s
```