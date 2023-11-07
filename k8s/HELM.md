# Helm

Output of `kubectl get pods,svc`

```
NAME                                  READY   STATUS             RESTARTS   AGE
pod/my-app-release-5644dbc566-qwckm   0/1     ImagePullBackOff   0          12m

NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
service/kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   20m
service/my-app-release   ClusterIP   10.109.154.115   <none>        80/TCP    12m
```