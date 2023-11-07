## Task 1

```bash
kubectl get pods,svc
NAME                                         READY   STATUS    RESTARTS   AGE
pod/app-python-1699386294-57866b5455-tgp8f   1/1     Running   0          3m12s

NAME                            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/app-python-1699386294   ClusterIP   10.107.87.44   <none>        80/TCP    3m12s
service/kubernetes              ClusterIP   10.96.0.1      <none>        443/TCP   6d23h
```

## Task 2

```bash
kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-1699386294-57866b5455-tgp8f   1/1     Running     0          134m
helm-hooks-app-python-6478894694-nv2mp   1/1     Running     0          45s
postinstall-hook                         0/1     Completed   0          45s
preinstall-hook                          0/1     Completed   0          65m
```

```bash
kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.105.2
Start Time:       Tue, 07 Nov 2023 23:53:03 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.32
IPs:
  IP:  10.244.0.32
Containers:
  pre-install-container:
    Container ID:  docker://f38dccd50ace1040fb9ea20a8eb082b93c38b07911a9d74f83a2ef7d70921bb8
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 00:57:59 +0300
      Finished:     Wed, 08 Nov 2023 00:58:09 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-759j4 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-759j4:
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
  Normal  Scheduled  66m   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    66m   kubelet            Pulling image "busybox"
  Normal  Pulled     77s   kubelet            Successfully pulled image "busybox" in 5.330667892s (5.330693808s including waiting)
  Normal  Created    77s   kubelet            Created container pre-install-container
  Normal  Started    77s   kubelet            Started container pre-install-container
```

```bash
kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.105.2
Start Time:       Wed, 08 Nov 2023 00:58:10 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.33
IPs:
  IP:  10.244.0.33
Containers:
  pre-install-container:
    Container ID:  docker://23edfdea894bb4bc853367faf63ede45d99d0370c892933ca608e3e0c7259517
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 10
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 00:58:11 +0300
      Finished:     Wed, 08 Nov 2023 00:58:21 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-nhmjs (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-nhmjs:
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
  Normal  Scheduled  99s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     99s   kubelet            Container image "busybox" already present on machine
  Normal  Created    99s   kubelet            Created container pre-install-container
  Normal  Started    99s   kubelet            Started container pre-install-container
```

```bash
kubectl get pods,svc
NAME                                         READY   STATUS      RESTARTS   AGE
pod/app-python-1699386294-57866b5455-tgp8f   1/1     Running     0          140m
pod/helm-hooks-app-python-6478894694-vr2tm   1/1     Running     0          25s
pod/postinstall-hook                         0/1     Completed   0          7m21s
pod/preinstall-hook                          0/1     Completed   0          72m

NAME                            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/app-python-1699386294   ClusterIP   10.107.87.44   <none>        80/TCP    140m
service/helm-hooks-app-python   ClusterIP   10.99.236.52   <none>        80/TCP    25s
service/kubernetes              ClusterIP   10.96.0.1      <none>        443/TCP   7d1h
```

## Bonus

```bash
helm dependency update app-elixir
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/kitt/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/kitt/.kube/config
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "postgres-operator-charts" chart repository
...Successfully got an update from the "blockscout-ci-cd" chart repository
...Successfully got an update from the "blockscout" chart repository
...Successfully got an update from the "ingress-nginx" chart repository
...Successfully got an update from the "enapter" chart repository
...Successfully got an update from the "minio" chart repository
...Successfully got an update from the "bedag" chart repository
...Successfully got an update from the "longhorn" chart repository
...Successfully got an update from the "grafana" chart repository
...Successfully got an update from the "prometheus-community" chart repository
...Successfully got an update from the "elastic" chart repository
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```

```bash
helm lint app-elixir
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/kitt/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/kitt/.kube/config
==> Linting app-elixir
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

```bash
helm dependency update app-python
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/kitt/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/kitt/.kube/config
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "postgres-operator-charts" chart repository
...Successfully got an update from the "blockscout-ci-cd" chart repository
...Successfully got an update from the "longhorn" chart repository
...Successfully got an update from the "blockscout" chart repository
...Successfully got an update from the "bedag" chart repository
...Successfully got an update from the "enapter" chart repository
...Successfully got an update from the "minio" chart repository
...Successfully got an update from the "ingress-nginx" chart repository
...Successfully got an update from the "elastic" chart repository
...Unable to get an update from the "prometheus-community" chart repository (https://prometheus-community.github.io/helm-charts):
	local error: tls: bad record MAC
...Successfully got an update from the "grafana" chart repository
...Unable to get an update from the "bitnami" chart repository (https://charts.bitnami.com/bitnami):
	local error: tls: bad record MAC
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```

```bash
helm lint app-python
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/kitt/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/kitt/.kube/config
==> Linting app-python
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

```bash
kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-elixir-687748dd46-wbprd   1/1     Running   0          7m30s
pod/app-python-5b658744b9-r5msp   1/1     Running   0          19s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-elixir   LoadBalancer   10.105.31.63    <pending>     4000:31821/TCP   7m30s
service/app-python   LoadBalancer   10.106.203.64   <pending>     80:30660/TCP     19s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          7d2h
```