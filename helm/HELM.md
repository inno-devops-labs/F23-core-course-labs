# Task 1

```
D:\study\core-course-labs> minikube service python-app
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app | http/5000   | http://192.168.49.2:31032 |
|-----------|------------|-------------|---------------------------|
* Starting tunnel for service python-app.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | python-app |             | http://127.0.0.1:11932 |
|-----------|------------|-------------|------------------------|
* Opening service default/python-app in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

```
D:\study\core-course-labs\k8s\helm\python-app> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-7cd64b5444-2pgbm   1/1     Running   0          76s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP          10m
service/python-app   NodePort    10.105.0.211   <none>        5000:31032/TCP   76s
```

# Task 2

```
D:\study\core-course-labs\k8s\helm\python-app> kubectl get pods,svc
NAME                              READY   STATUS      RESTARTS   AGE
pod/post-install-hook             0/1     Completed   0          105s
pod/pre-install-hook              0/1     Completed   0          111s
pod/python-app-7cd64b5444-h9bjk   1/1     Running     0          105s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          104m
service/python-app   NodePort    10.98.169.109   <none>        5000:31339/TCP   105s
```

```
D:\study\core-course-labs\k8s\helm\python-app> kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 02:44:38 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.19
IPs:
  IP:  10.244.0.19
Containers:
  post-install-container:
    Container ID:  docker://8c5a509c7903ae55ca467ed5b49ae285b65c02f8505df403c0974566f5e1aecd
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 2
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 02:44:39 +0300
      Finished:     Wed, 08 Nov 2023 02:44:41 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-flxgw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-flxgw:
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
  Normal  Scheduled  2m17s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulled     2m16s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m16s  kubelet            Created container post-install-container
  Normal  Started    2m16s  kubelet            Started container post-install-container
```

```
D:\study\core-course-labs\k8s\helm\python-app> kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 02:44:33 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.17
IPs:
  IP:  10.244.0.17
Containers:
  pre-install-container:
    Container ID:  docker://c8ee71de20e530250be8a92fdd42cac64afe626937da3c5a06ff8b5dff543d0d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 2
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 02:44:34 +0300
      Finished:     Wed, 08 Nov 2023 02:44:36 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-vtr8c (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-vtr8c:
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
  Normal  Scheduled  2m58s  default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     2m58s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m58s  kubelet            Created container pre-install-container
  Normal  Started    2m57s  kubelet            Started container pre-install-container
```

# Bonus task

```
D:\study\core-course-labs\k8s\helm\svelte-app> kubectl describe po svelte-app
Name:             svelte-app-6b7cfc5456-nrnml
Namespace:        default
Priority:         0
Service Account:  svelte-app
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 02:53:54 +0300
Labels:           app.kubernetes.io/instance=svelte-app
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=svelte-app
                  app.kubernetes.io/version=1.16.0
                  custom=custom
                  helm.sh/chart=svelte-app-0.1.0
                  pod-template-hash=6b7cfc5456
Annotations:      <none>
Status:           Pending
IP:
IPs:              <none>
Controlled By:    ReplicaSet/svelte-app-6b7cfc5456
Containers:
  svelte-app:
    Container ID:
    Image:          relisqu/svelte-app:latest
    Image ID:
    Port:           5173/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Liveness:       http-get http://:5173/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:5173/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5dggz (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-5dggz:
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
  Normal  Scheduled  21s   default-scheduler  Successfully assigned default/svelte-app-6b7cfc5456-nrnml to minikube
  Normal  Pulling    20s   kubelet            Pulling image "relisqu/svelte-app:latest"
```
