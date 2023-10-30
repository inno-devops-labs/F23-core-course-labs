# Kubernetes
## Lab 9
Commands:
```
~/iu-devops/monitoring$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
app-python   1/1     1            1           24m 
```

```
~/iu-devops/monitoring$ kubectl get pods
NAME                          READY   STATUS    RESTARTS      AGE
app-python-6f5d9cfdcf-sx47n   1/1     Running   1 (13m ago)   25m
```

```
~/iu-devops/monitoring$ kubectl get events
LAST SEEN   TYPE      REASON                    OBJECT                             MESSAGE
26m         Normal    Scheduled                 pod/app-python-6f5d9cfdcf-sx47n    Successfully assigned default/app-python-6f5d9cfdcf-sx47n to minikube
13m         Normal    Pulling                   pod/app-python-6f5d9cfdcf-sx47n    Pulling image "edikgoose/moscow-time-app:latest"
26m         Normal    Pulled                    pod/app-python-6f5d9cfdcf-sx47n    Successfully pulled image "edikgoose/moscow-time-app:latest" in 2.757616384s (6.347523891s including waiting)
13m         Normal    Created                   pod/app-python-6f5d9cfdcf-sx47n    Created container moscow-time-app
13m         Normal    Started                   pod/app-python-6f5d9cfdcf-sx47n    Started container moscow-time-app
13m         Normal    SandboxChanged            pod/app-python-6f5d9cfdcf-sx47n    Pod sandbox changed, it will be killed and re-created.
13m         Normal    Pulled                    pod/app-python-6f5d9cfdcf-sx47n    Successfully pulled image "edikgoose/moscow-time-app:latest" in 4.206597058s (4.206620755s including waiting)
26m         Normal    SuccessfulCreate          replicaset/app-python-6f5d9cfdcf   Created pod: app-python-6f5d9cfdcf-sx47n
26m         Normal    ScalingReplicaSet         deployment/app-python              Scaled up replica set app-python-6f5d9cfdcf to 1
27m         Normal    Scheduled                 pod/app.python-5968db7cd6-fnq45    Successfully assigned default/app.python-5968db7cd6-fnq45 to minikube
26m         Normal    Pulling                   pod/app.python-5968db7cd6-fnq45    Pulling image "edikgoose/moscow-time-app:latest"
27m         Warning   Failed                    pod/app.python-5968db7cd6-fnq45    Failed to pull image "edikgoose/moscow-time-app:latest": rpc error: code = Unknown desc = Error response from daemon: Head "https://registry-1.docker.io/v2/edikgoose/moscow-time-app/manifests/latest": net/http: TLS handshake timeout
27m         Warning   Failed                    pod/app.python-5968db7cd6-fnq45    Error: ErrImagePull
27m         Normal    BackOff                   pod/app.python-5968db7cd6-fnq45    Back-off pulling image "edikgoose/moscow-time-app:latest"
27m         Warning   Failed                    pod/app.python-5968db7cd6-fnq45    Error: ImagePullBackOff
26m         Normal    Pulled                    pod/app.python-5968db7cd6-fnq45    Successfully pulled image "edikgoose/moscow-time-app:latest" in 33.460950753s (33.46103158s including waiting)
26m         Normal    Created                   pod/app.python-5968db7cd6-fnq45    Created container moscow-time-app
26m         Normal    Started                   pod/app.python-5968db7cd6-fnq45    Started container moscow-time-app
26m         Normal    Killing                   pod/app.python-5968db7cd6-fnq45    Stopping container moscow-time-app
27m         Normal    SuccessfulCreate          replicaset/app.python-5968db7cd6   Created pod: app.python-5968db7cd6-fnq45
27m         Normal    ScalingReplicaSet         deployment/app.python              Scaled up replica set app.python-5968db7cd6 to 1
34m         Normal    NodeHasSufficientMemory   node/minikube                      Node minikube status is now: NodeHasSufficientMemory
34m         Normal    NodeHasNoDiskPressure     node/minikube                      Node minikube status is now: NodeHasNoDiskPressure
34m         Normal    NodeHasSufficientPID      node/minikube                      Node minikube status is now: NodeHasSufficientPID
34m         Normal    NodeAllocatableEnforced   node/minikube                      Updated Node Allocatable limit across pods
34m         Normal    Starting                  node/minikube                      Starting kubelet.
34m         Normal    NodeAllocatableEnforced   node/minikube                      Updated Node Allocatable limit across pods
34m         Normal    NodeHasSufficientMemory   node/minikube                      Node minikube status is now: NodeHasSufficientMemory
34m         Normal    NodeHasNoDiskPressure     node/minikube                      Node minikube status is now: NodeHasNoDiskPressure
34m         Normal    NodeHasSufficientPID      node/minikube                      Node minikube status is now: NodeHasSufficientPID
34m         Normal    RegisteredNode            node/minikube                      Node minikube event: Registered Node minikube in Controller
34m         Normal    Starting                  node/minikube                      
13m         Normal    Starting                  node/minikube                      
13m         Normal    RegisteredNode            node/minikube                      Node minikube event: Registered Node minikube in Controller
```

```angular2html
~/iu-devops/monitoring$ kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/edikgoose/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Mon, 30 Oct 2023 18:30:32 MSK
        provider: minikube.sigs.k8s.io
        version: v1.31.2
      name: cluster_info
    server: https://192.168.49.2:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Mon, 30 Oct 2023 18:30:32 MSK
        provider: minikube.sigs.k8s.io
        version: v1.31.2
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /home/edikgoose/.minikube/profiles/minikube/client.crt
    client-key: /home/edikgoose/.minikube/profiles/minikube/client.key
```

```
~/iu-devops/monitoring$ kubectl logs app-python-6f5d9cfdcf-sx47n
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
INFO:     10.244.0.1:28644 - "GET / HTTP/1.1" 200 OK
INFO:     10.244.0.1:28644 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```

```
~/iu-devops/monitoring$ kubectl get svc
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
app-python   LoadBalancer   10.108.85.31   <pending>     80:30241/TCP   7m48s
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP        36m
```


K8s service 
- [basic tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)
- [for minikube](https://minikube.sigs.k8s.io/docs/start/)