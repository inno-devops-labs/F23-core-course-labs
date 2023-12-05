## Serving helm chart

![healthy_application_dashboard.png](resources/healthy_application_dashboard.png)

`kubectl get pods,svc`

```
NAME                                         READY   STATUS    RESTARTS      AGE
pod/app-python-1699274183-699595b64c-z54jl   1/1     Running   0             4m14s
pod/web-548f6458b5-2vbr4                     1/1     Running   3 (10m ago)   5d18h

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/app-python-1699274183   ClusterIP   10.99.217.112   <none>        8000/TCP   4m14s
service/kubernetes              ClusterIP   10.96.0.1       <none>        443/TCP    8d
```

## Testing hooks

`kubectl get po`

```
NAME                                         READY   STATUS      RESTARTS      AGE
app-with-hooks-app-python-7ff58fcf8f-9294v   1/1     Running     0             40s
postinstall-hook                             0/1     Completed   0             40s
preinstall-hook                              0/1     Completed   0             69s
web-548f6458b5-2vbr4                         1/1     Running     3 (37m ago)   5d19h
```

`kubectl describe po preinstall-hook`

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 06 Nov 2023 16:06:57 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.63
IPs:
  IP:  10.244.0.63
Containers:
  pre-install-container:
    Container ID:  docker://435f10365228d19fa4f99a0e25b1c20e1c2134b92991255a8da64be8f2ca3460
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
      Started:      Mon, 06 Nov 2023 16:07:04 +0300
      Finished:     Mon, 06 Nov 2023 16:07:24 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-2vrh5 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-2vrh5:
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
  Normal  Scheduled  99s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    99s   kubelet            Pulling image "busybox"
  Normal  Pulled     93s   kubelet            Successfully pulled image "busybox" in 5.737886211s (5.737897669s including waiting)
  Normal  Created    93s   kubelet            Created container pre-install-container
  Normal  Started    93s   kubelet            Started container pre-install-container
  
```

`kubectl describe po postinstall-hook`

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 06 Nov 2023 16:07:26 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.65
IPs:
  IP:  10.244.0.65
Containers:
  post-install-container:
    Container ID:  docker://fabc26bc77ac2086344daad0c0a559230779e8ea9199a34210b9eb8694cdf313
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
      Started:      Mon, 06 Nov 2023 16:07:28 +0300
      Finished:     Mon, 06 Nov 2023 16:07:43 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-v9wsl (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-v9wsl:
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
  Normal  Pulled     110s  kubelet            Successfully pulled image "busybox" in 1.560901501s (1.560912625s including waiting)
  Normal  Created    110s  kubelet            Created container post-install-container
  Normal  Started    110s  kubelet            Started container post-install-container
```

## Hook deletion policy

### Pods and services before adding hook deletion policy

`kubectl get pods,svc`

```
NAME                                             READY   STATUS      RESTARTS      AGE
pod/app-with-hooks-app-python-7ff58fcf8f-9294v   1/1     Running     0             6m7s
pod/postinstall-hook                             0/1     Completed   0             6m7s
pod/preinstall-hook                              0/1     Completed   0             6m36s
pod/web-548f6458b5-2vbr4                         1/1     Running     3 (43m ago)   5d19h

NAME                                TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/app-with-hooks-app-python   ClusterIP   10.96.76.161   <none>        8000/TCP   6m7s
service/kubernetes                  ClusterIP   10.96.0.1      <none>        443/TCP    8d
```

### Pods and services after adding hook deletion policy and reinstalling chart:

`kubectl get pods,svc`

```
NAME                                                                 READY   STATUS    RESTARTS      AGE
pod/app-with-hooks-and-deletion-policy-app-python-64f5bbfdc5-qz25c   1/1     Running   0             34s
pod/web-548f6458b5-2vbr4                                             1/1     Running   3 (45m ago)   5d19h

NAME                                                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/app-with-hooks-and-deletion-policy-app-python   ClusterIP   10.98.197.11   <none>        8000/TCP   34s
service/kubernetes                                      ClusterIP   10.96.0.1      <none>        443/TCP    8d
```

## Library chart

I added library chart with some labels including `app.kubernetes.io/managed-by: klemencja-devops-lab-charts` to make
sure the Helm uses values from the library.
I updated dependencies for both of the charts by `helm dependency update app-python/`
and  `helm dependency update app-kotlin/`
The outpu is:

```
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```

Then I reinstalled my charts and checked pods:
`kubectl get pod`

```
NAME                                READY   STATUS    RESTARTS        AGE
app-kotlin-chart-59f95745fc-fn6nk   1/1     Running   0               3m24s
app-python-chart-6b84d7c6cd-hbmhv   1/1     Running   0               2m12s
```

Finally, I checked the pods descriptions:

`kubectl describe po app-kotlin-chart-59f95745fc-fn6nk`

```
Name:             app-kotlin-chart-59f95745fc-fn6nk
Namespace:        default
Priority:         0
Service Account:  app-kotlin-chart
Node:             minikube/192.168.49.2
Start Time:       Mon, 06 Nov 2023 20:51:44 +0300
Labels:           app.kubernetes.io/instance=app-kotlin-chart
                  app.kubernetes.io/managed-by=klemencja-devops-lab-charts
                  app.kubernetes.io/version=1.16.0
                  pod-template-hash=59f95745fc
Annotations:      <none>
Status:           Running
IP:               10.244.0.76
IPs:
  IP:           10.244.0.76
Controlled By:  ReplicaSet/app-kotlin-chart-59f95745fc
...
```

`kubectl describe pod app-python-chart-7dc9d64b98-2hzc4`

```
Name:             app-python-chart-6b84d7c6cd-s6zj4
Namespace:        default
Priority:         0
Service Account:  app-python-chart
Node:             minikube/192.168.49.2
Start Time:       Mon, 06 Nov 2023 20:58:51 +0300
Labels:           app.kubernetes.io/instance=app-python-chart
                  app.kubernetes.io/managed-by=klemencja-devops-lab-charts
                  app.kubernetes.io/version=1.16.0
                  pod-template-hash=6b84d7c6cd
Annotations:      <none>
Status:           Running
IP:               10.244.0.81
IPs:
  IP:           10.244.0.81
Controlled By:  ReplicaSet/app-python-chart-6b84d7c6cd
...
```

And found that both pods have my custom label `app.kubernetes.io/managed-by=klemencja-devops-lab-charts`.
Which means that my library is being used.