# Helm
## Task 1
### Output of `kubectl get pods,svc`

```
[kinjalik@kinjalik-laptop k8s]$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-6b7d7dd46b-7c9xg   1/1     Running   0          65s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP          5d18h
service/python-app   NodePort    10.96.11.85   <none>        8000:31207/TCP   65s
```

## Task 2
Output of non-existing hooks is expected due to hook-delete-policy
```
[kinjalik@kinjalik-laptop k8s]$ kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
python-app-6b7d7dd46b-jt6dh   1/1     Running   0          81s
[kinjalik@kinjalik-laptop k8s]$ kubectl describe po post-install-hook
Error from server (NotFound): pods "post-install-hook" not found
[kinjalik@kinjalik-laptop k8s]$ kubectl describe po pre-install-hook
Error from server (NotFound): pods "pre-install-hook" not found
```

## Bonus
Additional application with custom labels from chart library

```
[kinjalik@kinjalik-laptop k8s]$ kubectl describe po kotlin-native-app-
Name:             kotlin-native-app-6cf685f7b4-7jbn6
Namespace:        default
Priority:         0
Service Account:  kotlin-native-app
Node:             minikube/192.168.49.2
Start Time:       Mon, 06 Nov 2023 17:24:53 +0300
Labels:           app.kubernetes.io/instance=kotlin-native-app
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=kotlin-native-app
                  app.kubernetes.io/version=1.16.0
                  custom=this_is_custom_label
                  pod-template-hash=6cf685f7b4
Annotations:      <none>
Status:           Running
IP:               10.244.0.65
IPs:
  IP:           10.244.0.65
Controlled By:  ReplicaSet/kotlin-native-app-6cf685f7b4
Containers:
  kotlin-native-app:
    Container ID:   docker://a79e98c4b23a6c38a89ac5ef0df33055b518b1f9470f0ecbfb57b9ee33f229a0
    Image:          kinjalik/devops-course-app:kotlin-native
    Image ID:       docker-pullable://kinjalik/devops-course-app@sha256:22fed002b71631ec8880edb80ab8c4862ff2da003805bb56f64da82991a9da76
    Port:           8080/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 07 Nov 2023 22:45:26 +0300
    Last State:     Terminated
      Reason:       Error
      Exit Code:    255
      Started:      Mon, 06 Nov 2023 17:24:54 +0300
      Finished:     Tue, 07 Nov 2023 22:44:55 +0300
    Ready:          True
    Restart Count:  1
    Liveness:       http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-skx57 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-skx57:
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
  Type    Reason          Age   From               Message
  ----    ------          ----  ----               -------
  Normal  Scheduled       29h   default-scheduler  Successfully assigned default/kotlin-native-app-6cf685f7b4-7jbn6 to minikube
  Normal  Pulled          29h   kubelet            Container image "kinjalik/devops-course-app:kotlin-native" already present on machine
  Normal  Created         29h   kubelet            Created container kotlin-native-app
  Normal  Started         29h   kubelet            Started container kotlin-native-app
  Normal  SandboxChanged  57s   kubelet            Pod sandbox changed, it will be killed and re-created.
  Normal  Pulled          56s   kubelet            Container image "kinjalik/devops-course-app:kotlin-native" already present on machine
  Normal  Created         56s   kubelet            Created container kotlin-native-app
  Normal  Started         55s   kubelet            Started container kotlin-native-app
```