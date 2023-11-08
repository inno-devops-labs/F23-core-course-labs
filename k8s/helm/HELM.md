# Task 1

```
dmpru@dmpru:/mnt/g/git/core-course-labs$ minikube service app-python
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python | http/8000   | http://192.168.49.2:30947 |
|-----------|------------|-------------|---------------------------|
* Starting tunnel for service app-python.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:16417 |
|-----------|------------|-------------|------------------------|
* Opening service default/app-python in default browser...
```

```
dmpru@dmpru:/mnt/g/git/core-course-labs$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6b6dd7b8c9-gsbql   1/1     Running   0          74s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.109.152.114   <none>        8000:30620/TCP   74s
```

# Task 2

```
dmpru@dmpru:/mnt/g/git/core-course-labs$ kubectl get pods,svc
NAME                              READY   STATUS        RESTARTS      AGE
pod/app-python-6b79bb8584-bqjjt   0/1     Terminating   0             25s
pod/app-python-6b79bb8584-tp6dn   0/1     Running       0             10s
pod/post-install-hook             0/1     Completed     0             10s
pod/pre-install-hook              0/1     Completed     0             15s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.110.239.214   <none>        8000:30600/TCP   11s
```

```
dmpru@dmpru:/mnt/g/git/core-course-labs$ kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:31:49 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:  10.244.0.35
Containers:
  post-install-container:
    Container ID:  docker://6bd8d7157733559bb78d4150882a30606fb3148725ccd7df500d6f3e05715931
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 1
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 03:31:50 +0300
      Finished:     Wed, 08 Nov 2023 03:31:51 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gc4sw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-gc4sw:
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
  Normal  Scheduled  52s   default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulled     51s   kubelet            Container image "busybox" already present on machine
  Normal  Created    51s   kubelet            Created container post-install-container
  Normal  Started    51s   kubelet            Started container post-install-container
```

```
dmpru@dmpru:/mnt/g/git/core-course-labs$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:31:44 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.34
IPs:
  IP:  10.244.0.34
Containers:
  pre-install-container:
    Container ID:  docker://3bf52082cbc9490728b32b0e4da2840d379708e3036148997d3b791fab63265f
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
      Started:      Wed, 08 Nov 2023 03:31:45 +0300
      Finished:     Wed, 08 Nov 2023 03:31:46 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-sdlk9 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-sdlk9:
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
  Normal  Scheduled  80s   default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     79s   kubelet            Container image "busybox" already present on machine
  Normal  Created    79s   kubelet            Created container pre-install-container
  Normal  Started    79s   kubelet            Started container pre-install-container
```

# Bonus task

```
dmpru@dmpru:/mnt/g/git/core-course-labs$ kubectl describe po app-js
Name:             app-csharp-68948bdb45-dvdh4
Namespace:        default
Priority:         0
Service Account:  app-csharp
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:38:26 +0300
Labels:           app.kubernetes.io/instance=app-csharp
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=app-csharp
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=app-csharp-0.1.0
                  pod-template-hash=68948bdb45
                  test=test
Annotations:      <none>
Status:           Pending
IP:
IPs:              <none>
Controlled By:    ReplicaSet/app-csharp-68948bdb45
Containers:
  app-csharp:
    Container ID:
    Image:          dmitriypru/core_course_labs_csharp:latest
    Image ID:
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Liveness:       http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vvs6x (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-vvs6x:
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
  Normal  Scheduled  17s   default-scheduler  Successfully assigned default/app-csharp-68948bdb45-dvdh4 to minikube
  Normal  Pulling    16s   kubelet            Pulling image "dmitriypru/core_course_labs_csharp:latest"
```
