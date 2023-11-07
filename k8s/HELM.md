# Task 1

Installed chart:

```bash
helm create doe-app
# edited configs
helm package doe-app/
helm install doe-app doe-app-0.1.0.tgz
```

❯ kubectl get pods,svc:

```bash
NAME                           READY   STATUS    RESTARTS   AGE
pod/doe-app-5dcdfcfb58-8lw75   1/1     Running   0          3m42s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/doe-app      ClusterIP   10.106.32.132   <none>        8000/TCP   3m42s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    13d
```

# Task 2

❯ helm lint doe-app:

```bash
==> Linting doe-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

❯ helm install --dry-run helm-hooks doe-app:

```bash
NAME: helm-hooks
LAST DEPLOYED: Tue Nov  7 19:54:23 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: doe-app/templates/hooks/post-install.yaml
apiVersion: v1
kind: Pod
metadata:
   name: postinstall-hook
   annotations:
       "helm.sh/hook": "post-install"
       "helm.sh/hook-delete-policy": "hook-succeeded"
spec:
  containers:
  - name: post-install-container
    image: irsokolova/time_app
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 10' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: doe-app/templates/hooks/pre-install.yaml
apiVersion: v1
kind: Pod
metadata:
   name: preinstall-hook
   annotations:
       "helm.sh/hook": "pre-install"
       "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: pre-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 10' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---

...
```

❯ kubectl get po:

```bash
NAME              READY   STATUS    RESTARTS   AGE
preinstall-hook   1/1     Running   0          2s
```

Running it again 10 seconds later.\
❯ kubectl get po:

```bash
NAME                       READY   STATUS    RESTARTS   AGE
doe-app-5dcdfcfb58-qkhd5   1/1     Running   0          10s
postinstall-hook           1/1     Running   0          10s
```

❯ kubectl describe po preinstall-hook:

```yml
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 21:00:54 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Running
IP:               10.244.0.27
IPs:
  IP:  10.244.0.27
Containers:
  pre-install-container:
    Container ID:  docker://9166c3ae58314993d78bb6b93d9edd268d32ff97465fd1af42c695c66eecd2d1
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The pre-install hook is running && sleep 10
    State:          Running
      Started:      Tue, 07 Nov 2023 21:00:55 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-v6lqz (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kube-api-access-v6lqz:
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
  Normal  Scheduled  2s    default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2s    kubelet            Container image "busybox" already present on machine
  Normal  Created    2s    kubelet            Created container pre-install-container
  Normal  Started    2s    kubelet            Started container pre-install-container
```

❯ kubectl describe po postinstall-hook:

```yml
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 21:08:38 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
                  helm.sh/hook-delete-policy: hook-succeeded
Status:           Running
IP:               10.244.0.42
IPs:
  IP:  10.244.0.42
Containers:
  post-install-container:
    Container ID:  docker://6b1e675dc6942406dac7eeeaddea7cfbce395cf00765a0043d2157d412dfa296
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 10
    State:          Running
      Started:      Tue, 07 Nov 2023 21:08:41 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-9mzhq (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  kube-api-access-9mzhq:
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
  Normal  Scheduled  4s    default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    4s    kubelet            Pulling image "busybox"
  Normal  Pulled     2s    kubelet            Successfully pulled image "busybox" in 2.555853206s (2.555870191s including waiting)
  Normal  Created    2s    kubelet            Created container post-install-container
  Normal  Started    2s    kubelet            Started container post-install-container
```
