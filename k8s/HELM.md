# HELM
![Alt text](image.png)
## Task 1
```
~ helm install python . --values values_python.yaml
```

```
NAME: python
LAST DEPLOYED: Tue Nov 7 20:23:03 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
```

## Output of kubectl get pods,svc

```
[ilya@ilya-ThinkPad-T14-Gen-1 k8s]$ kubectl get pods,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/python-app-4c5d8ff35b-8g1xl   1/1     Running   0          32s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.94.0.1     <none>        443/TCP          2d12h
service/python-app   NodePort    10.92.10.85   <none>        8000:30203/TCP   42s
```

# Task 2

```
~ helm lint my-app
```

```
Linting my-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) faile
```

```
[ilya@ilya-ThinkPad-T14-Gen-1 k8s]$ kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
python-app-4c5d8ff35b-7b2kd   1/1     Running   0          81s
```