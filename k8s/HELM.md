# Helm

## Task 1

kubectl get pods,svc
```
NAME                                              READY   STATUS      RESTARTS   AGE
pod/helm-hooks-app-python-helm-6fb6f55588-wn5px   1/1     Running     0          5m43s
pod/postinstall-hook                              0/1     Completed   0          5m42s
pod/preinstall-hook                               0/1     Completed   0          6m12s

NAME                                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/helm-hooks-app-python-helm   ClusterIP   10.98.222.47   <none>        5000/TCP   5m43s
service/kubernetes                   ClusterIP   10.96.0.1      <none>        443/TCP    12m
```

## Task 2

kubectl get po

```
NAME                                          READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-helm-6fb6f55588-wn5px   1/1     Running     0          113s
postinstall-hook                              0/1     Completed   0          112s
preinstall-hook                               0/1     Completed   0          2m22s
```

kubectl describe po preinstall-hook
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 23:29:45 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.84
IPs:
  IP:  10.244.0.84
Containers:
  pre-install-container:
    Container ID:  docker://c1537b2b4e06238ebc5c697a13ae97106363ad3b3942f694921d741f956654d4
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
      Started:      Wed, 08 Nov 2023 23:29:52 +0300
      Finished:     Wed, 08 Nov 2023 23:30:13 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fzbdt (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-fzbdt:
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
  Normal  Scheduled  3m36s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    3m35s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m29s  kubelet            Successfully pulled image "busybox" in 6.690728091s (6.690856181s including waiting)
  Normal  Created    3m29s  kubelet            Created container pre-install-container
  Normal  Started    3m28s  kubelet            Started container pre-install-container
```

kubectl describe po postinstall-hook
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 23:30:15 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.86
IPs:
  IP:  10.244.0.86
Containers:
  post-install-container:
    Container ID:  docker://1793f77c10b9e967b8ed3f274d6df5f9a362decbf2f4d9b902ca296c3b26d0b6
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
      Started:      Wed, 08 Nov 2023 23:30:18 +0300
      Finished:     Wed, 08 Nov 2023 23:30:38 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vsv29 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-vsv29:
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
  Normal  Scheduled  4m49s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    4m49s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m46s  kubelet            Successfully pulled image "busybox" in 2.854117025s (2.854139157s including waiting)
  Normal  Created    4m46s  kubelet            Created container post-install-container
  Normal  Started    4m46s  kubelet            Started container post-install-container
```

## Bonus

### Helm chart for bonus app

[Typescript Chart](./app-typescript-helm/)

### Library chart

[Library Chart](./library-chart/)
