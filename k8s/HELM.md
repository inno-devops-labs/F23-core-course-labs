## COnfiguration


### Python
```
>>> helm install python . --values values.python.yaml
NAME: python
LAST DEPLOYED: Wed Nov  1 15:13:25 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://python.app/
```

### Typescript
```
>>> helm install typescript . --values values.typescript.yaml
NAME: typescript
LAST DEPLOYED: Wed Nov  1 15:19:47 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://typescript.app/
```

```
>>> helm list
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
python          default         1               2023-11-01 21:42:53.914917216 +0300 MSK deployed        helm-app-0.1.0  1.16.0
typescript      default         1               2023-11-01 22:25:12.492188639 +0300 MSK deployed        helm-app-0.1.0  1.16.0
```

### Checking pods
```
>>> kubectl get all
NAME                                  READY   STATUS    RESTARTS   AGE
pod/python-app-5946bc9c94-4tdzs       1/1     Running   0          42m
pod/python-app-5946bc9c94-pph9d       1/1     Running   0          42m
pod/python-app-5946bc9c94-q8z9d       1/1     Running   0          42m
pod/typescript-app-578744c658-5wtwh   1/1     Running   0          31s
pod/typescript-app-578744c658-d2l7h   1/1     Running   0          31s
pod/typescript-app-578744c658-drc55   1/1     Running   0          31s

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          49m
service/python-app-svc       LoadBalancer   10.102.60.70    <pending>     8000:30191/TCP   42m
service/typescript-app-svc   LoadBalancer   10.103.63.226   <pending>     5137:32033/TCP   31s

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/python-app       3/3     3            3           42m
deployment.apps/typescript-app   3/3     3            3           31s

NAME                                        DESIRED   CURRENT   READY   AGE
replicaset.apps/python-app-5946bc9c94       3         3         3       42m
replicaset.apps/typescript-app-578744c658   3         3         3       31s
```



## Task 2

```
>>> helm lint helm-app
==> Linting helm-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```


```
>>> helm install --dry-run helm-hooks ./helm-app
NAME: helm-hooks
LAST DEPLOYED: Wed Nov  1 23:42:46 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
HOOKS:
```

```
>>> kubectl get po
NAME                              READY   STATUS      RESTARTS   AGE
nginx-app-69ccf856dd-f4rlq        1/1     Running     0          3m21s
post-install-hook                 0/1     Completed   0          37s
pre-install-hook                  0/1     Completed   0          67s
python-app-5946bc9c94-4tdzs       1/1     Running     0          126m
python-app-5946bc9c94-pph9d       1/1     Running     0          126m
python-app-5946bc9c94-q8z9d       1/1     Running     0          126m
typescript-app-578744c658-5wtwh   1/1     Running     0          83m
typescript-app-578744c658-d2l7h   1/1     Running     0          83m
typescript-app-578744c658-drc55   1/1     Running     0          83m
```


### kubectl describe po pre-install-hook
```
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.64.2
Start Time:       Wed Nov  1 23:54:12 2023
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.102.60.42
IPs:
  IP:  10.102.60.42
Containers:
  pre-install-container:
    Container ID:  docker://9e109867575333d00dab5a42a598b1caa44921c02affa8294eacb41abasdaj33
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:283jkasc632167424a6d997e74f52b878d7cc478225cffac6bc977ksdahhjdase42
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed Nov  1 23:54:55 2023 +0300
      Finished:     Wed Nov  1 23:54:56 2023 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-xgx9l (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-xgx9l:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3602
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
  Normal  Scheduled  2m5s   default-scheduler  Successfully assigned default/pre-install-hook to minikube
  Normal  Pulling    1m4s   kubelet            Pulling image "busybox"
  Normal  Pulled     2m43s  kubelet            Successfully pulled image "busybox" in 3.3201205s (4.3201205s including waiting)
  Normal  Created    3m1s  kubelet            Created container pre-install-container
  Normal  Started    3m54s  kubelet            Started container pre-install-container
```


### kubectl describe po post-install-hook

```
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed Nov  1 23:54:56 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.102.60.43
IPs:
  IP:  10.102.60.43
Containers:
  post-install-container:
    Container ID:  docker://9e109867575333d00dab5a42a598b1caa44921c02affa8294eacb41abasdaj33
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:283jkasc632167424a6d997e74f52b878d7cc478225cffac6bc977ksdahhjdase42
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed Nov  1 23:56:43 +0300
      Finished:     Wed Nov  1 23:56:43 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7qtpz (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-7qtpz:
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
  Normal  Scheduled  2m12s  default-scheduler  Successfully assigned default/post-install-hook to minikube
  Normal  Pulling    2m11s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m9s   kubelet            Successfully pulled image "busybox" in 2.525182475s (2.525191793s including waiting)
  Normal  Created    2m1s   kubelet            Created container post-install-container
  Normal  Started    2m1s   kubelet            Started container post-install-container
```

### Hook Delete Policy

added `"helm.sh/hook-delete-policy": hook-succeeded`

# Bonus Task

Implemented Helm Chart for Extra App: `values.typescript.yaml`

Created library-chart/

Library charts:
```
>>> helm dependency update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```
