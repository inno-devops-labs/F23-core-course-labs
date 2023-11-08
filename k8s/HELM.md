# Helm

Helm is a package manager for Kubernetes, simplifying the deployment and management of applications on the cluster. 
It provides a templating system to define and configure complex Kubernetes resources in a declarative manner. 
With Helm, users can easily package and distribute their applications as Helm charts, enabling others to reproduce and 
deploy the same application with ease. It also supports versioning, rollbacks, and dependency management, making 
it a powerful tool for Kubernetes application lifecycle management.

## Task 1

### Installing Helm App

`helm install python helm-python/`

```
NAME: python
LAST DEPLOYED: Wed Nov  8 08:46:30 2023
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

### Verifying Services

`minikube service app-python`

```
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   |    app-python    |        8080 | http://192.168.49.2:30245 |
|-----------|------------------|-------------|---------------------------|
```

### Getting Pods and Services

`kubectl get pods,svc`

```
NAME                                      READY   STATUS    RESTARTS     AGE
pod/app-python-6c64b5648d-4l6ft           1/1     Running   0          108s
pod/app-python-6c64b5648d-m78sq           1/1     Running   0          108s
pod/app-python-6c64b5648d-qptcc           1/1     Running   0          108s
pod/python-helm-python-58fccf7f84-mf5zg   1/1     Running   0          60s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python           LoadBalancer   10.100.12.78    <pending>     8000:30495/TCP   104s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          3m11s
service/python-helm-python   ClusterIP      10.106.67.103   <none>        5000/TCP         60s
```

## Task 2

### Installing and Describing Hooks

`helm lint helm-python/`

```
==> Linting helm-python/
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

`kubectl get po`

```
app-python-6c64b5648d-4l6ft               1/1     Running     0          19m
app-python-6c64b5648d-m78sq               1/1     Running     0          19m
app-python-6c64b5648d-qptcc               1/1     Running     0          19m
helm-hooks-helm-python-7b6d6d7969-b4tkv   1/1     Running     0          36s
postinstall-hook                          0/1     Completed   0          36s
preinstall-hook                           0/1     Completed   0          59s
python-helm-python-58fccf7f84-mf5zg       1/1     Running     0          18m
```

### Preinstall Hook

`kubectl describe po preinstall-hook`

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 09:41:14 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.67
IPs:
  IP:  10.244.0.67
Containers:
  pre-install-container:
    Container ID:  docker://e285c90872aab58c2548cb466648c8e7186430268b065877038c5f11156063df
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
      Started:      Wed, 08 Nov 2023 09:41:15 +0300
      Finished:     Wed, 08 Nov 2023 09:41:35 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-m9d9f (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-m9d9f:
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
  Normal  Scheduled  103s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     103s  kubelet            Container image "busybox" already present on machine
  Normal  Created    102s  kubelet            Created container pre-install-container
  Normal  Started    102s  kubelet            Started container pre-install-container
```

### Postinstall Hook

`kubectl describe po postinstall-hook`

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 09:41:37 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.69
IPs:
  IP:  10.244.0.69
Containers:
  post-install-container:
    Container ID:  docker://45481b053946099c83468cb18b775b5d59b69788c7413b934927d695514fa7aa
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
      Started:      Wed, 08 Nov 2023 09:41:38 +0300
      Finished:     Wed, 08 Nov 2023 09:41:58 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lqdc4 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-lqdc4:
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
  Normal  Scheduled  106s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     106s  kubelet            Container image "busybox" already present on machine
  Normal  Created    106s  kubelet            Created container post-install-container
  Normal  Started    106s  kubelet            Started container post-install-container
```

## Bonus Task

### Creating a Library Chart

`helm dependency update .`

```
Saving 1 charts
Deleting outdated charts
```