# Helm

## Task 1

`helm upgrade --install python . --values values.python.yaml`

```
PS C:\Users\Damir\Documents\devops-course\k8s\helm-chart-app> helm upgrade --install python . --values values.python.yaml
Release "python" has been upgraded. Happy Helming!
NAME: python
LAST DEPLOYED: Mon Nov  6 00:06:15 2023
NAMESPACE: default
STATUS: deployed
REVISION: 3
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services python-helm-chart-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

`kubectl get pods,svc`

```
PS C:\Users\Damir> kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS       AGE
pod/c-sharp-app-7cf987d7f6-5q9zj             1/1     Running   3 (5d2h ago)   5d7h
pod/c-sharp-app-7cf987d7f6-jgbkg             1/1     Running   3 (5d2h ago)   5d7h
pod/c-sharp-app-7cf987d7f6-lfq5b             1/1     Running   3 (5d2h ago)   5d7h
pod/python-app-7d674fd95-jt9zk               1/1     Running   3 (5d2h ago)   5d7h
pod/python-app-7d674fd95-knrz6               1/1     Running   3 (5d2h ago)   5d7h
pod/python-app-7d674fd95-r9hln               1/1     Running   3 (5d2h ago)   5d7h
pod/python-helm-chart-app-7fd57cbc9d-24smg   1/1     Running   0              8m4s
pod/python-helm-chart-app-7fd57cbc9d-q9jz7   1/1     Running   0              8m4s
pod/python-helm-chart-app-7fd57cbc9d-qvf5m   1/1     Running   0              8m4s

NAME                            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/c-sharp-app             NodePort    10.100.124.164   <none>        80:31880/TCP     5d7h
service/kubernetes              ClusterIP   10.96.0.1        <none>        443/TCP          5d8h
service/python-app              NodePort    10.103.179.73    <none>        8000:31680/TCP   5d7h
service/python-helm-chart-app   NodePort    10.103.140.82    <none>        8000:30940/TCP   8m4s
```

## Task 2

`helm lint helm-chart-app`

```
PS C:\Users\Damir\Documents\devops-course\k8s> helm lint helm-chart-app
==> Linting helm-chart-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

`kubectl get po`

```
PS C:\Users\Damir\Documents\devops-course\k8s> kubectl get po
NAME                                         READY   STATUS      RESTARTS      AGE
c-sharp-app-7cf987d7f6-5q9zj                 1/1     Running     4 (24m ago)   6d21h
c-sharp-app-7cf987d7f6-jgbkg                 1/1     Running     4 (24m ago)   6d21h
c-sharp-app-7cf987d7f6-lfq5b                 1/1     Running     4 (24m ago)   6d21h
helm-hooks-helm-chart-app-654f45bff5-6qtjk   1/1     Running     0             62s
helm-hooks-helm-chart-app-654f45bff5-tcnj2   1/1     Running     0             62s
helm-hooks-helm-chart-app-654f45bff5-w9sz8   1/1     Running     0             62s
postinstall-hook                             0/1     Completed   0             61s
preinstall-hook                              0/1     Completed   0             85s
python-app-7d674fd95-jt9zk                   1/1     Running     4 (24m ago)   6d22h
python-app-7d674fd95-knrz6                   1/1     Running     4 (24m ago)   6d22h
python-app-7d674fd95-r9hln                   1/1     Running     4 (24m ago)   6d22h
python-helm-chart-app-7fd57cbc9d-6whsk       1/1     Running     0             8m5s
python-helm-chart-app-7fd57cbc9d-8zcml       1/1     Running     0             8m5s
python-helm-chart-app-7fd57cbc9d-sn486       1/1     Running     0             8m5s
```

`kubectl describe po preinstall-hook`

```
PS C:\Users\Damir\Documents\devops-course\k8s> kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 14:27:26 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.80
IPs:
  IP:  10.244.0.80
Containers:
  pre-install-container:
    Container ID:  docker://a8505a1a27d89381cef9043ce7284fe2eeb4a95e0c818d3021d2904a4e16fed7
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
      Started:      Tue, 07 Nov 2023 14:27:27 +0300
      Finished:     Tue, 07 Nov 2023 14:27:47 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-f2rpr (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-f2rpr:
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
  Normal  Scheduled  2m7s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m6s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m6s  kubelet            Created container pre-install-container
  Normal  Started    2m6s  kubelet            Started container pre-install-container
```

`kubectl describe po postinstall-hook`

```
PS C:\Users\Damir\Documents\devops-course\k8s> kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 14:27:50 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.82
IPs:
  IP:  10.244.0.82
Containers:
  post-install-container:
    Container ID:  docker://254c7253ad6ede0cb373b79ac7b46074281bdcd6491ee5089c8ff86cfe1f980b
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 14:27:51 +0300
      Finished:     Tue, 07 Nov 2023 14:28:11 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-r6br7 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-r6br7:
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
  Normal  Scheduled  2m18s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     2m17s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m17s  kubelet            Created container post-install-container
  Normal  Started    2m17s  kubelet            Started container post-install-container
```

### Delete policy

I used such delete policy for both post/pre-install:

`"helm.sh/hook-delete-policy": hook-succeeded`

## Bonus task

### Extra app

I have created `values.c-sharp.yaml` file for extra app

`helm install c-sharp . --values values.c-sharp.yaml`

```
PS C:\Users\Damir\Documents\devops-course\k8s\helm-chart-app> helm install c-sharp . --values values.c-sharp.yaml
NAME: c-sharp
LAST DEPLOYED: Tue Nov  7 14:39:33 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services c-sharp-helm-chart-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

`kubectl get pods,svc`

```
PS C:\Users\Damir\Documents\devops-course\k8s\helm-chart-app> kubectl get pods,svc
NAME                                          READY   STATUS    RESTARTS      AGE
pod/c-sharp-app-7cf987d7f6-5q9zj              1/1     Running   4 (76m ago)   6d22h
pod/c-sharp-app-7cf987d7f6-jgbkg              1/1     Running   4 (76m ago)   6d22h
pod/c-sharp-app-7cf987d7f6-lfq5b              1/1     Running   4 (76m ago)   6d22h
pod/c-sharp-helm-chart-app-564445c4c9-dzs8f   1/1     Running   0             49s
pod/c-sharp-helm-chart-app-564445c4c9-hcv99   1/1     Running   0             49s
pod/c-sharp-helm-chart-app-564445c4c9-xhdc9   1/1     Running   0             49s
pod/python-app-7d674fd95-jt9zk                1/1     Running   4 (76m ago)   6d23h
pod/python-app-7d674fd95-knrz6                1/1     Running   4 (76m ago)   6d23h
pod/python-app-7d674fd95-r9hln                1/1     Running   4 (76m ago)   6d23h
pod/python-helm-chart-app-7fd57cbc9d-6whsk    1/1     Running   0             60m
pod/python-helm-chart-app-7fd57cbc9d-8zcml    1/1     Running   0             60m
pod/python-helm-chart-app-7fd57cbc9d-sn486    1/1     Running   0             60m

NAME                             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/c-sharp-app              NodePort    10.100.124.164   <none>        80:31880/TCP     6d22h
service/c-sharp-helm-chart-app   NodePort    10.108.52.5      <none>        80:32062/TCP     49s
service/kubernetes               ClusterIP   10.96.0.1        <none>        443/TCP          6d23h
service/python-app               NodePort    10.103.179.73    <none>        8000:31680/TCP   6d23h
service/python-helm-chart-app    NodePort    10.99.153.233    <none>        8000:31704/TCP   60m
```

### Helm Library Charts

`helm dependency update helm-chart-app`

```
PS C:\Users\Damir\Documents\devops-course\k8s> helm dependency update helm-chart-app
Saving 1 charts
Deleting outdated charts
```

I have updatetd `helm-chart-app/templates/deployment.yaml` to use library Chart

```
...
labels:
  {{- include "libchart.labels" . | nindent 4 }}
...
matchLabels:
  {{- include "libchart.labels" . | nindent 6 }}
...
labels:
  {{- include "libchart.labels" . | nindent 8 }}
```