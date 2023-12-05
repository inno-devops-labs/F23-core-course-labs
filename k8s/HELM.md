# Helm 

```shell
$ kubectl get pods,svc

NAME                             READY   STATUS             RESTARTS       AGE
pod/app-go-8666b999c9-94tpt      0/1     Running            7 (3m7s ago)   7m28s
pod/app-python-964d5d6cf-7hcbc   0/1     CrashLoopBackOff   7 (71s ago)    8m42s
pod/go-app-6f8cbb79b9-2sz46      1/1     Running            0              138m
pod/python-app-7db595cff-zhd74   1/1     Running            0              139m

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-go       ClusterIP   10.100.178.49    <none>        80/TCP     7m28s
service/app-python   ClusterIP   10.110.154.195   <none>        80/TCP     8m42s
service/go-app       ClusterIP   10.98.118.137    <none>        8081/TCP   138m
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    6d23h
service/python-app   ClusterIP   10.99.91.60      <none>        8080/TCP   138m

```

```shell
$ minikube service --all 

|-----------|--------|-------------|--------------|
| NAMESPACE |  NAME  | TARGET PORT |     URL      |
|-----------|--------|-------------|--------------|
| default   | app-go |             | No node port |
|-----------|--------|-------------|--------------|
😿  service default/app-go has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | app-python |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/app-python has no node port
|-----------|--------|-------------|--------------|
| NAMESPACE |  NAME  | TARGET PORT |     URL      |
|-----------|--------|-------------|--------------|
| default   | go-app |             | No node port |
|-----------|--------|-------------|--------------|
😿  service default/go-app has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | python-app |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/python-app has no node port

```

```shell
$ kubectl get po 

NAME                         READY   STATUS             RESTARTS       AGE
app-go-8666b999c9-94tpt      0/1     CrashLoopBackOff   6 (112s ago)   6m13s
app-python-964d5d6cf-7hcbc   0/1     Running            7 (3m6s ago)   7m27s
go-app-6f8cbb79b9-2sz46      1/1     Running            0              137m
python-app-7db595cff-zhd74   1/1     Running            0              138m


```

```shell
$ kubectl get po

NAME                         READY   STATUS             RESTARTS         AGE
app-go-8666b999c9-94tpt      0/1     CrashLoopBackOff   43 (4m44s ago)   121m
app-python-964d5d6cf-2qzqr   0/1     CrashLoopBackOff   6 (40s ago)      5m
go-app-6f8cbb79b9-2sz46      1/1     Running            0                4h12m
python-app-7db595cff-zhd74   1/1     Running            0                4h13m

$  kubectl describe po python-preinstall-hook 
Error from server (NotFound): pods "python-preinstall-hook" not found

$ kubectl describe po go-preinstall-hook
Error from server (NotFound): pods "go-preinstall-hook" not found

```
