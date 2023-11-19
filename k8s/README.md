### Output of the `kubectl get pods,svc` command
```
NAME                                     READY   STATUS             RESTARTS   AGE
pod/app-python-node-2-5d84c8fd6f-qspzp   0/1     ImagePullBackOff   0          88s
pod/app-python-node-66c4798c8-8h4qz      0/1     ImagePullBackOff   0          6m46s
pod/my-app-release-5644dbc566-qwckm      0/1     ImagePullBackOff   0          12d

NAME                      TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python-node   LoadBalancer   10.106.236.58    <pending>     8089:30992/TCP   5m19s
service/kubernetes        ClusterIP      10.96.0.1        <none>        443/TCP          12d
service/my-app-release    ClusterIP      10.109.154.115   <none>        80/TCP           12d
```