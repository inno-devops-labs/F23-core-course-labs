# Helm

## Report of pods and services (Task 1)

```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-77d599594-n6mqh   1/1     Running   0          94s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.99.65.158   <none>        8080:31441/TCP   94s
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          26m
```

## Report of preinstall and posinstall pods

### `kubectl get po`

```bash
NAME                         READY   STATUS      RESTARTS   AGE
app-python-77d599594-k9wjx   1/1     Running     0          23s
postinstall-hook             0/1     Completed   0          23s
preinstall-hook              0/1     Completed   0          28s
```

### `kubectl describe po preinstall-hook`

```yaml
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 11 Nov 2023 21:38:56 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  docker://6d8d3e7450ffcd421378cef1452c8293d4fccbfa84c08e339b995e49bdf3c039
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 3
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 11 Nov 2023 21:38:56 +0300
      Finished:     Sat, 11 Nov 2023 21:38:59 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-9v7lh (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-9v7lh:
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
  Normal  Scheduled  77s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     77s   kubelet            Container image "busybox" already present on machine
  Normal  Created    77s   kubelet            Created container pre-install-container
  Normal  Started    77s   kubelet            Started container pre-install-container
```

### `kubectl describe po postinstall-hook`

```yaml
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 11 Nov 2023 21:39:01 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  post-install-container:
    Container ID:  docker://bf275af6734d47addb736503b7d6aea5980d6e7782bdab68413f8c45ff0f1950
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 3
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 11 Nov 2023 21:39:03 +0300
      Finished:     Sat, 11 Nov 2023 21:39:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-brrzk (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-brrzk:
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
  Normal  Scheduled  112s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    112s  kubelet            Pulling image "busybox"
  Normal  Pulled     111s  kubelet            Successfully pulled image "busybox" in 1.374s (1.374s including waiting)
  Normal  Created    111s  kubelet            Created container post-install-container
  Normal  Started    110s  kubelet            Started container post-install-container
  ```