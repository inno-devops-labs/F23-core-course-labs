# Helm (lab 10)

## Task 1

### Python and Rust chart deployment

```bash
[user@fedora app-helm]$ helm install python . --values values.python.yaml 
NAME: python
LAST DEPLOYED: Sun Oct 29 13:04:00 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://python.app/

[user@fedora app-helm]$ helm install rust . --values values.rust.yaml 
NAME: rust
LAST DEPLOYED: Sun Oct 29 13:04:48 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://rust.app/
```

### minikube service

![](img/2.png)

```bash
curl -H "Host: python.app" 192.168.49.2
2023-10-29T13:05:14.345680+03:00

curl -H "Host: rust.app" 192.168.49.2
2023-10-29T13:08:24.083086627+03:00
```

### kubectl get pods,svc

```bash
NAME                                   READY   STATUS    RESTARTS   AGE
pod/python-app-helm-656f549cd6-bdfq9   1/1     Running   0          6m17s
pod/python-app-helm-656f549cd6-hcnkc   1/1     Running   0          6m17s
pod/python-app-helm-656f549cd6-hl5xk   1/1     Running   0          6m17s
pod/rust-app-helm-5ff5bffbc8-n9r6m     1/1     Running   0          5m29s
pod/rust-app-helm-5ff5bffbc8-whf9j     1/1     Running   0          5m29s
pod/rust-app-helm-5ff5bffbc8-zrkzm     1/1     Running   0          5m29s

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP          28m
service/python-app-helm   LoadBalancer   10.106.72.109   <pending>     8080:31213/TCP   6m17s
service/rust-app-helm     LoadBalancer   10.110.123.62   <pending>     8080:31945/TCP   5m29s
```

## Task 2

### helm lint

```bash
```

### helm install --dry-run helm-hooks

```bash
```

### Outputs

```bash
```

## Bonus

### Rust application

For Rust application I have created separated `values.rust.yaml` file

### Helm Library
