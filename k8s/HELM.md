# Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

3. Create Your Own Helm Chart:

Generate a Helm chart for your application.

```
helm create app-python
```

I had to update paths for `livenessProbe` and `readinessProbe` so they can poll the `/time` endpoint.

4. Install your helm chart:

`helm install app-python-chart app-python -f app-python/values.yaml`

Verify this by checking the Workloads page in the Minikube dashboard:

![Workloads](https://i.imgur.com/TcFgkd2.png)

5. Access your application:
```
minikube service app-python-chart
```

Access the app:
![minikube service](https://i.imgur.com/ATliXqm.png)

App in browser:
![App](https://i.imgur.com/gR9Ab6D.png)

6. Create a HELM.md File with outputs: done
```
$ kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/app-python-chart-7975466f9-m9fvq   1/1     Running   0          27m

NAME                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/app-python-chart   NodePort    10.98.128.252   <none>        80:32251/TCP   35m
service/kubernetes         ClusterIP   10.96.0.1       <none>        443/TCP        7d4h
```


## Task 2: Helm Chart Hooks

4. Provide output:

```
$ kubectl get pods
NAME                                     READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-5dcf4cdcf7-lgvgk   1/1     Running     0          4m31s
postinstall-hook                         0/1     Completed   0          4m31s
preinstall-hook                          0/1     Completed   0          4m48s
```

```
$ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 01:29:33 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.40
IPs:
  IP:  10.244.0.40
Containers:
  pre-install-container:
    Container ID:  docker://2f0d68a26ef9574bd1e147c75e6df2f605d476dee5f1dce0df28706acfd92184
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
      Started:      Wed, 08 Nov 2023 01:29:39 +0300
      Finished:     Wed, 08 Nov 2023 01:29:49 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jspwn (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-jspwn:
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
  Normal  Scheduled  6m10s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    6m10s  kubelet            Pulling image "busybox"
  Normal  Pulled     6m5s   kubelet            Successfully pulled image "busybox" in 4.802839478s (4.802850289s including waiting)
  Normal  Created    6m5s   kubelet            Created container pre-install-container
  Normal  Started    6m5s   kubelet            Started container pre-install-container
  ```

```
$ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 01:29:50 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.41
IPs:
  IP:  10.244.0.41
Containers:
  post-install-container:
    Container ID:  docker://1292f4fd12c733065b334ad0c5e5330cd397c541bbfd8a12c3db271bc07e573f
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
      Started:      Wed, 08 Nov 2023 01:29:53 +0300
      Finished:     Wed, 08 Nov 2023 01:30:08 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-stcm9 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-stcm9:
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
  Normal  Scheduled  5m4s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    5m4s  kubelet            Pulling image "busybox"
  Normal  Pulled     5m2s  kubelet            Successfully pulled image "busybox" in 1.977649388s (1.977660549s including waiting)
  Normal  Created    5m2s  kubelet            Created container post-install-container
  Normal  Started    5m2s  kubelet            Started container post-install-container
  ```


5. Hook Delete Policy:

To accomplish this, I add `"helm.sh/hook-delete-policy": hook-succeeded,hook-failed` annotation to both hooks.

Now check pods again:
```
$ kubectl get po
NAME                                     READY   STATUS    RESTARTS   AGE
helm-hooks-app-python-5dcf4cdcf7-pkjf2   1/1     Running   0          27s
```

```
$ kubectl describe po preinstall-hook
Error from server (NotFound): pods "preinstall-hook" not found
```

```
$ kubectl describe po postinstall-hook
Error from server (NotFound): pods "postinstall-hook" not found
```