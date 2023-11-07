```bash
kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-1699386294-57866b5455-tgp8f   1/1     Running   0          3m12s

NAME                            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/app-python-1699386294   ClusterIP   10.107.87.44   <none>        80/TCP    3m12s
service/kubernetes              ClusterIP   10.96.0.1      <none>        443/TCP   6d23h
```