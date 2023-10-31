```bash
➜ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-6f6bd85f9-xd7ph   1/1     Running   0          11m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
service/app-python   LoadBalancer   10.108.229.12   10.108.229.12   80:31829/TCP   3m22s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP        16m
```

## Manifests:
```bash
➜ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-6f6bd85f9-2hjx4   1/1     Running   0          28s
pod/app-python-6f6bd85f9-n5svf   1/1     Running   0          28s
pod/app-python-6f6bd85f9-q87zf   1/1     Running   0          28s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
service/app-python   LoadBalancer   10.108.229.12   10.108.229.12   80:31829/TCP   22s
service/kubernetes   ClusterIP      10.96.0.1       <none>          443/TCP        29m
```

```bash
➜ minikube service --all
|-----------|------------|-------------|----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL             |
|-----------|------------|-------------|----------------------------|
| default   | app-python |          80 | http://192.168.105.2:31829 |
|-----------|------------|-------------|----------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🎉  Opening service default/app-python in default browser...
```