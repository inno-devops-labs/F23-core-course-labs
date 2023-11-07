## Before adding hooks:

### `kubectl get pods,svc`

```shell
NAME                                              READY   STATUS    RESTARTS   AGE
pod/app-python-helm-1699348937-6f7db94555-t8mnx   1/1     Running   0          17m

NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python-helm-1699348937   ClusterIP   10.110.155.199   <none>        80/TCP         17m
service/kubernetes                   ClusterIP   10.96.0.1        <none>        443/TCP        6d11h
```

## After adding hooks with no delete policy:

### `kubectl get pods,svc`
```shell
NAME                                              READY   STATUS      RESTARTS   AGE
pod/helm-hooks-app-python-helm-5786b5d599-979gc   1/1     Running     0          98s
pod/postinstall-hook                              0/1     Completed   0          97s
pod/preinstall-hook                               0/1     Completed   0          2m1s

NAME                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/helm-hooks-app-python-helm   ClusterIP   10.109.204.73   <none>        80/TCP    98s
service/kubernetes                   ClusterIP   10.96.0.1       <none>        443/TCP   6d12h
```

### `kubectl get po`
```shell
NAME                                          READY   STATUS    RESTARTS   AGE
app-python-5d95765f48-dx8c9                   1/1     Running   0          73m
app-python-5d95765f48-mn26w                   1/1     Running   0          73m
app-python-5d95765f48-tf7bb                   1/1     Running   0          73m
helm-hooks-app-python-helm-5786b5d599-jwfmd   1/1     Running   0          49s
```

### `kubectl describe po preinstall-hook`
```shell
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.64.2
Start Time:       Tue, 07 Nov 2023 13:27:50 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.66
IPs:
  IP:  10.244.0.66
Containers:
  pre-install-container:
    Container ID:  docker://e462fa53c203ded2b7922a12d4ec1b51f275668ee5de4f77cf6135171d1c57e6
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
      Started:      Tue, 07 Nov 2023 13:27:51 +0300
      Finished:     Tue, 07 Nov 2023 13:28:11 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jlzww (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-jlzww:
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
  Normal  Scheduled  82s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     81s   kubelet            Container image "busybox" already present on machine
  Normal  Created    81s   kubelet            Created container pre-install-container
  Normal  Started    81s   kubelet            Started container pre-install-container
```

### `kubectl describe po postinstall-hook`
```shell
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.64.2
Start Time:       Tue, 07 Nov 2023 13:28:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.67
IPs:
  IP:  10.244.0.67
Containers:
  post-install-container:
    Container ID:  docker://62cb4f49d439381aa8b9ad504c421d2b1cae6fbe6993abb8e3284dea6cb10230
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
      Started:      Tue, 07 Nov 2023 13:28:17 +0300
      Finished:     Tue, 07 Nov 2023 13:28:37 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fz9j5 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-fz9j5:
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
  Normal  Scheduled  65s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    64s   kubelet            Pulling image "busybox"
  Normal  Pulled     62s   kubelet            Successfully pulled image "busybox" in 1.53989089s (1.539984922s including waiting)
  Normal  Created    62s   kubelet            Created container post-install-container
  Normal  Started    62s   kubelet            Started container post-install-container
```

## After adding pods with the delete policy

### `kubectl get pods,svc`
```shell
NAME                                              READY   STATUS    RESTARTS   AGE
pod/helm-hooks-app-python-helm-5786b5d599-4jzwj   1/1     Running   0          57s

NAME                                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/helm-hooks-app-python-helm   ClusterIP   10.96.21.166   <none>        80/TCP    57s
service/kubernetes                   ClusterIP   10.96.0.1      <none>        443/TCP   6d12h
```