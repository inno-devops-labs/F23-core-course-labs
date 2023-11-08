## Task 1

```bash
kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
app-python-7b8f9db449-dcpd6   1/1     Running   0          62s
```

```bash
kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
app-python   NodePort    10.103.184.118   <none>        5000:31150/TCP   84s
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          8d
```

## Task 2
```bash
kubectl get po
NAME                          READY   STATUS      RESTARTS   AGE
app-python-7b8f9db449-vgszb   1/1     Running     0          36s
post-install-hook             0/1     Completed   0          36s
pre-install-hook              0/1     Completed   0          39s
```

```bash
kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 09 Nov 2023 01:14:03 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.42
IPs:
  IP:  10.244.0.42
Containers:
  pre-install-container:
    Container ID:  docker://2b2c9f87f83cd13c088112040d635a7a59666a1f1317c1e90e364e51e55c6b83
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 1
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 09 Nov 2023 01:14:04 +0300
      Finished:     Thu, 09 Nov 2023 01:14:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rqfk6 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-rqfk6:
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
  Normal  Scheduled  108s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     108s  kubelet            Container image "busybox" already present on machine
  Normal  Created    108s  kubelet            Created container pre-install-container
  Normal  Started    108s  kubelet            Started container pre-install-container
```

```bash
kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Thu, 09 Nov 2023 01:14:06 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.43
IPs:
  IP:  10.244.0.43
Containers:
  post-install-container:
    Container ID:  docker://32c1c6a4fbc74a4e9b3d88eb9cfdb958bc2347b29132284291415e49349823f3
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Thu, 09 Nov 2023 01:14:20 +0300
      Finished:     Thu, 09 Nov 2023 01:14:35 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-czh28 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-czh28:
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
  Normal  Scheduled  2m16s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    2m16s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m4s   kubelet            Successfully pulled image "busybox" in 2.289335918s (12.559444881s including waiting)
  Normal  Created    2m4s   kubelet            Created container post-install-container
  Normal  Started    2m3s   kubelet            Started container post-install-container
```

