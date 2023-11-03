# HELM installation

### Python app
```
>>> helm install python . --values values.python.yaml
NAME: python
LAST DEPLOYED: Fri Nov  3 16:31:49 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://python.app/
```

### Typescript app
```
>>> helm install typescript . --values values.typescript.yaml
NAME: typescript
LAST DEPLOYED: Fri Nov  3 16:32:32 2023
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
python          default         1               2023-11-03 16:31:49.339981995 +0300 MSK deployed        mywebapps-0.1.0 1.16.0
typescript      default         1               2023-11-03 16:32:32.353172998 +0300 MSK deployed        mywebapps-0.1.0 1.16.0
```

### Display running pods and services
```
>>> kubectl get all
NAME                                  READY   STATUS    RESTARTS   AGE
pod/python-app-fc4cb86cf-b5f7d        1/1     Running   0          4m4s
pod/python-app-fc4cb86cf-gtjcq        1/1     Running   0          4m4s
pod/python-app-fc4cb86cf-q5sr4        1/1     Running   0          4m4s
pod/typescript-app-7cfd496848-bj98c   1/1     Running   0          3m21s
pod/typescript-app-7cfd496848-h2cqf   1/1     Running   0          3m21s
pod/typescript-app-7cfd496848-n9mzp   1/1     Running   0          3m21s

NAME                             TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes               ClusterIP      10.96.0.1       <none>        443/TCP          5d
service/python-app-service       LoadBalancer   10.101.30.109   <pending>     8000:30273/TCP   4m5s
service/typescript-app-service   LoadBalancer   10.96.84.8      <pending>     8080:31986/TCP   3m21s

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/python-app       3/3     3            3           4m5s
deployment.apps/typescript-app   3/3     3            3           3m21s

NAME                                        DESIRED   CURRENT   READY   AGE
replicaset.apps/python-app-fc4cb86cf        3         3         3       4m4s
replicaset.apps/typescript-app-7cfd496848   3         3         3       3m21s
```



## Task 2

```
>>> helm lint helm-app
==> Linting mywebapps
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```


```
>>> helm install --dry-run helm-hooks ./helm-app
NAME: helm-hooks
LAST DEPLOYED: Fri Nov  3 16:39:10 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
HOOKS:
```

```
>>> kubectl get po
NAME                              READY   STATUS      RESTARTS    AGE
nginx-app-69ccf856dd-cxlq7        1/1     Running     0          2m32s
post-install-hook                 0/1     Completed   0          2m37s
pre-install-hook                  0/1     Completed   0          2m67s
python-app-fc4cb86cf-b5f7d        1/1     Running     0          13m
python-app-fc4cb86cf-gtjcq        1/1     Running     0          13m
python-app-fc4cb86cf-q5sr4        1/1     Running     0          13m
typescript-app-7cfd496848-bj98c   1/1     Running     0          13m
typescript-app-7cfd496848-h2cqf   1/1     Running     0          13m
typescript-app-7cfd496848-n9mzp   1/1     Running     0          13m
```

## describe hooks (pre install hook)
```
>>> kubectl describe po pre-install-hook
Name:             pre-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.64.2
Start Time:       Fri Nov  3 16:39:10 2023
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.101.60.44
IPs:
  IP:  10.101.60.44
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
      Started:      Fri Nov  3 16:39:10 2023 +0300
      Finished:     Fri Nov  3 16:39:10 2023 +0300
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

## post install hook
```
>>> kubectl describe po post-install-hook
Name:             post-install-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri Nov  3 16:39:10 2023 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.101.60.45
IPs:
  IP:  10.102.60.45
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
      Started:      Fri Nov  3 16:39:10 2023 +0300
      Finished:     Fri Nov  3 16:39:10 2023 +0300
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

Implemented HELM chart for typescript app: `values.typescript.yaml`

Created library-chart/
`Chart.yaml`
`templates/_labels.tpl`


Library charts:
Update helm chart dependencies
```
>>> helm dependency update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Deleting outdated charts
```