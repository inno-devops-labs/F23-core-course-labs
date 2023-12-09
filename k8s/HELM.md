```shell
helm install ch app-python
minikube service list
minikube service ch-app-python
```


```shell
> kubectl get pods,svc 
NAME                                  READY   STATUS             RESTARTS      AGE
pod/app-python-67b7cb9579-rcz5n       1/1     Running            1 (18m ago)   23m
pod/app-python-67b7cb9579-shwbv       1/1     Running            1 (18m ago)   23m
pod/ch-app-python-dd888f9c4-s4mjt     1/1     Running            0             3m54s
pod/hello-minikube-74f785749c-xnmcr   0/1     ImagePullBackOff   0             38d

NAME                    TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python      LoadBalancer   10.105.106.132   <pending>     7098:31849/TCP   21m
service/ch-app-python   ClusterIP      10.108.109.33    <none>        80/TCP           3m54s
service/kubernetes      ClusterIP      10.96.0.1        <none>        443/TCP          38d
```