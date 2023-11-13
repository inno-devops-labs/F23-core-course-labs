Lab 10.
1)

```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % helm install py-app ./python-app-helm/

NAME: py-app
LAST DEPLOYED: Mon Nov 13 21:46:06 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w py-app-python-app'
  export SERVICE_IP=$(kubectl get svc --namespace default py-app-python-app --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8080
```
2)
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % kubectl get pods,svc
NAME                                    READY   STATUS    RESTARTS   AGE
pod/py-app-python-app-5c6b4fcb8-lb6bh   1/1     Running   0          3m15s
pod/py-app-python-app-5c6b4fcb8-n4ls8   1/1     Running   0          3m15s
pod/py-app-python-app-5c6b4fcb8-zxsjt   1/1     Running   0          3m15s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          7m25s
service/py-app-python-app   LoadBalancer   10.110.13.135   <pending>     8080:32743/TCP   3m15s
```
3)
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % kubectl get pods,svc
NAME                                    READY   STATUS    RESTARTS   AGE
pod/py-app-python-app-5c6b4fcb8-lb6bh   1/1     Running   0          3m15s
pod/py-app-python-app-5c6b4fcb8-n4ls8   1/1     Running   0          3m15s
pod/py-app-python-app-5c6b4fcb8-zxsjt   1/1     Running   0          3m15s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP          7m25s
service/py-app-python-app   LoadBalancer   10.110.13.135   <pending>     8080:32743/TCP   3m15s
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
|-----------|-------------------|-------------|---------------------------|
| NAMESPACE |       NAME        | TARGET PORT |            URL            |
|-----------|-------------------|-------------|---------------------------|
| default   | py-app-python-app | http/8080   | http://192.168.49.2:32743 |
|-----------|-------------------|-------------|---------------------------|
🏃  Starting tunnel for service kubernetes.
🏃  Starting tunnel for service py-app-python-app.
|-----------|-------------------|-------------|------------------------|
| NAMESPACE |       NAME        | TARGET PORT |          URL           |
|-----------|-------------------|-------------|------------------------|
| default   | kubernetes        |             | http://127.0.0.1:51724 |
| default   | py-app-python-app |             | http://127.0.0.1:51726 |
|-----------|-------------------|-------------|------------------------|
🎉  Opening service default/kubernetes in default browser...
🎉  Opening service default/py-app-python-app in default browser...
```
4)
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % helm install --dry-run python-hook ./python-app-helm/
NAME: python-hook
LAST DEPLOYED: Mon Nov 13 21:58:35 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: python-app/templates/post-install-hook.yaml
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
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: python-app/templates/pre-install-hook.yaml
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
# Source: python-app/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "python-hook-python-app-test-connection"
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: python-hook
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['python-hook-python-app:8080']
  restartPolicy: Never
MANIFEST:
---
# Source: python-app/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: python-hook-python-app
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: python-hook
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: python-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: python-hook-python-app
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: python-hook
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: LoadBalancer
  ports:
    - port: 8080
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: python-hook
---
# Source: python-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-hook-python-app
  labels:
    helm.sh/chart: python-app-0.1.0
    app.kubernetes.io/name: python-app
    app.kubernetes.io/instance: python-hook
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
    
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/instance: python-hook
    aboba: "aboba"
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: python-app
      app.kubernetes.io/instance: python-hook      
      app.kubernetes.io/version: "1.16.0"
      app.kubernetes.io/managed-by: Helm
      app.kubernetes.io/instance: python-hook
      aboba: "aboba"
  template:
    metadata:
      labels:
        helm.sh/chart: python-app-0.1.0
        app.kubernetes.io/name: python-app
        app.kubernetes.io/instance: python-hook
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm        
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/instance: python-hook
        aboba: "aboba"
    spec:
      serviceAccountName: python-hook-python-app
      securityContext:
        {}
      containers:
        - name: python-app
          securityContext:
            {}
          image: "pavel5609/do_course:latest"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 8080
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
           You can watch the status of by running 'kubectl get --namespace default svc -w python-hook-python-app'
  export SERVICE_IP=$(kubectl get svc --namespace default python-hook-python-app --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8080
```
5)
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % helm install --dry-run python-hook ./python-app-helm/
NAME: python-hook
LAST DEPLOYED: Mon Nov 13 21:59:51 2023
NAMESPACE: default
STATUS: pending-install
REVISION: 1
HOOKS:
---
# Source: python-app/templates/post-install-hook.yaml
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
    command: ['sh', '-c', 'echo The post-install hook is running && sleep 15' ]
  restartPolicy: Never
  terminationGracePeriodSeconds: 0
---
# Source: python-app/templates/pre-install-hook.yaml
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
  ...
  ```
6)
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % helm install python-hook ./python-app-helm/
NAME: python-hook
LAST DEPLOYED: Mon Nov 13 22:02:19 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get --namespace default svc -w python-hook-python-app'
  export SERVICE_IP=$(kubectl get svc --namespace default python-hook-python-app --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
  echo http://$SERVICE_IP:8080
```
7)
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % kubectl get po
NAME                                     READY   STATUS    RESTARTS   AGE
py-app-python-app-5c6b4fcb8-lb6bh        1/1     Running   0          17m
py-app-python-app-5c6b4fcb8-n4ls8        1/1     Running   0          17m
py-app-python-app-5c6b4fcb8-zxsjt        1/1     Running   0          17m
python-hook-python-app-b66cf54cc-kxkmd   1/1     Running   0          91s
python-hook-python-app-b66cf54cc-nkrb5   1/1     Running   0          91s
python-hook-python-app-b66cf54cc-rml9p   1/1     Running   0          91s
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s % kubectl describe po preinstall-hook
Name:             preinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 22:04:32 +0300
Labels:           <none>
Annotations:      helm.sh/hook: pre-install
Status:           Succeeded
IP:               10.244.0.49
IPs:
  IP:  10.244.0.49
Containers:
  pre-install-container:
    Container ID:  docker://2c38cad7361d3477e503a9617a061e47c991585ee38aa6db6296f95929ba575f
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
      Started:      Mon, 13 Nov 2023 22:04:33 +0300
      Finished:     Mon, 13 Nov 2023 22:04:53 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-phvdq (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-phvdq:
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
  Normal  Scheduled  99s   default-scheduler  Successfully assigned default/preinstall-hook to minikube
  Normal  Pulled     98s   kubelet            Container image "busybox" already present on machine
  Normal  Created    98s   kubelet            Created container pre-install-container
  Normal  Started    98s   kubelet            Started container pre-install-container
```
```
pbakharuev@mbp-pbakharuev-OZON-FVFG74Q1Q05N k8s %  kubectl describe po postinstall-hook 
Name:             postinstall-hook
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Wed, 08 Nov 2023 22:04:55 +0300
Labels:           <none>
Annotations:      helm.sh/hook: post-install
Status:           Succeeded
IP:               10.244.0.53
IPs:
  IP:  10.244.0.53
Containers:
  post-install-container:
    Container ID:  docker://11983defb61e8733a34a9594c388b94a713f51b5b107ec42b725da27a16c85ee
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
      Started:      Mon, 13 Nov 2023 22:05:00 +0300
      Finished:     Mon, 13 Nov 2023 22:05:15 +0300
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-b5sg6 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-b5sg6:
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
  Normal  Scheduled  103s  default-scheduler  Successfully assigned default/postinstall-hook to minikube
  Normal  Pulling    102s  kubelet            Pulling image "busybox"
  Normal  Pulled     99s   kubelet            Successfully pulled image "busybox" in 3.687247197s (3.687258935s including waiting)
  Normal  Created    99s   kubelet            Created container post-install-container
  Normal  Started    98s   kubelet            Started container post-install-container
```

