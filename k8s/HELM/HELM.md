# Task 1

```
purfreak@Tashas-MBP:/git/core-course-labs$ minikube service app-python
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python | http/8000   | http://192.168.49.2:30620 |
|-----------|------------|-------------|---------------------------|
* Starting tunnel for service app-python.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:14714 |
|-----------|------------|-------------|------------------------|
* Opening service default/app-python in default browser...
```

```
purfreak@Tashas-MBP:/git/core-course-labs$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-6b6dd7b8c9-gsbql   1/1     Running   0          74s

NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.109.152.114   <none>        8000:30620/TCP   74s
```

# Task 2

```
purfreak@Tashas-MBP:/git/core-course-labs$ kubectl get pods,svc
NAME                              READY   STATUS      RESTARTS   AGE
pod/app-python-6b6dd7b8c9-nsrdz   1/1     Running     0          15s
pod/post-install-hook             0/1     Completed   0          15s
pod/pre-install-hook              0/1     Completed   0          19s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/app-python   NodePort    10.99.85.225   <none>        8000:30550/TCP   15s
```

```
purfreak@Tashas-MBP:/git/core-course-labs$ kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:10:57 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.26
IPs:
  IP:  10.244.0.26
Containers:
  post-install-container:
    Container ID:  docker://9c116b77039f533542f0a4e18cc98f06c838ed94ba32c1caab6aee0b637f9662
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
      Started:      Wed, 08 Nov 2023 03:10:59 +0300
      Finished:     Wed, 08 Nov 2023 03:11:00 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-84nnp (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-84nnp:
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
  Normal  Scheduled  33s   default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulled     32s   kubelet            Container image "busybox" already present on machine
  Normal  Created    32s   kubelet            Created container post-install-container
  Normal  Started    31s   kubelet            Started container post-install-container
```

```
purfreak@Tashas-MBP:/git/core-course-labs$ kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:10:53 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  pre-install-container:
    Container ID:  docker://bcb1a4f22c9d795136d38382d553df96b6f452c37676f0d4bad5ff1cdba274a7
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
      Started:      Wed, 08 Nov 2023 03:10:54 +0300
      Finished:     Wed, 08 Nov 2023 03:10:55 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-55psw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-55psw:
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
  Normal  Scheduled  62s   default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulled     61s   kubelet            Container image "busybox" already present on machine
  Normal  Created    61s   kubelet            Created container pre-install-container
  Normal  Started    61s   kubelet            Started container pre-install-container
```

# Bonus task

```
purfreak@Tashas-MBP:/git/core-course-labs$ kubectl describe po app-js
Name:             app-js-756454486-t5vnz
Namespace:        default
Priority:         0
Service Account:  app-js
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:18:26 +0300
Labels:           app.kubernetes.io/instance=app-js
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=app-js
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=app-js-0.1.0
                  pod-template-hash=756454486
                  test=test
Annotations:      <none>
Status:           Pending
IP:
IPs:              <none>
Controlled By:    ReplicaSet/app-js-756454486
Containers:
  app-js:
    Container ID:
    Image:          purfreak/lab2_devops:latest-js
    Image ID:
    Port:           3000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Liveness:       http-get http://:3000/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:3000/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2bg2b (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-2bg2b:
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
  Normal  Scheduled  16s   default-scheduler  Successfully assigned default/app-js-756454486-t5vnz to minikube
  Normal  Pulling    15s   kubelet            Pulling image "purfreak/lab2_devops:latest-js"
```
