# Helm 
## Chart creation 
### Create helm charts
Python app
```
helm create app_python
```
### Install Helm charts
Modified default `values.yaml` and `deployment.yaml` files to fit the task better.

Python app:
```
helm install app_python app_python/
```
Output:
```
NAME: app_python
LAST DEPLOYED: Mon Nov  6 17:39:34 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://python.app/
```
### Checking
````
kubectl get pods,svc     
````
Output:
````
NAME                              READY   STATUS    RESTARTS   AGE
pod/app_python-76c869585d-bqd6b   1/1     Running   0          24m
pod/app_python-76c869585d-pfh8z   1/1     Running   0          24m
pod/app_python-76c869585d-txwm6   1/1     Running   0          24m
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app_python   LoadBalancer   10.109.204.17   <pending>     8080:30113/TCP   23m
service/kubernetes   ClusterIP      10.95.0.1       <none>        443/TCP          24m
````
### Starting services
````
minikube service --all
````
Output:
````
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app_python | http/8080   | http://192.168.47.2:30113 |
|-----------|------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service app_python.
🏃  Starting tunnel for service kubernetes.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app_python |             | http://127.0.0.1:49916 |
| default   | kubernetes |             | http://127.0.0.1:49922 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app_python in default browser...
🎉  Opening service default/kubernetes in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
````
### Dashboard 
![dashboard](/k8s/img/dashboard.png)

## Chart Hooks 
### Linting 
Python:
````
helm lint app_python/ 
````
Output:
````
==> Linting app_python/
[INFO] Chart.yaml: icon is recommended
1 chart(s) linted, 0 chart(s) failed
````
### Pre-install and post-install hooks
Added `pre-install-hook.yaml` and `post-install-hook.yaml` files to `templates` directory. After reinstalling charts hooks can be verified:
```` 
kubectl get po  
````
Output:
````
NAME                          READY   STATUS      RESTARTS   AGE
app_python-76c869585d-2wlxw   1/1     Running     0          77s
app_python-76c869585d-j66m9   1/1     Running     0          77s
app_python-76c869585d-n29hm   1/1     Running     0          77s
python-postinstall-hook       0/1     Completed   0          77s
python-preinstall-hook        0/1     Completed   0          99s
````
### Describe pre-install hooks 
Python:
````
kubectl describe po python-preinstall-hook 
````
Output:
````
Name:         python-preinstall-hook
Namespace:    default
Priority:     0
Node:         minikube/192.168.48.2
Start Time:   Mon, 06 Nov 2023 18:48:14 +0300
Labels:       <none>
Annotations:  helm.sh/hook: pre-install
Status:       Succeeded
IP:           10.244.0.132
IPs:
  IP:  10.244.0.132
Containers:
  pre-install-container:
    Container ID:  docker://ba42f1b200a9666df2a7e1708e2ce70c6e21eca1b07418b3aee661e41563771d
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977efdfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 06 Nov 2023 18:48:14 +0300
      Finished:     Mon, 06 Nov 2023 18:48:34 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-f56b5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-f56b5:
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
  Normal  Scheduled  2m47s  default-scheduler  Successfully assigned default/python-preinstall-hook to minikube
  Normal  Pulled     2m47s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m47s  kubelet            Created container pre-install-container
  Normal  Started    2m47s  kubelet            Started container pre-install-container
````

### Describe post-install hooks
Python
````
kubectl describe po python-postinstall-hook
````
Output:
````
Name:         python-postinstall-hook
Namespace:    default
Priority:     0
Node:         minikube/192.168.48.2
Start Time:   Mon, 06 Nov 2023 18:48:36 +0300
Labels:       <none>
Annotations:  helm.sh/hook: post-install
Status:       Succeeded
IP:           10.244.0.136
IPs:
  IP:  10.244.0.136
Containers:
  post-install-container:
    Container ID:  docker://745eabd08444d33ad6500cc75f2402b9b682bc806cd87affd2b79cc678a849f4
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977efdfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 15
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Mon, 06 Nov 2023 20:48:40 +0300
      Finished:     Mon, 06 Nov 2023 20:48:55 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mzr5q (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mzr5q:
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
  Normal  Scheduled  5m26s  default-scheduler  Successfully assigned default/python-postinstall-hook to minikube
  Normal  Pulling    5m25s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m23s  kubelet            Successfully pulled image "busybox" in 2.096710746s (2.096723995s including waiting)
  Normal  Created    5m22s  kubelet            Created container post-install-container
  Normal  Started    5m22s  kubelet            Started container post-install-container
````

## Delete hooks policy 
Added `"helm.sh/hook-delete-policy": hook-succeeded` annotation to `pre-install-hook.yaml` and `post-install-hook.yaml` files.
After reinstalling:
````
kubectl get po            
````
Output:
````
NAME                          READY   STATUS    RESTARTS   AGE
app_python-76c869585d-2q9tl   1/1     Running   0          8m15s
app_python-76c869585d-7w64n   1/1     Running   0          8m15s
app_python-76c869585d-flp5r   1/1     Running   0          8m15s
````
Pods:
````
kubectl get pods,svc
````
Output:
````
NAME                              READY   STATUS    RESTARTS   AGE
pod/app_python-76c869585d-2q9tl   1/1     Running   0          8m58s
pod/app_python-76c869585d-7w64n   1/1     Running   0          8m58s
pod/app_python-76c869585d-flp5r   1/1     Running   0          8m58s
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app_python   LoadBalancer   10.106.157.28   <pending>     8080:30377/TCP   8m58s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          95m
````

## Library chart
* Created simple library chart in `library-chart` directory.
* Added dependencies to `Chart.yaml` file:
    ````
    dependencies:
      - name: library-chart
        version: 1.0.0
        repository: file://../library-chart
    ````
* Updating dependencies:
  * Python:
      ```
      helm dependency update app_python/
      ```
    Output:
    ````
    Hang tight while we grab the latest from your chart repositories...
    ...Successfully got an update from the "bitnami" chart repository
    Update Complete. ⎈Happy Helming!⎈
    Saving 1 charts
    Deleting outdated charts
    ````
* Updating labels in `templates/deployment.yaml`:
  ````
  {{- include "library-chart.labels" . | indent 4 }}
  ````