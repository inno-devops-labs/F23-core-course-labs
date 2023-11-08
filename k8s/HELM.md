# Helm
The lab is completed including the bonus task

* Instead of creating two seperate charts, one flexible chart is created and files `deployment.yml`,  `ingress.yml` and `service.yml` from the last lab are brought with a bit of change. 
* Two `values` files are added for two applicaitons:
    * `values.python.yaml`
    * `values.go.yaml`
* If you wanna create a chart for your application you just need to create a file `values.<app_name>.yaml`, fill it with proper information and run the following code:
    * `helm install <app_name> ./my-helm-app --values values.<app_name>.yaml`

## Outputs

### `kubectl get pods,svc`:
```
NAME                              READY   STATUS      RESTARTS   AGE
pod/postinstall-hook              0/1     Completed   0          35s
pod/preinstall-hook               0/1     Completed   0          45s
pod/python-app-595db68d7c-9dptr   1/1     Running     0          35s

NAME                         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1      <none>        443/TCP          112d
service/python-web-app-svc   LoadBalancer   10.108.222.9   <pending>     5000:30143/TCP   35s

```

### `kubectl describe po preinstall-hook`:
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 10:24:10 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.24
IPs:
  IP:  10.244.0.24
Containers:
  pre-install-container:
    Container ID:  containerd://7296c41bdf5bacfb3df15ebc302375f73ceb02fae268258ffb6b84347f851170
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 10:24:11 +0300
      Finished:     Wed, 08 Nov 2023 10:24:16 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mmj4d (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-mmj4d:
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
  Normal  Scheduled  85s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     85s   kubelet            Container image "busybox" already present on machine
  Normal  Created    85s   kubelet            Created container pre-install-container
  Normal  Started    85s   kubelet            Started container pre-install-container
```


### `kubectl describe po postinstall-hook`:
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 10:24:20 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.26
IPs:
  IP:  10.244.0.26
Containers:
  post-install-container:
    Container ID:  containerd://7d86c640a90c4aa0d474a4dbd0c43a524a92a2b788091a97d2be7501963607f2
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 5
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 08 Nov 2023 10:24:23 +0300
      Finished:     Wed, 08 Nov 2023 10:24:28 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4hvt6 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-4hvt6:
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
  Normal  Scheduled  105s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    105s  kubelet            Pulling image "busybox"
  Normal  Pulled     102s  kubelet            Successfully pulled image "busybox" in 1.320434291s (2.624798923s including waiting)
  Normal  Created    102s  kubelet            Created container post-install-container
  Normal  Started    102s  kubelet            Started container post-install-container
```