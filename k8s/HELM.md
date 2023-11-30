# Helm

Azamat Shakirov B20-CS

a.shakirov@innopolis.university





---

### Helm outputs:

Output of `kubectl get pods,svc`:

```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/app-python-9c9f4bd89-vqq92   1/1     Running   0          3m19s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.99.226.90   <pending>     5000:30405/TCP   3m19s
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          7d16h

```



Output of `kubectl get po` with hooks:

```bash
NAME                                READY   STATUS      RESTARTS   AGE
app-python-hooks-74c469d9cb-z6mzc   1/1     Running     0          26s
postinstall-hook                    0/1     Completed   0          26s
preinstall-hook                     0/1     Completed   0          49s

```



Output of `kubectl describe po postinstall-hook`:

```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 16:44:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.21
IPs:
  IP:  10.244.0.21
Containers:
  post-install-container:
    Container ID:  docker://e8e644a39358c3e3b19bfe228076bc6a6dd605e33fd83a2467d2844773d36069
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
      Started:      Wed, 08 Nov 2023 16:44:17 +0300
      Finished:     Wed, 08 Nov 2023 16:44:32 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lfctr (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-lfctr:
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
  Normal  Scheduled  6m18s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    6m19s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m16s  kubelet            Successfully pulled image "busybox" in 2.547241229s (2.547256203s including waiting)
  Normal  Created    6m16s  kubelet            Created container post-install-container
  Normal  Started    6m16s  kubelet            Started container post-install-container

```



Output of `kubectl describe po preinstall-hook`:

```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 16:43:51 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.19
IPs:
  IP:  10.244.0.19
Containers:
  pre-install-container:
    Container ID:  docker://58e78c88dfd6860ce031a5dff0c79c3afe44b3b32ecc5b7176853d21d5755cbe
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
      Started:      Wed, 08 Nov 2023 16:43:52 +0300
      Finished:     Wed, 08 Nov 2023 16:44:12 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vqtg8 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-vqtg8:
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
  Normal  Scheduled  7m44s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     7m43s  kubelet            Container image "busybox" already present on machine
  Normal  Created    7m43s  kubelet            Created container pre-install-container
  Normal  Started    7m43s  kubelet            Started container pre-install-container

```



Output of `kubectl get pods,svc`:

```bash
NAME                                    READY   STATUS      RESTARTS   AGE
pod/app-python-hooks-74c469d9cb-z6mzc   1/1     Running     0          8m2s
pod/postinstall-hook                    0/1     Completed   0          8m2s
pod/preinstall-hook                     0/1     Completed   0          8m25s

NAME                            TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python-hooks        LoadBalancer   10.96.15.193   <pending>     5000:30309/TCP   8m2s
service/kubernetes              ClusterIP      10.96.0.1      <none>        443/TCP          7d16h

```

