# Helm

Output of `minikube service chart-app-python`:

```
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   | chart-app-python | http/80     | http://192.168.49.2:31423 |
|-----------|------------------|-------------|---------------------------|
🎉  Opening service default/chart-app-python in default browser...
```

Output of command `kubectl get pods`:

```
NAME                                READY   STATUS    RESTARTS   AGE
chart-app-python-7cc85b6dc7-fh6bw   1/1     Running   0          4m27s
```

Output of command `kubectl get svc`:

```
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
chart-app-python   NodePort    10.111.121.245   <none>        80:31423/TCP   5m24s
kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP        17m
```

And working application:

![app-python](../images/Screenshot%20from%202023-12-09%2019-40-31.png)