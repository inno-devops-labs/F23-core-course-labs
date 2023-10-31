```bash
➜ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-6f6bd85f9-xd7ph   1/1     Running   0          11m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
service/app-python   LoadBalancer   10.108.229.12   10.108.229.12   80:31829/TCP   3m22s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP        16m
```