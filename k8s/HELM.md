# Helm

1. Helm chart installation 
```bash
helm install python-app python-app
```

```bash
NAME: python-app
LAST DEPLOYED: Sun Oct 29 23:33:42 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
```

2. Deployed app with helm

```bash
kubectl get pods,svc
```

```bash
NAME                              READY   STATUS      RESTARTS   AGE
pod/postinstall-hook              0/1     Completed   0          8m40s
pod/preinstall-hook               0/1     Completed   0          9m3s
pod/python-app-65c7657b45-bpgzl   1/1     Running     0          8m40s
pod/python-app-65c7657b45-k78qm   1/1     Running     0          8m40s
pod/python-app-65c7657b45-vs2d7   1/1     Running     0          8m40s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          6h27m
service/python-app   LoadBalancer   10.98.204.58   <pending>     8000:32219/TCP   8m41s
```

3. Hooks describe

```bash
kubectl describe po preinstall-hook
```

```bash
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 30 Oct 2023 00:43:04 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.21
IPs:
  IP:  10.244.0.21
Containers:
  pre-install-container:
    Container ID:  docker://3e02b474137d358ca4d488926c0444da9da372543add1835d7b99172102d33e9
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
      Started:      Mon, 30 Oct 2023 00:43:05 +0300
      Finished:     Mon, 30 Oct 2023 00:43:25 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zgthk (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-zgthk:
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
  Normal  Scheduled  11m   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     11m   kubelet            Container image "busybox" already present on machine
  Normal  Created    11m   kubelet            Created container pre-install-container
  Normal  Started    11m   kubelet            Started container pre-install-container
```

```bash
kubectl describe po postinstall-hook
```

```bash
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Mon, 30 Oct 2023 00:43:27 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.25
IPs:
  IP:  10.244.0.25
Containers:
  post-install-container:
    Container ID:  docker://4897861d13a774d11963d6eb57529b4d74fe15cc6fc49b9cb47ae42acc9f3cd0
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
      Started:      Mon, 30 Oct 2023 00:43:31 +0300
      Finished:     Mon, 30 Oct 2023 00:43:46 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-j9zwh (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-j9zwh:
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
  Normal  Scheduled  11m   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    11m   kubelet            Pulling image "busybox"
  Normal  Pulled     11m   kubelet            Successfully pulled image "busybox" in 3.482896862s (3.482904135s including waiting)
  Normal  Created    11m   kubelet            Created container post-install-container
  Normal  Started    11m   kubelet            Started container post-install-container
```

4. Running service 

```bash
platun0v-pc 3$ ➜ minikube service python-app                                                                   user:platun0v ~/pr/in/devops/k8s git:lab10 (2?1!)
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | python-app | http/8000   | http://192.168.49.2:32219 |
|-----------|------------|-------------|---------------------------|
🎉  Opening service default/python-app in default browser...
platun0v-pc 3$ ➜ curl http://192.168.49.2:32219/                                                            user:platun0v ~/pr/in/devops/k8s git:lab10 (2?1!) 2s
<!DOCTYPE html>
<html>
<head>
    <title>Current Time in Moscow</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <p>2023-10-30 00:56:36</p>
</body>
</html>⏎
```