## Task 1

### helm install python helm-python/
```
NAME: python
LAST DEPLOYED: Tue Nov  7 22:29:24 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w python-helm-python'
  export SERVICE_IP=$(kubectl get svc --namespace default python-helm-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```

pic 1
pic 2
pic 3


### minikube service python-helm-python
```
|-----------|--------------------|-------------|---------------------------|
| NAMESPACE |        NAME        | TARGET PORT |            URL            |
|-----------|--------------------|-------------|---------------------------|
| default   | python-helm-python | http/5000   | http://192.168.49.2:30949 |
|-----------|--------------------|-------------|---------------------------|
🎉  Opening service default/python-helm-python in default browser...
/snap/core20/current/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /lib/x86_64-linux-gnu/libproxy.so.1)
Failed to load module: /home/iviosab/snap/code/common/.cache/gio-modules/libgiolibproxy.so
```

pic 4


### kubectl get pods,svc
```
NAME                                      READY   STATUS    RESTARTS      AGE
pod/moscow-time-697f64d98-7t6vs           1/1     Running   4 (13m ago)   6d22h
pod/moscow-time-697f64d98-p8j59           1/1     Running   4 (13m ago)   6d22h
pod/moscow-time-697f64d98-qb96w           1/1     Running   4 (13m ago)   6d22h
pod/moscow-time-go-6f768858d-f4g66        1/1     Running   4 (13m ago)   6d22h
pod/moscow-time-go-6f768858d-nj2w2        1/1     Running   4 (13m ago)   6d22h
pod/moscow-time-go-6f768858d-xknmg        1/1     Running   4 (13m ago)   6d22h
pod/python-helm-python-78995647c7-zb9s6   1/1     Running   0             11m

NAME                             TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes               ClusterIP      10.96.0.1       <none>        443/TCP          6d23h
service/moscow-time-go-service   NodePort       10.104.99.116   <none>        8080:30001/TCP   6d22h
service/moscow-time-service      NodePort       10.106.160.44   <none>        5000:30000/TCP   6d22h
service/python-helm-python       LoadBalancer   10.109.76.167   <pending>     5000:30949/TCP   11m
```


## Task 2

### helm lint helm-python
```
==> Linting helm-python
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### helm install --dry-run helm-hooks helm-python
```
NAME: helm-hooks
LAST DEPLOYED: Wed Nov  8 00:45:46 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: helm-python/templates/post-install-hook.yml
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
    imagePullPolicy: Always
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 20' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: helm-python/templates/pre-install-hook.yml
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
# Source: helm-python/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "helm-hooks-helm-python-test-connection"
  labels:
    helm.sh/chart: helm-python-0.1.0
    app.kubernetes.io/name: helm-python
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['helm-hooks-helm-python:5000']
  restartPolicy: Never
MANIFEST:
---
# Source: helm-python/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: helm-hooks-helm-python
  labels:
    helm.sh/chart: helm-python-0.1.0
    app.kubernetes.io/name: helm-python
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: helm-python/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: helm-hooks-helm-python
  labels:
    helm.sh/chart: helm-python-0.1.0
    app.kubernetes.io/name: helm-python
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: LoadBalancer
  ports:
    - port: 5000
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: helm-python
    app.kubernetes.io/instance: helm-hooks
---
# Source: helm-python/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helm-hooks-helm-python
  labels:
    helm.sh/chart: helm-python-0.1.0
    app.kubernetes.io/name: helm-python
    app.kubernetes.io/instance: helm-hooks
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: helm-python
      app.kubernetes.io/instance: helm-hooks
  template:
    metadata:
      labels:
        helm.sh/chart: helm-python-0.1.0
        app.kubernetes.io/name: helm-python
        app.kubernetes.io/instance: helm-hooks
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: helm-hooks-helm-python
      securityContext:
        {}
      containers:
        - name: helm-python
          securityContext:
            {}
          image: "iviosab/moscow_time:latest"
          imagePullPolicy: Always
          ports:
            - name: http
              containerPort: 5000
              protocol: TCP
          # livenessProbe:
          #   httpGet:
          #     path: /
          #     port: http
          # readinessProbe:
          #   httpGet:
          #     path: /
          #     port: http
          resources:
            {}

NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w helm-hooks-helm-python'
  export SERVICE_IP=$(kubectl get svc --namespace default helm-hooks-helm-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```
### helm install helm-hooks helm-python
```
NAME: helm-hooks
LAST DEPLOYED: Wed Nov  8 00:47:11 2023
NAMESPACE: default
STATUS: deployed
REVISION: 3
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w helm-hooks-helm-python'
  export SERVICE_IP=$(kubectl get svc --namespace default helm-hooks-helm-python --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:5000
```

### kubectl get pods
```
NAME                                     READY   STATUS      RESTARTS      AGE
helm-hooks-helm-python-9c7ff8cd8-kjntx   1/1     Running     0             56s
moscow-time-697f64d98-7t6vs              1/1     Running     5 (22m ago)   7d
moscow-time-697f64d98-p8j59              1/1     Running     5 (22m ago)   7d
moscow-time-697f64d98-qb96w              1/1     Running     5 (22m ago)   7d
moscow-time-go-6f768858d-f4g66           1/1     Running     5 (22m ago)   7d
moscow-time-go-6f768858d-nj2w2           1/1     Running     5 (22m ago)   7d
moscow-time-go-6f768858d-xknmg           1/1     Running     5 (22m ago)   7d
postinstall-hook                         0/1     Completed   0             55s
preinstall-hook                          0/1     Completed   0             79s
python-helm-python-78995647c7-zb9s6      1/1     Running     1 (22m ago)   147m
```

### kubectl describe pod preinstall-hook
```
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 00:55:44 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.77
IPs:
  IP:  10.244.0.77
Containers:
  pre-install-container:
    Container ID:  docker://0e6e5fba271d8708567b198a2d7f9178c21c757532facc538b6a50a9b9cdc3f8
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
      Started:      Wed, 08 Nov 2023 00:55:45 +0300
      Finished:     Wed, 08 Nov 2023 00:56:05 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6vs8b (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-6vs8b:
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
  Normal  Scheduled  2m10s  default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     2m9s   kubelet            Container image "busybox" already present on machine
  Normal  Created    2m9s   kubelet            Created container pre-install-container
  Normal  Started    2m9s   kubelet            Started container pre-install-container
```

### kubectl describe pod postinstall-hook
```
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 00:56:08 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.79
IPs:
  IP:  10.244.0.79
Containers:
  post-install-container:
    Container ID:  docker://f6f946330a048205349ca4fef22d8b4f394bde3a901658c13de3994529c6ea02
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
      Started:      Wed, 08 Nov 2023 00:56:13 +0300
      Finished:     Wed, 08 Nov 2023 00:56:33 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zmqt5 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-zmqt5:
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
  Normal  Scheduled  2m4s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    2m4s  kubelet            Pulling image "busybox"
  Normal  Pulled     2m    kubelet            Successfully pulled image "busybox" in 1.875371118s (4.028551527s including waiting)
  Normal  Created    2m    kubelet            Created container post-install-container
  Normal  Started    2m    kubelet            Started container post-install-container
```



