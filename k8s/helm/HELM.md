## **TASK 1:**
### **Pods:**
```
$ kubectl get pods, svc
NAME                                READY   STATUS      RESTARTS    AGE
pod/app-python-483ac7ba53-81e56     1/1     Running     0           5m17s

NAME                  TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)           AGE
service/app-python    LoadBalancer   10.101.154.214   <pending>      5000:31047/TCP      3m8s
service/kubernetes    ClusterIP      10.96.0.1        <none>         443/TCP           5m13s
```

## **TASK 2:**

### **kubectl describe po pre-install-hook:**
```
$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 14 Nov 2023 22:37:04 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.9
IPs:
  IP:  10.244.0.9
Containers:
  pre-install-container:
    Container ID:  docker://g9ei71de20e530250be8a92fdd42caf64afe626937da3c5a06ff8b5dff543d0d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7c478225cffac6b7977eedfe51cf4e73
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 2
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 14 Nov 2023 22:37:05 +0300
      Finished:     Wed, 14 Nov 2023 22:37:06 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-sf4we (ro)  
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-sf4we:
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
  Normal  Scheduled  35s    default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     40s    kubelet            Container image "busybox" already present on machine
  Normal  Created    47s    kubelet            Created container pre-install-container
  Normal  Started    52s    kubelet            Started container pre-install-container  
```

### **kubectl describe po post-install-hook:**
```
$ kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 14 Nov 2023 22:38:23 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.11
IPs:
  IP:  10.244.0.11
Containers:
  pre-install-container:
    Container ID:  docker://se5b89sq43b840143ds6a87jfr21acf54sea938412xc3c56z23ld4f7awq756f4x
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7c478225cffac6b7977eedfe51cf4e73
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 2
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 14 Nov 2023 22:38:24 +0300
      Finished:     Wed, 14 Nov 2023 22:38:25 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-fre3q (ro)  
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-fre3q:
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
  Normal  Scheduled  1m32s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulled     1m36s  kubelet            Container image "busybox" already present on machine
  Normal  Created    1m41s  kubelet            Created container pre-install-container
  Normal  Started    1m43s  kubelet            Started container pre-install-container  
```
