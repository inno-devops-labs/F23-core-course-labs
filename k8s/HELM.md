# Helm


## kubectl get pods,svc

```
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-7fc9bd7cf7-58bkd   1/1     Running   0          7m29s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          11m
service/python-app   LoadBalancer   10.96.170.153   <pending>     8000:30009/TCP   7m29s
```

## kubectl get po

```
NAME                          READY   STATUS      RESTARTS   AGE
postinstall-hook              0/1     Completed   0          38s
preinstall-hook               0/1     Completed   0          67s
python-app-7fc9bd7cf7-4j4lf   1/1     Running     0          38s
```

## kubectl describe po postinstall-hook
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.59.101
Start Time:       Tue, 07 Nov 2023 21:04:30 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.6
IPs:
  IP:  10.244.0.6
Containers:
  post-install-container:
    Container ID:  docker://0fc6ac9b720aeed4e055a855c498bb982a12440516d6884d4f5e165d2a069644
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
      Started:      Tue, 07 Nov 2023 21:04:33 +0300
      Finished:     Tue, 07 Nov 2023 21:04:48 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-sb9bq (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-sb9bq:
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
  Normal  Scheduled  105s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    104s  kubelet            Pulling image "busybox"
  Normal  Pulled     102s  kubelet            Successfully pulled image "busybox" in 2.173373418s (2.173397523s including waiting)
  Normal  Created    102s  kubelet            Created container post-install-container
  Normal  Started    102s  kubelet            Started container post-install-container
```

## kubectl describe po preinstall-hook

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.59.101
Start Time:       Tue, 07 Nov 2023 21:04:01 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.4
IPs:
  IP:  10.244.0.4
Containers:
  pre-install-container:
    Container ID:  docker://f71d144c712db270f9ab3d4be9129f79da7b1c9374ca8544b6adb58cf955c5ac
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
      Started:      Tue, 07 Nov 2023 21:04:08 +0300
      Finished:     Tue, 07 Nov 2023 21:04:28 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8lq5g (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-8lq5g:
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
  Normal  Scheduled  3m5s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    3m5s   kubelet            Pulling image "busybox"
  Normal  Pulled     2m58s  kubelet            Successfully pulled image "busybox" in 6.496294959s (6.496310466s including waiting)
  Normal  Created    2m58s  kubelet            Created container pre-install-container
  Normal  Started    2m58s  kubelet            Started container pre-install-container
```
