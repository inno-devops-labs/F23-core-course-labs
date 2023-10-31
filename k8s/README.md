# K8S

## Task 1

`kubectl get pods,svc`

```bash
PS C:\Users\Damir\Documents\devops-course> kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-6dbf94d6d4-fskr9   1/1     Running   0          3m32s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          8m23s
service/python-app   LoadBalancer   10.101.93.142   <pending>     8000:30136/TCP   2m31s
```

## Task 2

`kubectl get pods,svc`

```bash
PS C:\Users\Damir\Documents\devops-course\k8s\app_python> kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/python-app-7d674fd95-jt9zk   1/1     Running   0          50s
pod/python-app-7d674fd95-knrz6   1/1     Running   0          50s
pod/python-app-7d674fd95-r9hln   1/1     Running   0          50s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          23m
service/python-app   NodePort    10.103.179.73   <none>        8000:31680/TCP   34s
```

`minikube service --all`

![minikube service](images/task2_minikube.png)

## Bonus

`kubectl get pods,svc`

```bash
PS C:\Users\Damir\Documents\devops-course\k8s> kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS   AGE
pod/c-sharp-app-7cf987d7f6-5q9zj   1/1     Running   0          84s
pod/c-sharp-app-7cf987d7f6-jgbkg   1/1     Running   0          84s
pod/c-sharp-app-7cf987d7f6-lfq5b   1/1     Running   0          84s
pod/python-app-7d674fd95-jt9zk     1/1     Running   0          14m
pod/python-app-7d674fd95-knrz6     1/1     Running   0          14m
pod/python-app-7d674fd95-r9hln     1/1     Running   0          14m

NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/c-sharp-app   NodePort    10.100.124.164   <none>        80:31880/TCP     80s
service/kubernetes    ClusterIP   10.96.0.1        <none>        443/TCP          36m
service/python-app    NodePort    10.103.179.73    <none>        8000:31680/TCP   14m
```

`kubectl get pods -n ingress-nginx`

```bash
PS C:\Users\Damir> kubectl get pods,svc
NAME                               READY   STATUS    RESTARTS      AGE
pod/c-sharp-app-7cf987d7f6-5q9zj   1/1     Running   1 (56m ago)   101m
pod/c-sharp-app-7cf987d7f6-jgbkg   1/1     Running   1 (56m ago)   101m
pod/c-sharp-app-7cf987d7f6-lfq5b   1/1     Running   1 (56m ago)   101m
pod/python-app-7d674fd95-jt9zk     1/1     Running   1 (56m ago)   114m
pod/python-app-7d674fd95-knrz6     1/1     Running   1 (56m ago)   114m
pod/python-app-7d674fd95-r9hln     1/1     Running   1 (56m ago)   114m

NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/c-sharp-app   NodePort    10.100.124.164   <none>        80:31880/TCP     101m
service/kubernetes    ClusterIP   10.96.0.1        <none>        443/TCP          137m
service/python-app    NodePort    10.103.179.73    <none>        8000:31680/TCP   114m
PS C:\Users\Damir> kubectl get pods -n ingress-nginx
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-sxrww        0/1     Completed   0          55m
ingress-nginx-admission-patch-tx885         0/1     Completed   1          55m
ingress-nginx-controller-7799c6795f-cd8k8   1/1     Running     0          55m
```

`minikube service --all`

![minikube service](images/bonus_minikube.png)

`curl --resolve "moscow.time:80:$( minikube ip )" -i http://moscow.time`

```
HTTP/1.1 200 OK
Content-Length: 233
Content-Type: text/html; charset=utf-8
Date: Tue, 31 Oct 2023 15:14:36 GMT

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"...
```

`curl --resolve "programmer.profile:80:$( minikube ip )" -i http://programmer.profile`

```
HTTP/1.1 200 OK
Transfer-Encoding: chunked
Content-Type: text/html; charset=utf-8
Date: Tue, 31 Oct 2023 15:16:31 GMT

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="...
```