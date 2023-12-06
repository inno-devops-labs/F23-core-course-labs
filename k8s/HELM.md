# Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

1. Learn About Helm: Done

2. Install Helm: Done

3. Create Your Own Helm Chart:

Generate a Helm chart for your application.

```bash
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

1. Learn About Chart Hooks: Done
2. Implement Helm Chart Hooks: Done
3. Troubleshoot hooks: Done
4. Provide output:

```bash
$ kubectl get pods
NAME                                     READY   STATUS      RESTARTS   AGE
helm-hooks-app-python-5dcf4cdcf7-lgvgk   1/1     Running     0          4m31s
postinstall-hook                         0/1     Completed   0          4m31s
preinstall-hook                          0/1     Completed   0          4m48s
```

```bash
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

```bash
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
```bash
$ kubectl get po
NAME                                     READY   STATUS    RESTARTS   AGE
helm-hooks-app-python-5dcf4cdcf7-pkjf2   1/1     Running   0          27s
```

```bash
$ kubectl describe po preinstall-hook
Error from server (NotFound): pods "preinstall-hook" not found
```

```bash
$ kubectl describe po postinstall-hook
Error from server (NotFound): pods "postinstall-hook" not found
```

**Due to hook delete policy, hook pods are deleted after they are completed.**

## Bonus

1. Helm Chart for Extra App:

```bash
helm create app-go
```

Update `values.yaml` and `templates/deployment.yaml` in the same way as for `app-python`.

Install the chart:

```bash
helm install app-go-chart app-go -f app-go/values.yaml
```

Verify the chart by checking the Workloads page in the Minikube dashboard:

![Workloads](https://i.imgur.com/ai77OQ2.png)

Access the app:

```bash
minikube service app-go-chart
```

![minikube service app-go-chart](https://i.imgur.com/PNvVgDr.png)

![App](https://i.imgur.com/OVdk0du.png)

```bash
$ kubectl get pods,svc
NAME                                READY   STATUS    RESTARTS   AGE
pod/app-go-chart-5996c54967-6t2wc   1/1     Running   0          4m37s

NAME                   TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/app-go-chart   NodePort    10.106.254.202   <none>        80:31123/TCP   4m37s
service/kubernetes     ClusterIP   10.96.0.1        <none>        443/TCP        7d5h
```

2. Helm Library Charts: done

3. Create a Library Chart:

```bash
helm create mylibchart
rm -rf mylibchart/templates/*
rm -f mylibchart/values.yaml
```

Add a distinctive label to library chart in mylibchart/templates/_labels.tpl:
```yaml
additional_template_label: "bonus library chart label"
```

Add dependency entry to `Chart.yml` of both `app-python` and `app-go`:

```yaml
dependencies:
  - name: mylibchart
    version: 0.1.0
    repository: "file://../mylibchart"
```

Update `deployment.yaml` with `mylibchart.labels` declaration for both `app-python` and `app-go`:

```yaml
{{- include "mylibchart.labels" . | indent 4 }}
```

Update dependencies of charts:

```bash
$ helm dependency update app-go
Saving 1 charts
Deleting outdated charts

$ helm dependency update app-python
Saving 1 charts
Deleting outdated charts
```

Install (or upgrade) charts:

```bash
helm install app-python-chart app-python -f app-python/values.yaml
helm install app-go-chart app-go -f app-go/values.yaml
```

Now we can see updated labels and our `additional_template_label=bonus-library-chart-label` for both pods:

```bash
$ kubectl describe po app-python-chart
Name:             app-python-chart-788769fcff-p62bj
Namespace:        default
Priority:         0
Service Account:  app-python-chart
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:12:05 +0300
Labels:           additional_template_label=bonus-library-chart-label
                  app.kubernetes.io/instance=app-python-chart
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=app-python
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=app-python-0.1.0
                  pod-template-hash=788769fcff
Annotations:      <none>
Status:           Running
IP:               10.244.0.64
IPs:
  IP:           10.244.0.64
Controlled By:  ReplicaSet/app-python-chart-788769fcff
Containers:
  app-python:
    Container ID:   docker://f95692c6348e43481e9a4665b68f065d2fe5c669520a13240757a59f03ee8c29
    Image:          docker.io/ar7ch/devops-app-python:latest
    Image ID:       docker-pullable://ar7ch/devops-app-python@sha256:e385636460645fb144fed865c023c39e55065e04917f4b798c35522633e61d77
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 08 Nov 2023 03:12:06 +0300
    Ready:          True
    Restart Count:  0
    Liveness:       http-get http://:http/time delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:http/time delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gnb84 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-gnb84:
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
  Normal  Scheduled  6m32s  default-scheduler  Successfully assigned default/app-python-chart-788769fcff-p62bj to minikube
  Normal  Pulled     6m32s  kubelet            Container image "docker.io/ar7ch/devops-app-python:latest" already present on machine
  Normal  Created    6m32s  kubelet            Created container app-python
  Normal  Started    6m32s  kubelet            Started container app-python
```

```bash
 kubectl describe po app-go-chart
Name:             app-go-chart-5f95788f99-pwvth
Namespace:        default
Priority:         0
Service Account:  app-go-chart
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 03:15:30 +0300
Labels:           additional_template_label=bonus-library-chart-label
                  app.kubernetes.io/instance=app-go-chart
                  app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=app-go
                  app.kubernetes.io/version=1.16.0
                  helm.sh/chart=app-go-0.1.0
                  pod-template-hash=5f95788f99
Annotations:      <none>
Status:           Running
IP:               10.244.0.66
IPs:
  IP:           10.244.0.66
Controlled By:  ReplicaSet/app-go-chart-5f95788f99
Containers:
  app-go:
    Container ID:   docker://57ed6b62cae3b1b506e98f015ec0fa3e342c7b493ac817a86ec0fcd231c8d816
    Image:          docker.io/ar7ch/devops-app-go:latest
    Image ID:       docker-pullable://ar7ch/devops-app-go@sha256:253dcf744d0fe968fb46c849a853ab7a5e7dd76438466cb0d8d6c44ad74ba5d9
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 08 Nov 2023 03:15:31 +0300
    Ready:          True
    Restart Count:  0
    Liveness:       http-get http://:http/time delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      http-get http://:http/time delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-k2lvl (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-k2lvl:
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
  Normal  Scheduled  29s   default-scheduler  Successfully assigned default/app-go-chart-5f95788f99-pwvth to minikube
  Normal  Pulled     29s   kubelet            Container image "docker.io/ar7ch/devops-app-go:latest" already present on machine
  Normal  Created    29s   kubelet            Created container app-go
  Normal  Started    29s   kubelet            Started container app-go
```
