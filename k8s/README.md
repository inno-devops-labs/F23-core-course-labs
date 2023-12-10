* > kubectl get pods
```
NAME                          READY   STATUS    RESTARTS   AGE
devops-lab-68f5758947-lb7zh   1/1     Running   0          6m37s
```

* > kubectl get svc
```
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
devops-lab   LoadBalancer   10.105.133.251   <pending>     8000:30934/TCP   2m57s
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          9m34s
```