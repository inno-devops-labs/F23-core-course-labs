# Helm

## Task 1
### `kubectl get pods,svc`
```
❯ kubectl get pods,svc
NAME                                    READY   STATUS    RESTARTS   AGE
pod/devops-python-app-74d9b8f97-ft75q   1/1     Running   0          61s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          5d13h
service/python-app   NodePort    10.109.194.54   <none>        8000:31209/TCP   61s
```
## Task 2
```
❯ kubectl get po
NAME                                 READY   STATUS    RESTARTS   AGE
devops-python-app-74d9b8f97-ft75q    1/1     Running   0          102s
❯ kubectl describe po post-install-hook
Error from server (NotFound): pods "post-install-hook" not found
❯ kubectl describe po pre-install-hook
Error from server (NotFound): pods "pre-install-hook" not found
```

Errors occured due to hook-delete-policy