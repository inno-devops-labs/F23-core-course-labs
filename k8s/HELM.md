# Commands output:

- ```kubectl get pods,svc```
  ```
    NAME                              READY   STATUS      RESTARTS   AGE
    pod/lab10chart-6dbb84d9c6-gqrsx   1/1     Running     0          2m1s
    pod/postinstall-hook              0/1     Completed   0          2m1s
    pod/preinstall-hook               0/1     Completed   0          2m29s
    
    NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
    service/kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP    54m
    service/lab10chart   ClusterIP   10.109.125.116   <none>        5000/TCP   2m1s
  ```

- ```kubectl get po```
  ```
    NAME                          READY   STATUS      RESTARTS   AGE
    lab10chart-6dbb84d9c6-gqrsx   1/1     Running     0          2m51s
    postinstall-hook              0/1     Completed   0          2m51s
    preinstall-hook               0/1     Completed   0          3m19s
  ```
- ```kubectl describe po postinstall-hook```
  ``` 
    Name:             postinstall-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Tue, 07 Nov 2023 15:19:09 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: post-install
    Status:           Succeeded
    IP:               10.244.0.10
    IPs:
      IP:  10.244.0.10
    Containers:
      post-install-container:
        Container ID:  docker://289a5d546e71c946860ac13951fd2e6410c554bf0d7f315b2b12aa042e50ee01
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
          Started:      Tue, 07 Nov 2023 15:19:12 +0300
          Finished:     Tue, 07 Nov 2023 15:19:27 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wccm6 (ro)
    Conditions:
      Type              Status
      Initialized       True 
      Ready             False 
      ContainersReady   False 
      PodScheduled      True 
    Volumes:
      kube-api-access-wccm6:
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
      Normal  Scheduled  4m15s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
      Normal  Pulling    4m14s  kubelet            Pulling image "busybox"
      Normal  Pulled     4m12s  kubelet            Successfully pulled image "busybox" in 2.433924317s (2.433944362s including waiting)
      Normal  Created    4m12s  kubelet            Created container post-install-container
      Normal  Started    4m11s  kubelet            Started container post-install-container
  ```
- ```kubectl describe po preinstall-hook```
  ```
    Name:             preinstall-hook
    Namespace:        default
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Tue, 07 Nov 2023 15:18:41 +0300
    Labels:           <none>
    Annotations:      helm.sh/hook: pre-install
    Status:           Succeeded
    IP:               10.244.0.8
    IPs:
      IP:  10.244.0.8
    Containers:
      pre-install-container:
        Container ID:  docker://086bb09785ed9ee41671a0bf76c40044d5139050665516aec1f7fb4d028533c3
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
          Started:      Tue, 07 Nov 2023 15:18:48 +0300
          Finished:     Tue, 07 Nov 2023 15:19:08 +0300
        Ready:          False
        Restart Count:  0
        Environment:    <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vxks9 (ro)
    Conditions:
      Type              Status
      Initialized       True 
      Ready             False 
      ContainersReady   False 
      PodScheduled      True 
    Volumes:
      kube-api-access-vxks9:
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
      Normal  Scheduled  6m3s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
      Normal  Pulling    6m3s   kubelet            Pulling image "busybox"
      Normal  Pulled     5m57s  kubelet            Successfully pulled image "busybox" in 6.190650198s (6.190678064s including waiting)
      Normal  Created    5m57s  kubelet            Created container pre-install-container
      Normal  Started    5m56s  kubelet            Started container pre-install-container
  
  ```