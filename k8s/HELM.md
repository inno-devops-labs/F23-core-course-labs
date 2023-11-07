# HELM

## Task 1
`helm install python . --values values.python.yaml`

```
NAME: python
LAST DEPLOYED: Tue Nov  7 21:09:45 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services python-helm-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

`kubectl get pods,svc`

```
NAME                                   READY   STATUS    RESTARTS        AGE
pod/app-c-sharp-b95d6b4b8-4bs88        1/1     Running   2 (3m1s ago)    6d23h
pod/app-c-sharp-b95d6b4b8-cml4r        1/1     Running   2 (3m8s ago)    6d23h
pod/app-c-sharp-b95d6b4b8-pldvs        1/1     Running   2 (3m3s ago)    6d23h
pod/app-python-79b9985c48-5whlt        1/1     Running   2 (2m42s ago)   6d23h
pod/app-python-79b9985c48-hxhcx        1/1     Running   2 (2m42s ago)   6d23h
pod/app-python-79b9985c48-rv76f        1/1     Running   2 (2m36s ago)   6d23h
pod/python-helm-app-768f94d4d6-xcf7r   1/1     Running   0               2m18s

NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-c-sharp       NodePort    10.98.195.174   <none>        80:31880/TCP     6d23h
service/app-python        NodePort    10.100.15.167   <none>        8080:31680/TCP   6d23h
service/kubernetes        ClusterIP   10.96.0.1       <none>        443/TCP          7d3h
service/python-helm-app   NodePort    10.96.68.163    <none>        8080:32231/TCP   2m18s
```

## Task 2

`helm lint .`

```
==> Linting .
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

`kubectl get po`

```
NAME                                  READY   STATUS      RESTARTS        AGE
app-c-sharp-b95d6b4b8-4bs88           1/1     Running     2 (9m46s ago)   6d23h
app-c-sharp-b95d6b4b8-cml4r           1/1     Running     2 (9m53s ago)   6d23h
app-c-sharp-b95d6b4b8-pldvs           1/1     Running     2 (9m48s ago)   6d23h
app-python-79b9985c48-5whlt           1/1     Running     2 (9m27s ago)   6d23h
app-python-79b9985c48-hxhcx           1/1     Running     2 (9m27s ago)   6d23h
app-python-79b9985c48-rv76f           1/1     Running     2 (9m21s ago)   6d23h
helm-hooks-helm-app-7d598dd97-2759n   1/1     Running     0               43s
postinstall-hook                      0/1     Completed   0               43s
preinstall-hook                       0/1     Completed   0               69s
python-helm-app-768f94d4d6-xcf7r      1/1     Running     0               9m3s
```

`kubectl describe po preinstall-hook`

```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 21:17:39 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.50
IPs:
  IP:  10.244.0.50
Containers:
  pre-install-container:
    Container ID:  docker://d84ec5ebf1ab14528cac59f4ae3dab54d08540b2aed390547c18c5c4d9cc751e
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
      Started:      Tue, 07 Nov 2023 21:17:43 +0300
      Finished:     Tue, 07 Nov 2023 21:18:03 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6zn9c (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-6zn9c:
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
  Normal  Scheduled  110s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulling    109s  kubelet            Pulling image "busybox"
  Normal  Pulled     106s  kubelet            Successfully pulled image "busybox" in 3.745591263s (3.745600587s including waiting)
  Normal  Created    106s  kubelet            Created container pre-install-container
  Normal  Started    106s  kubelet            Started container pre-install-container
```

`kubectl describe po postinstall-hook`

```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 07 Nov 2023 21:18:05 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.52
IPs:
  IP:  10.244.0.52
Containers:
  post-install-container:
    Container ID:  docker://b086971939b02e118d3e3e9a0490ac34ead7783c517270c4ee24f8333c884e3a
    Image:         busybox
    Image ID:      docker-pullable://busybox@sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The post-install hook is running && sleep 20
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 07 Nov 2023 21:18:06 +0300
      Finished:     Tue, 07 Nov 2023 21:18:26 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7hpb5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-7hpb5:
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
  Normal  Scheduled  2m11s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulled     2m11s  kubelet            Container image "busybox" already present on machine
  Normal  Created    2m11s  kubelet            Created container post-install-container
  Normal  Started    2m11s  kubelet            Started container post-install-container
```

### Delete policy
- Add `"helm.sh/hook-delete-policy": hook-succeeded` in post-install-job.yaml and pre-install-job.yaml

## Bonus task 

`helm install sharp . --values values.sharp.yaml`

```
NAME: sharp
LAST DEPLOYED: Tue Nov  7 21:25:44 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services sharp-helm-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

`kubectl get pods,svc`

```
NAME                                      READY   STATUS    RESTARTS      AGE
pod/app-c-sharp-b95d6b4b8-4bs88           1/1     Running   2 (18m ago)   6d23h
pod/app-c-sharp-b95d6b4b8-cml4r           1/1     Running   2 (18m ago)   6d23h
pod/app-c-sharp-b95d6b4b8-pldvs           1/1     Running   2 (18m ago)   6d23h
pod/app-python-79b9985c48-5whlt           1/1     Running   2 (17m ago)   6d23h
pod/app-python-79b9985c48-hxhcx           1/1     Running   2 (17m ago)   6d23h
pod/app-python-79b9985c48-rv76f           1/1     Running   2 (17m ago)   6d23h
pod/helm-hooks-helm-app-7d598dd97-2759n   1/1     Running   0             9m2s
pod/python-helm-app-768f94d4d6-xcf7r      1/1     Running   0             17m
pod/sharp-helm-app-6c7b986794-khkvb       1/1     Running   0             60s

NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-c-sharp           NodePort    10.98.195.174    <none>        80:31880/TCP     6d23h
service/app-python            NodePort    10.100.15.167    <none>        8080:31680/TCP   6d23h
service/helm-hooks-helm-app   ClusterIP   10.110.45.181    <none>        80/TCP           9m2s
service/kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          7d3h
service/python-helm-app       NodePort    10.96.68.163     <none>        8080:32231/TCP   17m
service/sharp-helm-app        NodePort    10.103.234.242   <none>        80:32508/TCP     60s
```

### I have updated `helm-chart-app/templates/deployment.yaml`

`helm dependency update .`

```
Saving 1 charts
Deleting outdated charts
```

`helm install --dry-run test . --values values.sharp.yaml`

```
NAME: test
LAST DEPLOYED: Tue Nov  7 21:34:44 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: helm-app/templates/post-install-job.yaml
apiVersion: v1
kind: Pod
metadata:
  name: postinstall-hook
  annotations:
    "helm.sh/hook": "post-install"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  containers:
  - name: post-install-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: helm-app/templates/pre-install-job.yaml
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
    command: ['sh', '-c', 'echo The pre-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: helm-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "test-helm-app-test-connection"
  labels:
    helm.sh/chart: helm-app-0.1.0
    app.kubernetes.io/name: helm-app
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['test-helm-app:80']
  restartPolicy: Never
MANIFEST:
---
# Source: helm-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: test-helm-app
  labels:
    helm.sh/chart: helm-app-0.1.0
    app.kubernetes.io/name: helm-app
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: helm-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: test-helm-app
  labels:
    helm.sh/chart: helm-app-0.1.0
    app.kubernetes.io/name: helm-app
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: helm-app
    app.kubernetes.io/instance: test
---
# Source: helm-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-helm-app
  labels:
    
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/instance: test
spec:
  replicas: 1
  selector:
    matchLabels:
      
      app.kubernetes.io/version: "1.16.0"
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/instance: test
  template:
    metadata:
      labels:
        
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/instance: test
    spec:
      serviceAccountName: test-helm-app
      securityContext:
        {}
      containers:
        - name: helm-app
          securityContext:
            {}
          image: "annadluzhinskaya/pet-app:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          resources:
            {}

NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services test-helm-app)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```
