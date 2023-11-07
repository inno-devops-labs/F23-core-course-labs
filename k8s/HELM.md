# Before configuring hooks
```shell
$ kubectl get pods,svc
NAME                                              READY   STATUS    RESTARTS   AGE
pod/app-js-helm-1699366018-645c9c59c4-p66k5       1/1     Running   0          60s
pod/app-python-helm-1699365820-6d54cbcf5d-gnf9z   1/1     Running   0          4m18s

NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-js-helm-1699366018       ClusterIP   10.105.109.200   <none>        3000/TCP   60s
service/app-python-helm-1699365820   ClusterIP   10.101.74.116    <none>        8000/TCP   4m18s
service/kubernetes                   ClusterIP   10.96.0.1        <none>        443/TCP    6m37s
```

# After configuring hooks 
### (auto-delete on successful completion)
```shell
$ kubectl get pods,svc
NAME                                             READY   STATUS    RESTARTS   AGE
pod/app-js-app-js-helm-59c79c9fc9-v95rs          1/1     Running   0          2m23s
pod/app-js-app-js-helm-statefulset-0             1/1     Running   0          2m23s
pod/app-python-app-python-helm-98fcc588c-m6vk9   1/1     Running   0          21s
pod/app-python-app-python-helm-statefulset-0     1/1     Running   0          21s

NAME                                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/app-js-app-js-helm           ClusterIP   10.108.113.139   <none>        3000/TCP   2m23s
service/app-python-app-python-helm   ClusterIP   10.109.42.5      <none>        8000/TCP   21s
service/kubernetes                   ClusterIP   10.96.0.1        <none>        443/TCP    17m
```

```shell
$ kubectl get po
NAME                                          READY   STATUS    RESTARTS   AGE
app-js-app-js-helm-59c79c9fc9-v95rs           1/1     Running   0          16m
app-js-app-js-helm-statefulset-0              1/1     Running   0          16m
app-js-libchart-app-js-helm-7fc5b697c-kmsd9   1/1     Running   0          70s
app-js-libchart-app-js-helm-statefulset-0     1/1     Running   0          70s
app-python-app-python-helm-98fcc588c-m6vk9    1/1     Running   0          14m
app-python-app-python-helm-statefulset-0      1/1     Running   0          14m
```

```shell
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.58.2
Start Time:       Tue, 07 Nov 2023 17:35:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
Status:           Running
IP:               10.244.0.51
IPs:
  IP:  10.244.0.51
Containers:
  pre-install-container:
    Container ID:  docker://86f7d94fea86bee3b422d7a34bca78934f57853c6d8efc1f448a3ad6cf7a4c16
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Running
      Started:      Tue, 07 Nov 2023 17:35:15 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xxp4d (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kube-api-access-xxp4d:
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
  Normal  Scheduled  11s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     11s   kubelet            Container image "busybox" already present on machine
  Normal  Created    11s   kubelet            Created container pre-install-container
  Normal  Started    10s   kubelet            Started container pre-install-container
```

```shell
$ kubectl describe po postinstall-hook 
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.58.2
Start Time:       Tue, 07 Nov 2023 17:35:37 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
Status:           Running
IP:               10.244.0.53
IPs:
  IP:  10.244.0.53
Containers:
  post-install-container:
    Container ID:  docker://09116a667e06d7b1fdea49a337e933ed64884722a850e4ed8d352003d05c52ca
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Running
      Started:      Tue, 07 Nov 2023 17:35:40 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mpr6c (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kube-api-access-mpr6c:
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
  Normal  Scheduled  14s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    13s   kubelet            Pulling image "busybox"
  Normal  Pulled     11s   kubelet            Successfully pulled image "busybox" in 1.920175859s (1.920200359s including waiting)
  Normal  Created    11s   kubelet            Created container post-install-container
  Normal  Started    11s   kubelet            Started container post-install-container
```