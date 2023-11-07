## Output

### Without hooks
`> kubectl get pods,svc`
```
NAME                                         READY   STATUS    RESTARTS      AGE
pod/python-app-7c5df44694-hc98r              1/1     Running   0             4m10s
pod/python-app-7c5df44694-k48lq              1/1     Running   0             4m10s
pod/python-app-7c5df44694-r4m99              1/1     Running   0             4m10s
pod/python-app-deployment-5f4cf84b6d-2l2bg   1/1     Running   1 (14m ago)   6d22h
pod/python-app-deployment-5f4cf84b6d-tslpn   1/1     Running   1 (14m ago)   6d22h
pod/python-app-deployment-5f4cf84b6d-w2vxp   1/1     Running   1 (14m ago)   6d22h

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP        6d23h
service/python-app           ClusterIP      10.99.141.30   <none>        5000/TCP       4m10s
service/python-app-service   LoadBalancer   10.105.21.98   <pending>     80:31530/TCP   6d22h
```

### With hooks
`> kubectl get pods,svc`
```
NAME                                         READY   STATUS      RESTARTS      AGE
pod/postinstall-hook                         0/1     Completed   0             3m10s
pod/preinstall-hook                          0/1     Completed   0             3m27s
pod/python-app-7c5df44694-m727f              1/1     Running     0             3m10s
pod/python-app-7c5df44694-r9zht              1/1     Running     0             3m10s
pod/python-app-7c5df44694-s5prx              1/1     Running     0             3m10s
pod/python-app-deployment-5f4cf84b6d-2l2bg   1/1     Running     1 (43m ago)   6d23h
pod/python-app-deployment-5f4cf84b6d-tslpn   1/1     Running     1 (43m ago)   6d23h
pod/python-app-deployment-5f4cf84b6d-w2vxp   1/1     Running     1 (43m ago)   6d23h

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          6d23h
service/python-app           LoadBalancer   10.102.153.12   <pending>     5000:30151/TCP   3m10s
service/python-app-service   LoadBalancer   10.105.21.98    <pending>     80:31530/TCP     6d23h
```

`> kubectl get po`
```
NAME                                     READY   STATUS      RESTARTS      AGE
postinstall-hook                         0/1     Completed   0             38s
preinstall-hook                          0/1     Completed   0             55s
python-app-7c5df44694-m727f              1/1     Running     0             38s
python-app-7c5df44694-r9zht              1/1     Running     0             38s
python-app-7c5df44694-s5prx              1/1     Running     0             38s
python-app-deployment-5f4cf84b6d-2l2bg   1/1     Running     1 (40m ago)   6d23h
python-app-deployment-5f4cf84b6d-tslpn   1/1     Running     1 (40m ago)   6d23h
python-app-deployment-5f4cf84b6d-w2vxp   1/1     Running     1 (40m ago)   6d23h
```

`> kubectl describe po preinstall-hook`
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 21:02:37 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.28
IPs:
  IP:  10.244.0.28
Containers:
  pre-install-container:
    Container ID:  docker://71761f943a24d037f08bc1a1601804157f22f962dcaa80199251fdedacb1ab27
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
      Started:      Tue, 07 Nov 2023 21:02:48 +0300
      Finished:     Tue, 07 Nov 2023 21:02:53 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-rt2gj (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-rt2gj:
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
  Normal  Scheduled  86s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    86s   kubelet            Pulling image "busybox"
  Normal  Pulled     76s   kubelet            Successfully pulled image "busybox" in 10.338079644s (10.338095289s including waiting)
  Normal  Created    76s   kubelet            Created container pre-install-container
  Normal  Started    76s   kubelet            Started container pre-install-container
```

`> kubectl describe po postinstall-hook`
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 21:02:54 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.32
IPs:
  IP:  10.244.0.32
Containers:
  post-install-container:
    Container ID:  docker://79f76ca72cd55bf068477fec59494c7d46a6dcf57414c57c0c01a0c512209fec
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
      Started:      Tue, 07 Nov 2023 21:02:58 +0300
      Finished:     Tue, 07 Nov 2023 21:03:03 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-9h2dm (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-9h2dm:
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
  Normal  Scheduled  2m31s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m31s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m28s  kubelet            Successfully pulled image "busybox" in 3.448704244s (3.448720309s including waiting)
  Normal  Created    2m28s  kubelet            Created container post-install-container
  Normal  Started    2m28s  kubelet            Started container post-install-container
```