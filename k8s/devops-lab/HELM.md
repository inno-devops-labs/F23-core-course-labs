* > kubectl get pods
```
NAME                          READY   STATUS    RESTARTS   AGE
devops-lab-7f6858b779-56wkf   1/1     Running   0          78s
```

* > kubectl get svc
```
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
devops-lab   NodePort    10.96.19.39   <none>        8000:32266/TCP   86s
kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP          40m
```