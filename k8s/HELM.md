# Helm

## Installation

### I installed chart with the helm install command

```bash
helm install helm ./khays-app/
```

### Started service in `minikube`

```bash
minikube service helm-khays-app
|-----------|----------------|-------------|--------------|
| NAMESPACE |      NAME      | TARGET PORT |     URL      |
|-----------|----------------|-------------|--------------|
| default   | helm-khays-app |             | No node port |
|-----------|----------------|-------------|--------------|
😿  service default/helm-khays-app has no node port
```

---

## Output of kubectl get pods, svc

```bash
kubectl get pods,svc
NAME                                  READY   STATUS    RESTARTS   AGE
pod/helm-khays-app-868d458d66-nnzvp   1/1     Running   0          5m24s

NAME                     TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/helm-khays-app   ClusterIP   10.98.6.245   <none>        80/TCP    5m24s
service/kubernetes       ClusterIP   10.96.0.1     <none>        443/TCP   9d
```

---

## After troubleshooting hooks I got

```bash
kubectl get po
NAME                                READY   STATUS      RESTARTS   AGE
helm-khays-app-868d458d66-62tq2     1/1     Running     0          111s
helm-post-install-job-k9rj6         0/1     Completed   0          111s
helm-pre-install-job-bsqhf          0/1     Completed   0          132s
```

---

## Output of kubectl describe po

```bash
kubectl describe po helm-pre-install-job
Name:             helm-pre-install-job-bsqhf
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.39.6
Start Time:       Tue, 07 Nov 2023 22:35:26 +0300
Labels:           batch.kubernetes.io/controller-uid=07e4940e-4376-4cf0-8cda-a400f1fe7577
                  batch.kubernetes.io/job-name=helm-pre-install-job
                  controller-uid=07e4940e-4376-4cf0-8cda-a400f1fe7577
                  job-name=helm-pre-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.35
IPs:
  IP:           10.244.0.35
Controlled By:  Job/helm-pre-install-job
Containers:
  pre-install-job:
    Container ID:  docker://a375e57e9f56fa8936af3472f01d6936758d7eaa4a528ffcd105875ad177a615
    Image:         alpine:3.3
    Image ID:      docker-pullable://alpine@sha256:6bff6f65597a69246f79233ef37ff0dc50d97eaecbabbe4f8a885bf358be1ecf
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 22:35:28 +0300
      Finished:     Tue, 07 Nov 2023 22:35:48 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hc4qg (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-hc4qg:
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
  Normal  Scheduled  4m41s  default-scheduler  Successfully assigned default/helm-pre-install-job-bsqhf to minikube
  Normal  Pulled     4m41s  kubelet            Container image "alpine:3.3" already present on machine
  Normal  Created    4m41s  kubelet            Created container pre-install-job
  Normal  Started    4m40s  kubelet            Started container pre-install-job
```

---

```bash
kubectl describe po helm-post-install-job
Name:             helm-post-install-job-k9rj6
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.39.6
Start Time:       Tue, 07 Nov 2023 22:35:50 +0300
Labels:           batch.kubernetes.io/controller-uid=6488b1cd-0133-4d3a-8c0e-2a5431edacd8
                  batch.kubernetes.io/job-name=helm-post-install-job
                  controller-uid=6488b1cd-0133-4d3a-8c0e-2a5431edacd8
                  job-name=helm-post-install-job
Annotations:      <none>
Status:           Succeeded
IP:               10.244.0.36
IPs:
  IP:           10.244.0.36
Controlled By:  Job/helm-post-install-job
Containers:
  post-install-job:
    Container ID:  docker://fd0a59662678b924467c3949b5f87a58b39f0251335262578c59e032b5c24151
    Image:         alpine:3.3
    Image ID:      docker-pullable://alpine@sha256:6bff6f65597a69246f79233ef37ff0dc50d97eaecbabbe4f8a885bf358be1ecf
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 22:35:52 +0300
      Finished:     Tue, 07 Nov 2023 22:36:12 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wzpv9 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-wzpv9:
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
  Normal  Scheduled  4m19s  default-scheduler  Successfully assigned default/helm-post-install-job-k9rj6 to minikube
  Normal  Pulled     4m19s  kubelet            Container image "alpine:3.3" already present on machine
  Normal  Created    4m19s  kubelet            Created container post-install-job
  Normal  Started    4m18s  kubelet            Started container post-install-job
```

---

## To implement a hook delete policy in the Helm chart, you should make the following modifications to both hooks. Once the hooks have been executed successfully, they will be deleted

```bash
    "helm.sh/hook-delete-policy": hook-succeeded
```
