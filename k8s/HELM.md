## pods
```
zrrrget@dungeon:~/projects/core-course-labs/k8s$ kubectl get pods,svc
NAME                                     READY   STATUS    RESTARTS   AGE
pod/bash-app-bash-5cf798d5b9-bbswh       1/1     Running   0          56s
pod/python-app-python-5b8f4fd494-bmxcq   1/1     Running   0          13m
pod/python-app-python-5b8f4fd494-q6fgx   1/1     Running   0          13m
pod/python-app-python-5b8f4fd494-r642w   1/1     Running   0          13m

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/bash-app-bash       LoadBalancer   10.100.12.216   <pending>     9000:30064/TCP   56s
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          6d22h
service/python-app-python   LoadBalancer   10.98.134.164   <pending>     8000:32455/TCP   13m
```
## Hooks
```
zrrrget@dungeon:~/projects/core-course-labs/k8s$ kubectl describe po python-pre-install
Name:             python-pre-install-pkbz8
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 00:43:58 +0300
Labels:           app.kubernetes.io/instance=python
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=ffdeaa53-6f11-4528-934e-b6968a319908
                  batch.kubernetes.io/job-name=python-pre-install
                  controller-uid=ffdeaa53-6f11-4528-934e-b6968a319908
                  helm.sh/chart=app-python-0.1.0
                  job-name=python-pre-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.75
IPs:
  IP:           10.244.0.75
Controlled By:  Job/python-pre-install
Containers:
  pre-install-job:
    Container ID:  docker://af5671aa4e4994aa21fc138ed22087d41f6f3de6692853685ba040f730e61b85
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
      Started:      Wed, 08 Nov 2023 00:44:00 +0300
      Finished:     Wed, 08 Nov 2023 00:44:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xzls4 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-xzls4:
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
  Normal  Scheduled  31s   default-scheduler  Successfully assigned default/python-pre-install-pkbz8 to minikube
  Normal  Pulling    31s   kubelet            Pulling image "busybox"
  Normal  Pulled     29s   kubelet            Successfully pulled image "busybox" in 1.650011688s (1.65002329s including waiting)
  Normal  Created    29s   kubelet            Created container pre-install-job
  Normal  Started    29s   kubelet            Started container pre-install-job

zrrrget@dungeon:~/projects/core-course-labs/k8s$ kubectl describe po python-post-install
Name:             python-post-install-8z9dw
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 00:44:08 +0300
Labels:           app.kubernetes.io/instance=python
                  app.kubernetes.io/managed-by=Helm
                  batch.kubernetes.io/controller-uid=9914d55e-5da6-4d8e-9d52-5b4aba37e98c
                  batch.kubernetes.io/job-name=python-post-install
                  controller-uid=9914d55e-5da6-4d8e-9d52-5b4aba37e98c
                  helm.sh/chart=app-python-0.1.0
                  job-name=python-post-install
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.79
IPs:
  IP:           10.244.0.79
Controlled By:  Job/python-post-install
Containers:
  post-install-job:
    Container ID:  docker://2a1602d6af09ecc40648bc11f870ecf1eb0cd680917e20a3887889aed3836f47
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
      Started:      Wed, 08 Nov 2023 00:44:11 +0300
      Finished:     Wed, 08 Nov 2023 00:44:16 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7m9lt (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-7m9lt:
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
  Normal  Scheduled  26s   default-scheduler  Successfully assigned default/python-post-install-8z9dw to minikube
  Normal  Pulling    26s   kubelet            Pulling image "busybox"
  Normal  Pulled     24s   kubelet            Successfully pulled image "busybox" in 1.843642314s (1.843655739s including waiting)
  Normal  Created    24s   kubelet            Created container post-install-job
  Normal  Started    24s   kubelet            Started container post-install-job
zrrrget@dungeon:~/projects/core-course-labs/k8s$ kubectl get po
NAME                                 READY   STATUS      RESTARTS        AGE
bash-app-bash-5cf798d5b9-wdzsw       1/1     Running     8 (5m37s ago)   17m
python-app-python-5b8f4fd494-89hst   1/1     Running     0               85s
python-app-python-5b8f4fd494-nbcl9   1/1     Running     0               85s
python-app-python-5b8f4fd494-s8ww8   1/1     Running     0               85s
python-post-install-8z9dw            0/1     Completed   0               85s
python-pre-install-pkbz8             0/1     Completed   0               95s
zrrrget@dungeon:~/projects/core-course-labs/k8s$ 
```