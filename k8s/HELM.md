# Helm

## Task 1

```commandline
~ helm install python . --values values_python.yaml
```

```commandline
NAME: python
LAST DEPLOYED: Tue Nov  7 17:08:08 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services python-my-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```
\
&nbsp;
```commandline
~ minikube service python-my-app
```

```commandline
|-----------|---------------|-------------|---------------------------|
| NAMESPACE |     NAME      | TARGET PORT |            URL            |
|-----------|---------------|-------------|---------------------------|
| default   | python-my-app | http/8090   | http://192.168.49.2:30633 |
|-----------|---------------|-------------|---------------------------|
🏃  Starting tunnel for service python-my-app.
|-----------|---------------|-------------|------------------------|
| NAMESPACE |     NAME      | TARGET PORT |          URL           |
|-----------|---------------|-------------|------------------------|
| default   | python-my-app |             | http://127.0.0.1:57878 |
|-----------|---------------|-------------|------------------------|
```
\
&nbsp;
```commandline
~ kubectl get pods,svc
```

```commandline
NAME                                 READY   STATUS    RESTARTS        AGE
pod/python-app-5699b8b9f-559x9       1/1     Running   1 (6d18h ago)   6d18h
pod/python-app-5699b8b9f-q8f4b       1/1     Running   1 (6d18h ago)   6d18h
pod/python-app-5699b8b9f-qkvwl       1/1     Running   1 (6d18h ago)   6d18h
pod/python-my-app-866bb84449-srccw   1/1     Running   0               24m

NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP          6d19h
service/python-app      NodePort    10.96.59.58     <none>        8090:30341/TCP   6d18h
service/python-my-app   NodePort    10.101.45.107   <none>        8090:30633/TCP   24m
```
 
## Task 2

```commandline
~ helm lint my-app
```

```commandline
==> Linting my-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) faile
```
\
&nbsp;
```commandline
~ helm install helm-hooks my-app
```

```commandline
NAME: helm-hooks
LAST DEPLOYED: Tue Nov  7 17:49:59 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=my-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
\
&nbsp;
```commandline
~ kubectl get po
```

```commandline
NAME                                READY   STATUS      RESTARTS        AGE
helm-hooks-my-app-757c78787-mpc2k   1/1     Running     0               9m27s
postinstall-hook                    0/1     Completed   0               9m27s
preinstall-hook                     0/1     Completed   0               9m56s
python-app-5699b8b9f-559x9          1/1     Running     1 (6d19h ago)   6d19h
python-app-5699b8b9f-q8f4b          1/1     Running     1 (6d19h ago)   6d19h
python-app-5699b8b9f-qkvwl          1/1     Running     1 (6d19h ago)   6d19h
python-my-app-866bb84449-srccw      1/1     Running     0               51m
```
\
&nbsp;
```commandline
~ kubectl describe po preinstall-hook
```

```commandline
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 17:50:00 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.19
IPs:
  IP:  10.244.0.19
Containers:
  pre-install-container:
    Container ID:  docker://acefff02a0f3c988dea8d650e28d7b799e8d5fffc07fa736cb916fc521723c4f
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 17:50:07 +0300
      Finished:     Tue, 07 Nov 2023 17:50:27 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bfljc (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-bfljc:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  11m   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    11m   kubelet            Pulling image "busybox"
  Normal  Pulled     11m   kubelet            Successfully pulled image "busybox" in 5.093083902s (5.093858056s including waiting)
  Normal  Created    11m   kubelet            Created container pre-install-container
  Normal  Started    11m   kubelet            Started container pre-install-container
```
\
&nbsp;
```commandline
~ kubectl describe po postinstall-hook
```

```commandline
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 17:50:30 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.20
IPs:
  IP:  10.244.0.20
Containers:
  post-install-container:
    Container ID:  docker://cd94412c89859001ed176990924aef0c38ec845436c761211ac4b45ac14f5e24
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 17:50:31 +0300
      Finished:     Tue, 07 Nov 2023 17:50:51 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rmhwd (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-rmhwd:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  12m   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     12m   kubelet            Container image "busybox" already present on machine
  Normal  Created    12m   kubelet            Created container post-install-container
  Normal  Started    12m   kubelet            Started container post-install-container
```

### Hook delete policy

```commandline
"helm.sh/hook-delete-policy": hook-succeeded
```