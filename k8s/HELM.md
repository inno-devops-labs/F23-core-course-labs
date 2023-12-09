# Helm 

## Chart creation 

### Create helm charts

* Python app

```shell
helm create app_python
```

```shell
helm install app_python app_python/
```

Output:
```text
NAME: app_python
LAST DEPLOYED: Mon Nov  7 20:33:20 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
...
```

### Checking

```shell
minikube service --all
```

Output:
```text
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app_python | http/5000   | http://192.168.47.2:30113 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app_python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app_python |             | http://127.0.0.1:49916 |
| default   | kubernetes |             | http://127.0.0.1:49922 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app_python in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```


```shell
kubectl get pods,svc     
```

Output:
```text
NAME                              READY   STATUS    RESTARTS   AGE
pod/app_python-82c528462d-ddg6b   1/1     Running   0          24m
pod/app_python-82c528462d-jdf8z   1/1     Running   0          24m
pod/app_python-82c528462d-tjfb6   1/1     Running   0          24m
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app_python   LoadBalancer   10.109.204.17   <pending>     5000:30113/TCP   23m
service/kubernetes   ClusterIP      10.95.0.1       <none>        443/TCP          24m
```

### Installing and Describing Hooks

```shell
helm lint app_python/
```

```text
==> Linting app_python/
[INFO] Chart.yaml: icon is recommended
[WARNING] templates/deployment.yaml: object name does not conform to Kubernetes naming requirements: 
...
1 chart(s) linted, 0 chart(s) failed
```

````shell
kubectl get po
````

Output
````text
NAME                          READY   STATUS      RESTARTS   AGE
app_python-82c528462d-n5hd3   1/1     Running     0          66s
app_python-82c528462d-fj4n3   1/1     Running     0          66s
app_python-82c528462d-ng54s   1/1     Running     0          66s
python-postinstall-hook       0/1     Completed   0          66s
python-preinstall-hook        0/1     Completed   0          78s          18m
````

````shell
kubectl describe po python-preinstall-hook
````

Ouoput:
````shell
Name:         python-preinstall-hook
Namespace:    default
Priority:     0
Node:         minikube/192.168.48.2
Start Time:   Mon, 08 Nov 2023 21:44:34 +0300
Labels:       <none>
Annotations:  helm.sh/hook: pre-install
Status:       Succeeded
IP:           10.244.0.132
IPs:
  IP:  10.244.0.132
Containers:
  pre-install-container:
    Container ID:  docker://ba7e1708ee21eca1b074182ce70c6b3a42f1b200a9661563776df2aee661e41d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc63277cc4167424a6d997ff748225cf5fe2b878d4e79ac6bc977efdfe51c7
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 07 Nov 2023 21:44:14 +0300
      Finished:     Mon, 07 Nov 2023 21:44:34 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-f56b5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-f56b5:
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
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m47s  default-scheduler  Successfully assigned default/python-preinstall-hook to minikube
  Normal  Pulled     2m47s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m47s  kubelet            Created container pre-install-container
  Normal  Started    2m47s  kubelet            Started container pre-install-container
````

````shell
kubectl describe po python-postinstall-hook
````

Output
```text
Name:         python-postinstall-hook
Namespace:    default
Priority:     0
Node:         minikube/192.168.48.2
Start Time:   Mon, 07 Nov 2023 21:58:36 +0300
Labels:       <none>
Annotations:  helm.sh/hook: post-install
Status:       Succeeded
IP:           10.244.0.136
IPs:
  IP:  10.244.0.136
Containers:
  post-install-container:
    Container ID:  docker://500cc745e24d08444d3abad675f302b2bc8069b68cd87ab678a8ffd249f479cc
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc63277cc4167424a6d997ff748225cf5fe2b878d4e79ac6bc977efdfe51c7
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 07 Nov 2023 21:58:40 +0300
      Finished:     Mon, 07 Nov 2023 21:58:55 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mzr5q (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mzr5q:
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
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  5m26s  default-scheduler  Successfully assigned default/python-postinstall-hook to minikube
  Normal  Pulling    5m25s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m23s  kubelet            Successfully pulled image "busybox" in 2.096710746s (2.096723995s including waiting)
  Normal  Created    5m22s  kubelet            Created container post-install-container
  Normal  Started    5m22s  kubelet            Started container post-install-container
```

...