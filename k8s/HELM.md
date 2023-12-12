# Helm

Helm provides a solution to the challenges encountered in managing a growing microservice architecture. 
It functions as a robust tool, automating the process of creating, packaging, configuring, 
and deploying Kubernetes applications. By consolidating configuration files into a single, reusable package, 
Helm simplifies the management complexities inherent in an expanding microservice infrastructure.

## Task 1

### Helm App Installation 

`helm install python helm-app-python/`

```
NAME: python
LAST DEPLOYED: Sun Nov  19 10:46:13 2023 
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=helm-python,app.kubernetes.io/instance=python" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

### Services Check Out

`minikube service app-python`

```
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   |    app-python    |        8080 | http://192.168.49.2:30445 |
|-----------|------------------|-------------|---------------------------|
```

### Pods and Services

`kubectl get pods,svc`

```
NAME                                          READY   STATUS    RESTARTS   AGE
pod/app-python-86b44b58ff-lb6bt               1/1     Running   0          90s
pod/app-python-86b44b58ff-n8ms6               1/1     Running   0          90s
pod/app-python-86b44b58ff-ppstz               1/1     Running   0          90s
pod/python-helm-app-python-54sggf5s64-nj5zl   1/1     Running   0          45s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           LoadBalancer   10.102.24.74    <pending>     5000:30495/TCP   102s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          2m17s
service/python-helm-python   ClusterIP      10.107.68.107   <none>        8080/TCP         48s
```

## Task 2

### Hooks Installation

`helm lint helm-app-python/`

```
==> Linting helm-app-python/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

`kubectl get po`

```
app-python-86b44b58ff-lb6bt                   1/1     Running     0          17m
app-python-86b44b58ff-n8ms6                   1/1     Running     0          17m
app-python-86b44b58ff-ppstz                   1/1     Running     0          17m
helm-hooks-helm-app-python-7d4b6b5767-b6ttl   1/1     Running     0          32s
postinstall-hook                              0/1     Completed   0          32s
preinstall-hook                               0/1     Completed   0          49s
python-helm-app-python-54sggf5s64-nj5zl       1/1     Running     0          16m
```

### Preinstall Hook

`kubectl describe po preinstall-hook`

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 19 Nov 2023 11:55:02 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.59
IPs:
  IP:  10.244.0.59
Containers:
  pre-install-container:
    Container ID:  docker://6e61c1770eb76bf3d42ca54262880b68a058838235960456c5c887610418c58f
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
      Started:      Sun, 19 Nov 2023 11:55:03 +0300
      Finished:     Sun, 19 Nov 2023 11:55:23 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mdf9n (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-mdf9n:
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
  Type    Reason     Age  From               Message
  ----    ------     ---- ----               -------
  Normal  Scheduled  99s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     99s  kubelet            Container image "busybox" already present on machine
  Normal  Created    98s  kubelet            Created container pre-install-container
  Normal  Started    98s  kubelet            Started container pre-install-container
```

### Postinstall Hook

`kubectl describe po postinstall-hook`

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 19 Nov 2023 11:55:26 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.63
IPs:
  IP:  10.244.0.63
Containers:
  post-install-container:
    Container ID:  docker://72681bea9ac8750d8c451e73ef979533d1c4aa47ab382b9b1b81531f534126aa
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
      Started:      Sun, 19 Nov 2023 11:55:27 +0300
      Finished:     Sun, 19 Nov 2023 11:55:53 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-d4sc6 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             Falses
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-d4sc6:
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
  Normal  Scheduled  103s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     103s  kubelet            Container image "busybox" already present on machine
  Normal  Created    103s  kubelet            Created container post-install-container
  Normal  Started    102s  kubelet            Started container post-install-container
```