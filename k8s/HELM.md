# Task 1
install dashboard:
``` 
helm install python . --values values.python.yml
```
```
NAME: python
LAST DEPLOYED: Tue Nov  7 19:36:42 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://python.timer.app/
```
## access application
```
 minikube service python-python-app
```
```
|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | python-python-app | http/5000   | http://192.168.49.2:30833 |
|-----------|-------------------|-------------|---------------------------|
🎉  Opening service default/python-python-app in default browser...
```
![img_4.png](img_4.png)


## Check application
```
kubectl get pods,svc
```
```
NAME                                    READY   STATUS    RESTARTS   AGE
pod/python-python-app-fcc5d5664-7r69n   1/1     Running   0          13m
pod/python-python-app-fcc5d5664-d8zg5   1/1     Running   0          13m
pod/python-python-app-fcc5d5664-jdpjt   1/1     Running   0          13m

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/kubernetes          ClusterIP      10.96.0.1       <none>          443/TCP          23m
service/python-python-app   LoadBalancer   10.108.115.52   10.108.115.52   5000:30833/TCP   13m
```
![img_5.png](img_5.png)
# Task 2 
1. lint 
```
helm lint python-app
```
```
==> Linting python-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```
2. install with dry-run
```
 helm install --dry-run helm-hooks python-app
NAME: helm-hooks
LAST DEPLOYED: Tue Nov  7 20:49:35 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: python-app/templates/post-install-hook.yaml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
...
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
3. install hooks
```
helm install helm-hooks ./python-app
```
```
NAME: helm-hooks
LAST DEPLOYED: Tue Nov  7 21:09:49 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-app,app.kubernetes.io/instance=helm-hooks" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
4. results
```
kubectl get po
```
```
NAME                                    READY   STATUS      RESTARTS   AGE
helm-hooks-python-app-864679bc9-zvrzj   1/1     Running     0          83s
postinstall-hook                        0/1     Completed   0          83s
preinstall-hook                         0/1     Completed   0          106s
```

```
kubectl describe po preinstall-hook
```
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 21:30:10 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.73
IPs:
  IP:  10.244.0.73
Containers:
  pre-install-container:
    Container ID:  docker://5831edc136137a5f7349cb5c9efe055d91868b97dadb9147903142a750892881
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
      Started:      Wed, 08 Nov 2023 21:30:11 +0300
      Finished:     Wed, 08 Nov 2023 21:30:31 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-kdxcq (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-kdxcq:
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
  Normal  Scheduled  6m4s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     6m4s  kubelet            Container image "busybox" already present on machine
  Normal  Created    6m4s  kubelet            Created container pre-install-container
  Normal  Started    6m4s  kubelet            Started container pre-install-container

```
```
kubectl describe po postinstall-hook
```

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 21:30:33 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.77
IPs:
  IP:  10.244.0.77
Containers:
  post-install-container:
    Container ID:  docker://9476bdaf9ab32c8d77fff18d6b209ec0d80cc73555ca1a2bb086e1f78cb255fb
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
      Started:      Wed, 08 Nov 2023 21:30:39 +0300
      Finished:     Wed, 08 Nov 2023 21:30:54 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pcdrr (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-pcdrr:
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
  Normal  Scheduled  4m34s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    4m32s  kubelet            Pulling image "busybox"
  Normal  Pulled     4m29s  kubelet            Successfully pulled image "busybox" in 3.502129762s (3.502170728s including waiting)
  Normal  Created    4m28s  kubelet            Created container post-install-container
  Normal  Started    4m28s  kubelet            Started container post-install-container
```
As we can see - hooks are completed, so we achieve desired results

5. delete policy

- Provided policy is enough
 ``` 
"helm.sh/hook-delete-policy": hook-succeeded
```
# Bonus task
## Extending for app_cpp
### Install
```
helm install cpp ./python-app/ --values python-app/values.cpp.yml
```
```
NAME: cpp
LAST DEPLOYED: Tue Nov  7 21:30:24 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://guess.game.cpp.app/
```
### Check
```
kubectl get pods,svc
```

```
NAME                                    READY   STATUS    RESTARTS      AGE
pod/cpp-python-app-6fb64b6bd6-2jmhx     0/1     Running   1 (57s ago)   118s
pod/cpp-python-app-6fb64b6bd6-75f24     0/1     Running   1 (57s ago)   118s
pod/cpp-python-app-6fb64b6bd6-t4qmb     0/1     Running   1 (57s ago)   118s
pod/python-python-app-fcc5d5664-fhwgj   1/1     Running   0             28s
pod/python-python-app-fcc5d5664-n48mk   1/1     Running   0             28s
pod/python-python-app-fcc5d5664-w2n4t   1/1     Running   0             28s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/cpp-python-app      LoadBalancer   10.99.229.94    10.99.229.94    5000:32433/TCP   118s
service/kubernetes          ClusterIP      10.96.0.1       <none>          443/TCP          125m
service/python-python-app   LoadBalancer   10.103.27.251   10.103.27.251   5000:31901/TCP   28s
```
```minikube service --all```
```
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | cpp-python-app | http/10000  | http://192.168.49.2:32722 |
|-----------|----------------|-------------|---------------------------|
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | python-python-app | http/5000   | http://192.168.49.2:31901 |
|-----------|-------------------|-------------|---------------------------|
🎉  Opening service default/cpp-python-app in default browser...
🎉  Opening service default/python-python-app in default browser...
ruslan@Elestrias:~/Downloads/devops/core-course-labs/k8s$ Opening in existing browser session.
```
![img_6.png](img_6.png)
![img_7.png](img_7.png)

## Chart library
### Completing task
1. I have created new chart
2. Remove all from template + values.yml
3. add to dependencies of application chart
4. update deps for chart
```
helm dependency update
```

```
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts

```
5. Install chart with dependencies and add to ```labes:``` part in deployment script

### Results
```
kubectl describe po
```
Part  with python labels
```
Name:             python-python-app-5484f6dbb8-xrjtf
Namespace:        default
Priority:         0
Service Account:  python-python-app
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 22:51:07 +0300
Labels:           absolutely_not_default=super_label
                  app.kubernetes.io/instance=python
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=python-app
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=python-app-0.1.0
                  pod-template-hash=5484f6dbb8

```
Part with cpp labels
```
Name:             cpp-python-app-7d48b9ddcd-t2zhb
Namespace:        default
Priority:         0
Service Account:  cpp-python-app
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 22:54:40 +0300
Labels:           absolutely_not_default=super_label
                  app.kubernetes.io/instance=cpp
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=python-app
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=python-app-0.1.0
                  pod-template-hash=7d48b9ddcd

```
