# HELM

### Task 1
#### Uploading chart to Kubernetes
```
helm install helm-app helm-app                                          
```

```
NAME: helm-app
LAST DEPLOYED: Wed Nov  8 00:24:55 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services helm-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

----
#### Listing releases of charts
```
helm ls
```

```
NAME    	NAMESPACE	REVISION	UPDATED                             	STATUS  	CHART         	APP VERSION
helm-app	default  	1       	2023-11-08 00:24:55.313736 +0300 MSK	deployed	helm-app-0.1.0	1.16.0
```


----

```
kubectl get pods,svc
```

```
NAME                              READY   STATUS    RESTARTS       AGE
pod/app-python-dbfc8f6b4-5gsbm    1/1     Running   1 (8m7s ago)   6d21h
pod/go-app-58b7c44d98-6dl5n       1/1     Running   1 (8m7s ago)   6d21h
pod/go-app-58b7c44d98-g5rl9       1/1     Running   1 (8m7s ago)   6d21h
pod/go-app-58b7c44d98-tvwhs       1/1     Running   1 (8m7s ago)   6d21h
pod/helm-app-674c8f757d-bd6fl     1/1     Running   0              98s
pod/python-app-84c9748db8-btxx8   1/1     Running   1 (8m7s ago)   6d21h
pod/python-app-84c9748db8-f2k6v   1/1     Running   1 (8m7s ago)   6d21h
pod/python-app-84c9748db8-nptck   1/1     Running   1 (8m7s ago)   6d21h

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/go-app       NodePort    10.108.176.231   <none>        9000:32732/TCP   6d21h
service/helm-app     NodePort    10.100.185.198   <none>        8000:31173/TCP   98s
service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          6d22h
service/python-app   NodePort    10.96.121.224    <none>        8000:32713/TCP   6d21h
```

----

#### Application is accessible by running the minikube service your_service_name command.

```
minikube service helm-app
```

```
|-----------|----------|-------------|---------------------------|
| NAMESPACE |   NAME   | TARGET PORT |            URL            |
|-----------|----------|-------------|---------------------------|
| default   | helm-app | http/8000   | http://192.168.49.2:31173 |
|-----------|----------|-------------|---------------------------|
🏃  Starting tunnel for service helm-app.
|-----------|----------|-------------|------------------------|
| NAMESPACE |   NAME   | TARGET PORT |          URL           |
|-----------|----------|-------------|------------------------|
| default   | helm-app |             | http://127.0.0.1:52885 |
|-----------|----------|-------------|------------------------|
🎉  Opening service default/helm-app in default browser...
```

![4](imgs/4.jpeg)