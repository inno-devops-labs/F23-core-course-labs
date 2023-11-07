## Deploying app-python

Following the provided example

```text
$ helm create app-python
Creating app-python
$ helm package app-python
Successfully packaged chart and saved it to: /Users/max/OneDrive/Документы/GitHub/devops-labs/k8s/app-python-0.1.0.tgz
$ helm install app-python ./app-python-0.1.0.tgz
NAME: app-python
LAST DEPLOYED: Tue Nov  7 18:07:35 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w app-python'
  export SERVICE_IP=$(kubectl get svc --namespace default app-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:80
```

Running the service

```text
$ minikube service app-python
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | app-python | http/80     | http://192.168.49.2:31245 |
|-----------|------------|-------------|---------------------------|
🏃  Starting tunnel for service app-python.
|-----------|------------|-------------|------------------------|
| NAMESPACE |    NAME    | TARGET PORT |          URL           |
|-----------|------------|-------------|------------------------|
| default   | app-python |             | http://127.0.0.1:62608 |
|-----------|------------|-------------|------------------------|
🎉  Opening service default/app-python in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

Checking pods and services

```text
$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-5db5bc5cfb-7jrwc   1/1     Running   0          5m39s
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/app-python   LoadBalancer   10.107.74.169   <pending>     80:31245/TCP   5m40s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP        33m
```

## [Bonus] Deploying app-go

Following the provided example

```text
$ helm create app-go
Creating app-go
$ helm package app-go
Successfully packaged chart and saved it to: /Users/max/OneDrive/Документы/GitHub/devops-labs/k8s/app-go-0.1.0.tgz
$ helm install app-go ./app-go-0.1.0.tgz
NAME: app-go
LAST DEPLOYED: Tue Nov  7 19:32:07 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w app-go'
  export SERVICE_IP=$(kubectl get svc --namespace default app-go --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:80
```

Running the service

```text
$ minikube service app-go
|-----------|----------|-------------|---------------------------|
| NAMESPACE |   NAME   | TARGET PORT |            URL            |
|-----------|----------|-------------|---------------------------|
| default   | app-go | http/80     | http://192.168.49.2:30732 |
|-----------|----------|-------------|---------------------------|
🏃  Starting tunnel for service app-go.
|-----------|----------|-------------|------------------------|
| NAMESPACE |   NAME   | TARGET PORT |          URL           |
|-----------|----------|-------------|------------------------|
| default   | app-go |             | http://127.0.0.1:49289 |
|-----------|----------|-------------|------------------------|
🎉  Opening service default/app-go in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

Checking pods and services

```
$ kubectl get pods,svc
```

```text
NAME                          READY   STATUS    RESTARTS   AGE
pod/app-go-58d8d488-tdnsh   1/1     Running   0          7m
NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/app-go     LoadBalancer   10.98.79.229   <pending>     80:30732/TCP   7m
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP        10m
```

## Helm Chart Hooks

```
$ kubectl get po
```
```text
NAME                         READY    STATUS   RESTARTS      AGE
app-python-5db5bc5cfb-7jrwc   1/1     Running     0          19s
app-python-5db5bc5cfb-j8qtk   1/1     Running     0          19s
app-python-5db5bc5cfb-x27mb   1/1     Running     0          19s
python-post-install-v6t6d     0/1     Completed   0          19s
python-pre-install-kzy5c      0/1     Completed   0          31s
```

```
$ kubectl describe po python-pre-install
```

```text
Name:             python-pre-install-kzy5c
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 19:32:47 +0300
Labels:           app.kubernetes.io/instance=python
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=96d4047f-37c4-4e50-b371-5f8d76a5eaab
                  batch.kubernetes.io/job-name=python-pre-install
                  controller-uid=96d4047f-37c4-4e50-b371-5f8d76a5eaab
                  helm.sh/chart=app-python-0.1.0
                  job-name=python-pre-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.58
IPs:
  IP:           10.244.0.58
Controlled By:  Job/python-pre-install
Containers:
  pre-install-job:
    Container ID:  docker://bb3ff0234b5c6ff995413d08a4ba5bbbc5d5dc030b1bf0640dddef3f7c0c8b11
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 19:32:51 +0300
      Finished:     Tue, 07 Nov 2023 19:32:54 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mspd6 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mspd6:
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
  Normal  Scheduled  3m55s  default-scheduler  Successfully assigned default/python-pre-install-kzy5c to minikube
  Normal  Pulling    3m55s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m53s  kubelet            Successfully pulled image "busybox" in 2.33875736s (2.338768418s including waiting)
  Normal  Created    3m53s  kubelet            Created container pre-install-job
  Normal  Started    3m53s  kubelet            Started container pre-install-job
```

```  
$ kubectl describe po python-post-install
```

```text
Name:             python-post-install-v6t6d
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 19:32:59 +0300
Labels:           app.kubernetes.io/instance=python
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=242ff093-b31b-45bd-b6ed-83e94f756277
                  batch.kubernetes.io/job-name=python-post-install
                  controller-uid=242ff093-b31b-45bd-b6ed-83e94f756277
                  helm.sh/chart=app-python-0.1.0
                  job-name=python-post-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.62
IPs:
  IP:           10.244.0.62
Controlled By:  Job/python-post-install
Containers:
  post-install-job:
    Container ID:  docker://1c3a6457dc484d1e3073927b9f70963d321de207fbe84a79fba2712501459416
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 19:33:04 +0300
      Finished:     Tue, 07 Nov 2023 19:33:10 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-tqxq6 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-tqxq6:
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
  Normal  Scheduled  6m59s  default-scheduler  Successfully assigned default/python-post-install-v6t6d to minikube
  Normal  Pulling    6m59s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m57s  kubelet            Successfully pulled image "busybox" in 1.966357395s (1.966365369s including waiting)
  Normal  Created    6m57s  kubelet            Created container post-install-job
  Normal  Started    6m57s  kubelet            Started container post-install-job
```

## [Bonus] Helm definitions

- Library Charts — are used to share some common definitions across Helm templates — they are very helpful to avoid repetition in code
- Umbrella Charts — describe a collection of k8s components as a Helm chart. Provide a way to deploy a collection of components atomically
