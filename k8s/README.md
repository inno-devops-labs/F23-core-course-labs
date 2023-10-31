
## Deploy application

for ARM64 arch users: https://devopscube.com/minikube-mac

```bash
❯ docker context use default
❯ minikube start --driver=qemu --network=socket_vmnet
...
❯ kubectl create deployment app-python --image=nikitosing/app_python:arm_64
deployment.apps/app-python created
```

## Access application

```bash
❯ kubectl expose deployment app-python --type=LoadBalancer --port=80
service/app-python exposed
❯ kubectl get services

NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
app-python   LoadBalancer   10.108.217.162   <pending>     80:31735/TCP   2m59s
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        4m5s
❯ minikube service app-python
|-----------|------------|-------------|----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL             |
|-----------|------------|-------------|----------------------------|
| default   | app-python |          80 | http://192.168.105.2:31735 |
|-----------|------------|-------------|----------------------------|
🎉  Opening service default/app-python in default browser...
```

```bash
❯ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-56648f7d8f-9lg58   1/1     Running   0          5m19s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python   LoadBalancer   10.108.217.162   <pending>     80:31735/TCP   5m12s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        6m18s
```


## Task 2

```bash
❯ kubectl apply -f ./
deployment.apps/app-python-deployment created
service/python-service created
❯ kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-deployment-574b5778ff-bwt8s   1/1     Running   0          81s
pod/app-python-deployment-574b5778ff-vpxrf   1/1     Running   0          81s
pod/app-python-deployment-574b5778ff-vrqt6   1/1     Running   0          81s

NAME                     TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes       ClusterIP      10.96.0.1      <none>        443/TCP        2m39s
service/python-service   LoadBalancer   10.106.39.41   <pending>     80:32023/TCP   3s
❯  minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|----------------|-------------|----------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL             |
|-----------|----------------|-------------|----------------------------|
| default   | python-service |          80 | http://192.168.105.2:32023 |
|-----------|----------------|-------------|----------------------------|
🎉  Opening service default/python-service in default browser...
```