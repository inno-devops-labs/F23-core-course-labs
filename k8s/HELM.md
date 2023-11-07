# Helm

Start `minikube`

```
minikube start
```

Install chart

```
helm install web-app-release ./web-app/
```

Start service in `minikube`

```
minikube service web-app-release
```

---

Output of `kubectl get pods,svc`

```
NAME                                   READY   STATUS    RESTARTS   AGE
pod/web-app-release-6554667c5f-nsrt6   1/1     Running   0          5m54s

NAME                      TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes        ClusterIP      10.96.0.1      <none>        443/TCP          9d
service/web-app-release   LoadBalancer   10.104.14.36   <pending>     8080:31241/TCP   5m54s
```
