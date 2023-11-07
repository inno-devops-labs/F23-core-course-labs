

## 1. Setup

```bash
❯ helm install app-python ./
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /Users/nikitosing/.kube/config
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /Users/nikitosing/.kube/config
NAME: app-python
LAST DEPLOYED: Tue Nov  7 22:05:50 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=app-python,app.kubernetes.io/instance=app-python" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

```bash
❯  kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-68bd86b98f-rmpwz   1/1     Running   0          48s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python   LoadBalancer   10.104.130.145   <pending>     80:31116/TCP   48s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        8m41s
```


## 2. Hooks

```bash
❯ kubectl get po
NAME                                     READY   STATUS      RESTARTS   AGE
app-python-68bd86b98f-rmpwz              1/1     Running     0          23m
helm-hooks-app-python-79bff4bbc4-2n55q   1/1     Running     0          58s
postinstall-hook                         0/1     Completed   0          58s
preinstall-hook                          0/1     Completed   0          86s
❯ kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.105.2
Start Time:       Tue, 07 Nov 2023 22:29:20 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.45
IPs:
  IP:  10.244.0.45
Containers:
  pre-install-container:
    Container ID:  docker://d2119bc95e52b890e2b2b04aee7bfecb0baf60544881914a0d338c18de8c7209
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
      Started:      Tue, 07 Nov 2023 22:29:25 +0300
      Finished:     Tue, 07 Nov 2023 22:29:45 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-lk9ms (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-lk9ms:
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
  Normal  Scheduled  95s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    95s   kubelet            Pulling image "busybox"
  Normal  Pulled     91s   kubelet            Successfully pulled image "busybox" in 4.655129509s (4.655138801s including waiting)
  Normal  Created    91s   kubelet            Created container pre-install-container
  Normal  Started    91s   kubelet            Started container pre-install-container
❯ kubectl describe po postinstall-hook
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.105.2
Start Time:       Tue, 07 Nov 2023 22:29:48 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.47
IPs:
  IP:  10.244.0.47
Containers:
  post-install-container:
    Container ID:  docker://c2c45783d2f41f865890addf8a037cc2757206e84a08882e21dac4746cc7f760
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
      Started:      Tue, 07 Nov 2023 22:29:50 +0300
      Finished:     Tue, 07 Nov 2023 22:30:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-km79b (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-km79b:
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
  Normal  Scheduled  91s   default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    91s   kubelet            Pulling image "busybox"
  Normal  Pulled     89s   kubelet            Successfully pulled image "busybox" in 1.422698542s (1.422713335s including waiting)
  Normal  Created    89s   kubelet            Created container post-install-container
  Normal  Started    89s   kubelet            Started container post-install-container
```


### Before adding hooks deletion policy

```bash
❯ kubectl get pods,svc
NAME                                         READY   STATUS      RESTARTS   AGE
pod/app-python-68bd86b98f-rmpwz              1/1     Running     0          36m
pod/helm-hooks-app-python-79bff4bbc4-2n55q   1/1     Running     0          14m
pod/postinstall-hook                         0/1     Completed   0          14m
pod/preinstall-hook                          0/1     Completed   0          15m

NAME                            TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python              LoadBalancer   10.104.130.145   <pending>     80:31116/TCP   36m
service/helm-hooks-app-python   LoadBalancer   10.103.184.47    <pending>     80:31956/TCP   14m
service/kubernetes              ClusterIP      10.96.0.1        <none>        443/TCP        44m
```

### After adding hooks deletion policy

```bash
❯ kubectl get pods,svc
NAME                                READY   STATUS    RESTARTS   AGE
pod/app-python-1-59cb6b664c-xjh96   1/1     Running   0          14s

NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-python-1   LoadBalancer   10.110.198.243   <pending>     80:30750/TCP   14s
service/kubernetes     ClusterIP      10.96.0.1        <none>        443/TCP        51m
```