## Deploying and accessing

```shell
minikube start
kubectl apply -f deployment.yaml
kubectl expose deployment app-python  --type=LoadBalancer --port=7098
minikube service app-python
```

1) `minikube start` - here minikube does it's own minikube things and prepare kubectl to work with minikube cluster
2) `kubectl apply -f deployment.yaml` starts new deployment
3) `kubectl expose...` creates a service for the deployment
4) this step is added, because minikube can not run LoadBalancer inside of it

```shell
> kubectl describe deployments     
Name:                   app-python
Namespace:              default
CreationTimestamp:      Sat, 09 Dec 2023 19:02:34 +0300
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=app-python
Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=app-python
  Containers:
   app-python:
    Image:        wiirtex/python_time_service:0.4.0
    Port:         7098/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   app-python-67b7cb9579 (2/2 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  2m53s  deployment-controller  Scaled up replica set app-python-67b7cb9579 to 2
```

```shell
> kubectl describe services   
Name:                     app-python
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=app-python
Type:                     LoadBalancer
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.105.106.132
IPs:                      10.105.106.132
Port:                     <unset>  7098/TCP
TargetPort:               7098/TCP
NodePort:                 <unset>  31849/TCP
Endpoints:                10.244.0.39:7098,10.244.0.40:7098
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```
